import numpy as np

def worker(iterations):
    """
    Generate desired number of random 2-tuples drawn uniformly from (0,1)^2
    Take L2 norm (distance from origin) of each tuple
    Use Boolean mask to count number of points within unit circle
    """
    simulations = np.linalg.norm(np.random.rand(iterations,2), axis = 1) 
    return np.count_nonzero(simulations < 1)