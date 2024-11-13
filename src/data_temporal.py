import pickle as pkl
import numpy as np
from request import BaseRequest, RequestTest
from pathlib import Path

BASE_DIR = str(Path(__file__).parent.parent.resolve())

def requests_time_homogeneous(seed=20230215,
    request_limit_hour=7,
    expected_request_day=500
):
    
    np.random.seed(seed)
    # each customer with an arrival rate \lambda (expected number of requests every minute),
    lam = expected_request_day / (request_limit_hour * 60)
    # create intervals
    tau = 1 / lam
    # 需求产生的时间间隔
    s = np.random.exponential(tau, int(expected_request_day))
    # 对时间间隔取整（四舍五入）
    s = np.round(s)
    # calculate the requesting time (cumulate intervals), stop when it > request limit time period
    T = [
        sum(s[: (i + 1)])
        for i in range(len(s))
        if sum(s[: (i + 1)]) <= 60 * request_limit_hour
    ]

    return T


def requests_time_heterogeneous(
    seed=20230215,
    request_limit_hour=7,
    expected_request_day=500
):
    """
    generate the arriving time of requests during a day, with the heterogeneous arrival rates
    """
    np.random.seed(seed)
    # each customer with an arrival rate \lambda (expected number of requests every minute),
    lam = expected_request_day / (request_limit_hour * 60)
    
    # create intervals
    tau_0, tau_1, tau_2 = 1 / lam, 1/(1.5*lam), 1/(2*lam)
    
    # 需求产生的时间间隔, 对时间间隔取整（四舍五入）
    s_0 = np.round(np.random.exponential(tau_0, int(expected_request_day)))
    s_1 = np.round(np.random.exponential(tau_1, int(expected_request_day)))
    s_2 = np.round(np.random.exponential(tau_2, int(expected_request_day)))
    
    # vary the arrival rate of requests, step function
    T = [] # the list to store the arriving time of requests during a day
    t = 0
    i, j, k = 0, 0, 0 # the counter of s_0, s_1 and s_2
    # calculate the requesting time (cumulate intervals)
    while t < 60 * request_limit_hour:
        if t <= 60 or 150<t<=260 or 350<t<=420:
            t += s_0[i]
            i += 1
        elif 60<t<=90 or 120<t<=150 or 260<t<=290 or 320<t<=350:
            t += s_1[j]
            j += 1
        elif 90<t<=120 or 290<t<=320:
            t += s_2[k]
            k += 1
        
        T.append(t)
    
    #print(T, len(T))
    return T

