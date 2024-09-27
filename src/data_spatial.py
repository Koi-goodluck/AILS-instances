import pickle as pkl
import numpy as np
from request import BaseRequest, RequestTest
from pathlib import Path
from scipy.stats import pareto
import matplotlib.pyplot as plt

BASE_DIR = str(Path(__file__).parent.parent.resolve())

# normal distribution
def normal(seed=20230507, I = 500, stand_dev=3.0):
    np.random.seed(seed)
    # create locations
    # the center: depot (0,0);  the standard deviation: 3
    xy_array = np.random.normal(0, stand_dev, (I, 2))
    
    return xy_array

# power-law population
def power_law(seed=20230507, population = 500, N_regions = 20, city_range = 6, region_range = 0.5, stand_dev=3):
    np.random.seed(seed)
    
    # first, generate N regions randomly
    # assume a region is a square grid with the length=1km
    #region_center = city_range * np.random.rand(N_regions, 2)
    region_center = np.random.normal(0, stand_dev, (N_regions, 2))
    #print((city_range-1) * grid_start_points)
    
    # next, generate the population in each region, obey the power law distribution
    #b_ = np.random.uniform(1,3)
    r = pareto.rvs(b=2, loc=0, scale=100, size=N_regions)
    request_distribution = (r/sum(r))*population
    #print(request_distribution)
    # finally, generate locations of requests, normal distribution inside each region
    locations_list = []
    for i in range(N_regions):
        num = int(round(request_distribution[i], 0))
        #print(num)
        x_array = np.random.normal(region_center[i][0], region_range, num)
        y_array = np.random.normal(region_center[i][1], region_range, num)
        #print(x_array, y_array)
        for j in range(np.shape(x_array)[0]):
            locations_list.append([x_array[j], y_array[j]])
    
    #print(len(locations_list))
  
    return locations_list

def power_law_2(seed=20230507, population = 500, N_regions = 10, city_range = 6, region_range = 1.0, stand_dev = 3.0):
    np.random.seed(seed)
    
    # first, generate N regions randomly
    # assume a region is a square grid with the length=1km
    #region_center = city_range * np.random.rand(N_regions, 2)
    region_center = np.random.normal(0, stand_dev, (N_regions, 2))
    #print((city_range-1) * grid_start_points)
    
    # next, generate the population in each region, 
    # the rule: 80% population in 20% regions
    N_regions_density = int(round(N_regions * 0.2, 0))
    N_regions_sparse = N_regions - N_regions_density
    r1 = np.random.rand(N_regions_density, 1)
    r2 = np.random.rand(N_regions_sparse, 1)
    request_distribution_1 = (r1/sum(r1)) * population * 0.8 
    request_distribution_2 = (r2/sum(r2)) * population * 0.2 
    request_distribution = np.vstack((request_distribution_1, request_distribution_2))
    print(request_distribution, sum(request_distribution))
    # finally, generate locations of requests, normal distribution inside each region
    locations_list = []
    for i in range(N_regions):
        num = int(round(request_distribution[i][0], 0))
        #print(num)
        x_array = np.random.normal(region_center[i][0], region_range, num)
        y_array = np.random.normal(region_center[i][1], region_range, num)
        #print(x_array, y_array)
        for j in range(np.shape(x_array)[0]):
            locations_list.append([x_array[j], y_array[j]])
    
    #print(len(locations_list))
  
    return locations_list




if __name__ == "__main__": 
    # visulize the spatial distribution of requests
    # normal distribution
    #locations = normal()
    # power-law distribution population
  
    locations = power_law(seed=1200)
    plt.figure(1)
    plt.scatter(-1, 1, c="red", marker='^', s=50)
    for l in locations:
        x, y = l[0], l[1]
        plt.scatter(x, y, c="black", s=5)
    plt.xticks([])
    plt.yticks([])
    plt.savefig('customer_spatial_normal.png', dpi=300, bbox_inches='tight', pad_inches=0.0)
    plt.show()





