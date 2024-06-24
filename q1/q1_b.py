import random
import time
from q1_a import pseudo_rand_num_gen  

def estimate_pi_pseudo_module(k):
    points_inside_circle = 0
    total_points = 0
    pi_errors = []
    
    for _ in range(k):
        seed = int(time.time())
        x = (((pseudo_rand_num_gen(seed, 1))[0]/10000) * 2) - 1 
        seed = int(time.time())
        y = ((pseudo_rand_num_gen(seed, 1)[0]/10000) * 2) - 1  
        
        if x**2 + y**2 <= 1:
            points_inside_circle += 1
        
        total_points += 1
        pi_estimate = 4 * points_inside_circle / total_points
        pi_error = abs(pi_estimate - 3.14159)
        pi_errors.append(pi_error)
    
    return pi_errors

def estimate_pi_random_module(k):
    points_inside_circle = 0
    total_points = 0
    pi_errors = []
    
    for _ in range(k):
        x = 2 * random.random() - 1  
        y = 2 * random.random() - 1  
        
        if x**2 + y**2 <= 1:
            points_inside_circle += 1
        
        total_points += 1
        pi_estimate = 4 * points_inside_circle / total_points
        pi_error = abs(pi_estimate - 3.14159)
        pi_errors.append(pi_error)
    
    return pi_errors

k = int(input("Enter the number of random points to generate: "))
pi_errors_pseudo = estimate_pi_pseudo_module(k)
pi_errors_random = estimate_pi_random_module(k)
    

