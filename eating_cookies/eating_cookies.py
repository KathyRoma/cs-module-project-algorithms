'''
Input: an integer
Returns: an integer
'''
def eating_cookies(n):
    # Your code here
    if n==0:
        return 1

    elif n<0:
        return 0    
    else:
        return eating_cookies(n-1) + eating_cookies(n-2) + eating_cookies(n-3)   

# from functools import lru_cache

# @lru_cache()
# def eating_cookies(n):
#     # Your code here
#     if n==0:
#         return 1

#     elif n<0:
#         return 0    
#     else:
#         return eating_cookies(n-1) + eating_cookies(n-2) + eating_cookies(n-3)

# Improved solution

def eating_cookies(n, cache=None):
    # what are our base cases?     
    if n < 0:
        return 0 
    # this represents there being a number of cookies where we can just take
    # that many cookies
    elif n == 0:
        return 1 
    # check the cache to see if the answer is stored in there 
    elif cache and cache[n] > 0:
        return cache[n]
    else:
        if not cache:
            # init an empty cache
            cache = {i: 0 for i in range(n+1)}
        # store answers in our cache 
        cache[n] = eating_cookies(n - 1, cache) + eating_cookies(n - 2, cache) + eating_cookies(n - 3, cache)
    return cache[n]        
​
print(eating_cookies(100))


if __name__ == "__main__":
    # Use the main function here to test out your implementation
    num_cookies = 5

    print(f"There are {eating_cookies(num_cookies)} ways for Cookie Monster to each {num_cookies} cookies")
