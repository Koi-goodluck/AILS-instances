
This repository contains computational instances for the paper "*A Learning and Searching Integration Approach for Same-day Delivery Problem with Heterogeneous Fleets Considering Uncertainty*".

#### Simulation data

Four types of data distributions are created, denoted as "Homo, Normal", "Homo, Power-law", "Heter, Normal" and "Heter, Power-law". Refer to Section 5.1 Data preparation in the paper for details. 

The training data set contains 500 instances of "Homo, Normal", while the test set  also contains 500 instances with each type of  125 instances. 

We provide both codes and detailed data here. 

- `src`：Codes for creating training and test data. Run `main.py` to create data. Change parameters 'temporal' and 'spatial' in `main.py` to create different types of test data.

- `data`: This folder contains the detailed training and test data utilized in the paper. 

  For example, `data_list_train_homo_normal.pickle` is a list containing 500 days of data and each element in the list represents detailed request information arriving during a day. Request information is created through a class named `BaseRequest` in `reques.py`.

The `.pickle` can be loaded use the following codes, and please refer to https://docs.python.org/3/library/pickle.html for learning more about `pickle` module.

```python
import pickle as pkl
with open ('data_list_train_homo_normal.pickle', 'rb') as f:
	data_list = pkl.load(f)
```

#### Case study

The case study data is in the folder `casestudy`, and derives from  an algorithm competition of Tianchi on last-mile express delivery. Refer to https://tianchi.aliyun.com/competition/entrance/231581/information for details.

**Raw data:**

- `Distribution_points.csv`: This file involves locations of 124 distribution points (longitudes and latitudes).
- `Delivery_points.csv`: This file involves locations of all delivery points.
- `O2O_orders.csv`: The information of O2O orders, including `Order_id`, `Spot_id`, `Shop_id`, `Pickup_time`, `Delivery_time` and `Num` (the number of packages in an order)

**Processed data in case study:**

Refer to our paper for the detailed data processing.

- `Case1-512.csv`: The information of 512 delivery points in the first case, including the arrival time, delivery deadlines, locations (longitudes and latitudes) and distances to the depot.
- `Case1-895.csv`:The information of 895 delivery points in the second case, including the arrival time, delivery deadlines, locations (longitudes and latitudes) and distances to the depot.



