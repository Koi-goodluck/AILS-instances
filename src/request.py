import numpy as np
from dataclasses import dataclass, field
from typing import Optional


@dataclass
class BaseRequest:
    """
    a class to define a request:

        t_arriving: the arrving time of the request
        (x, y): the location (coordinates) of the request
        limit_period: the limitation delivery time of the request,
        default value is set to 4 hours
        t_end: the deadline of the service to a request

    """
    number: int # according to the arrival time
    t_arriving: float
    x: float
    y: float
    location: tuple = field(init=False)
    limit_period: int = 4 * 60
    t_end: float = field(init=False)
    vehicle_type: Optional[int] = None
    vehicle_number: Optional[int] = None

    def __post_init__(self):
        self.location = (self.x, self.y)
        self.t_end = self.t_arriving + self.limit_period


@dataclass
class RequestTest(BaseRequest):
    """
    request should consider more in test phase for better visualization:
        delivery_mode: 0 -> drone, 1 -> vehicle, 2 -> reject; default value is set to None
        vehicle_number: if the request is delivered by the vehicle,
            it represents the vehicle number; default value is None
        t_finish: if the request is not rejected, it represents the time of
            finishing service; default value is None
    """

    insert_cost: Optional[float] = None
    t_finish: Optional[float] = None

    def cal_remain_t(self):
        if self.t_finish is None:
            print("Finishi-serving time of the request is not known!")
        else:
            self.t_remain = self.t_end - self.t_finish
