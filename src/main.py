import pickle as pkl
import numpy as np
from request import BaseRequest, RequestTest
from pathlib import Path
from data_temporal import requests_time_heterogeneous, requests_time_homogeneous
from data_spatial import normal, power_law, power_law_2

BASE_DIR = str(Path(__file__).parent.parent.resolve())

def day_data(Request, temporal =  "homo", spatial="normal", seed=20230508, expected_request_day=500):
    """
    generate requests of a day,
    args:
        Request: a class of requests
        I: the number of locations of customers
        
    """
    requests_list = []
    # first, create the arival time of requests
    if temporal == "homo":
        T = requests_time_homogeneous(seed=seed, expected_request_day=expected_request_day)
    
    elif temporal == "heter":
        T = requests_time_heterogeneous(seed=seed, expected_request_day=expected_request_day)
    
    # next, create the loctions of customers
    if spatial == "normal":
        locations = normal(seed=seed, I = expected_request_day)
    
    elif spatial == "power_law":
        locations = power_law(seed=seed, population=expected_request_day)
    
    I = len(locations)
        
    # finally, link requests and customers
    Pi = [round((1 / I) * (i + 1), 3) for i in range(I)]
    Pi[0] = 0
    request_number = 0
    for t in T:
        u = np.random.rand()
        if u < Pi[1]:
            customer_num = 0
            a_request = Request(
                request_number, t, locations[customer_num][0], locations[customer_num][1]
            )
            requests_list.append(a_request)
            request_number += 1
            continue
        for i in range(len(Pi)):
            if u < Pi[i]:
                customer_num = i
                a_request = Request(
                    request_number, t, locations[customer_num][0], locations[customer_num][1]
                )
                requests_list.append(a_request)
                request_number += 1
                break

    return requests_list

if __name__ == "__main__":
    temporal, spatial, expected_request_day = "homo", "normal", 500
    seed_train, seed_test = 20220506, 20230215
    n_train_data, n_test_data = 500, 125
    data_list_train = []
    data_list_test = []

    # training data
    for i in range(n_train_data):
        print(seed_train)
        requests_a_day = day_data(BaseRequest,temporal=temporal, spatial=spatial,expected_request_day=expected_request_day, seed=seed_train)
        seed_train += 10000
        data_list_train.append(requests_a_day)
    with open(f"{BASE_DIR}/data/data_list_train_{temporal}_{spatial}.pickle", "wb") as f:
        pkl.dump(data_list_train, f)

    # test data
    for i in range(n_test_data):
        print(seed_test)
        requests_a_day = day_data(RequestTest, temporal=temporal, spatial=spatial,expected_request_day=expected_request_day,seed=seed_test)
        seed_test += 10000
        data_list_test.append(requests_a_day)
    with open(f"{BASE_DIR}/data/data_list_test_{temporal}_{spatial}.pickle", "wb") as f:
        pkl.dump(data_list_test, f)