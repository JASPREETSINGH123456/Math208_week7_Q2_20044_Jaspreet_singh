import random
import math

# Generate 50 random numbers from a normal distribution
mu = 10
sigma = 0.5
random_numbers = [random.normalvariate(mu, sigma) for _ in range(50)]

def verify_Chebyshev_ineq(lst, k):
    within_range_count = sum(1 for x in lst if mu - k * sigma < x < mu + k * sigma)
    return within_range_count

# Test Chebyshev's inequality for various values of k
print(" ")
#when k = 1
k = 1
cnt = verify_Chebyshev_ineq(random_numbers, k)
prob_within_range = cnt / len(random_numbers)
prob_chebyshev_ineq = 1 - 1 / (k ** 2)
print(f"When k = {k}, Probability of |X-u| = {prob_within_range:.2f} ; 1-1/(k^2) = {prob_chebyshev_ineq:.2f}")
print(f"When k = {k}, P(|X-u| < {k}*sd) >= 1-1/k^2 is {prob_within_range >= prob_chebyshev_ineq}")

print(" ")
#when k = 2**0.5
k = 2**0.5
cnt = verify_Chebyshev_ineq(random_numbers, k)
prob_within_range = cnt / len(random_numbers)
prob_chebyshev_ineq = 1 - 1 / (k ** 2)
print(f"When k = {k}, Probability of |X-u| = {prob_within_range:.2f} ; 1-1/(k^2) = {prob_chebyshev_ineq:.2f}")
print(f"When k = {k}, P(|X-u| < {k}*sd) >= 1-1/k^2 is {prob_within_range >= prob_chebyshev_ineq}")

print(" ")
#when k = 1.5
k = 1.5
cnt = verify_Chebyshev_ineq(random_numbers, k)
prob_within_range = cnt / len(random_numbers)
prob_chebyshev_ineq = 1 - 1 / (k ** 2)
print(f"When k = {k}, Probability of |X-u| = {prob_within_range:.2f} ; 1-1/(k^2) = {prob_chebyshev_ineq:.2f}")
print(f"When k = {k}, P(|X-u| < {k}*sd) >= 1-1/k^2 is {prob_within_range >= prob_chebyshev_ineq}")

print(" ")
#when k = 2
k = 2
cnt = verify_Chebyshev_ineq(random_numbers, k)
prob_within_range = cnt / len(random_numbers)
prob_chebyshev_ineq = 1 - 1 / (k ** 2)
print(f"When k = {k}, Probability of |X-u| = {prob_within_range:.2f} ; 1-1/(k^2) = {prob_chebyshev_ineq:.2f}")
print(f"When k = {k}, P(|X-u| < {k}*sd) >= 1-1/k^2 is {prob_within_range >= prob_chebyshev_ineq}")

print(" ")
#when k = 3
k = 3
cnt = verify_Chebyshev_ineq(random_numbers, k)
prob_within_range = cnt / len(random_numbers)
prob_chebyshev_ineq = 1 - 1 / (k ** 2)
print(f"When k = {k}, Probability of |X-u| = {prob_within_range:.2f} ; 1-1/(k^2) = {prob_chebyshev_ineq:.2f}")
print(f"When k = {k}, P(|X-u| < {k}*sd) >= 1-1/k^2 is {prob_within_range >= prob_chebyshev_ineq}")

# Repeat the process with random numbers generated from a uniform distribution
uniform_random_numbers = [random.uniform(-20, 20) for _ in range(50)]
print(" ")
#when k = 1
k = 1
cnt = verify_Chebyshev_ineq(uniform_random_numbers, k)
prob_within_range = cnt / len(uniform_random_numbers)
prob_chebyshev_ineq = 1 - 1 / (k ** 2)
print(f"When k = {k}, Probability of |X-u| = {prob_within_range:.2f} ; 1-1/(k^2) = {prob_chebyshev_ineq:.2f}")
print(f"When k = {k}, P(|X-u| < {k}*sd) >= 1-1/k^2 is {prob_within_range >= prob_chebyshev_ineq}")

print(" ")
#when k = 2**0.5
k = 2**0.5
cnt = verify_Chebyshev_ineq(uniform_random_numbers, k)
prob_within_range = cnt / len(uniform_random_numbers)
prob_chebyshev_ineq = 1 - 1 / (k ** 2)
print(f"When k = {k}, Probability of |X-u| = {prob_within_range:.2f} ; 1-1/(k^2) = {prob_chebyshev_ineq:.2f}")
print(f"When k = {k}, P(|X-u| < {k}*sd) >= 1-1/k^2 is {prob_within_range >= prob_chebyshev_ineq}")

print(" ")
#when k = 1.5
k = 1.5
cnt = verify_Chebyshev_ineq(uniform_random_numbers, k)
prob_within_range = cnt / len(uniform_random_numbers)
prob_chebyshev_ineq = 1 - 1 / (k ** 2)
print(f"When k = {k}, Probability of |X-u| = {prob_within_range:.2f} ; 1-1/(k^2) = {prob_chebyshev_ineq:.2f}")
print(f"When k = {k}, P(|X-u| < {k}*sd) >= 1-1/k^2 is {prob_within_range >= prob_chebyshev_ineq}")

print(" ")
#when k = 2
k = 2
cnt = verify_Chebyshev_ineq(uniform_random_numbers, k)
prob_within_range = cnt / len(uniform_random_numbers)
prob_chebyshev_ineq = 1 - 1 / (k ** 2)
print(f"When k = {k}, Probability of |X-u| = {prob_within_range:.2f} ; 1-1/(k^2) = {prob_chebyshev_ineq:.2f}")
print(f"When k = {k}, P(|X-u| < {k}*sd) >= 1-1/k^2 is {prob_within_range >= prob_chebyshev_ineq}")

print(" ")
#when k = 3
k = 3
cnt = verify_Chebyshev_ineq(uniform_random_numbers, k)
prob_within_range = cnt / len(uniform_random_numbers)
prob_chebyshev_ineq = 1 - 1 / (k ** 2)
print(f"When k = {k}, Probability of |X-u| = {prob_within_range:.2f} ; 1-1/(k^2) = {prob_chebyshev_ineq:.2f}")
print(f"When k = {k}, P(|X-u| < {k}*sd) >= 1-1/k^2 is {prob_within_range >= prob_chebyshev_ineq}")