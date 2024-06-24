import time
import matplotlib.pyplot as plt

def pseudo_rand_num_gen(seed, k):
    random_numbers = []
    for _ in range(k):
        squared = seed ** 2
        squared_str = str(squared)
        squared_str = squared_str.zfill(2 * len(str(seed)))
        middle_index = len(squared_str) // 4
        middle_digits = squared_str[middle_index: -middle_index]
        seed = int(middle_digits)
        random_numbers.append(seed)
    
    return random_numbers

if __name__ == '__main__':
    seed = int(time.time())  
    k = int(input("Enter the number of pseudo-random numbers to generate: "))
    rand_nums = pseudo_rand_num_gen(seed, k)
    n = len(str(seed))
    rand_nums = [num / 10**n for num in rand_nums]

    plt.hist(rand_nums, bins=20, color='blue', edgecolor='black')
    plt.xlabel('Random Values')
    plt.ylabel('Frequency')
    plt.title('Histogram of Generated Random Values (After Division by 10^n)')
    plt.grid(True)
    plt.show()
