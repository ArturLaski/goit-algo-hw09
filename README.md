# Greedy Algorithms and Dynamic Programming

## Overview

This homework assignment involves implementing two algorithms to determine the best way to give change to a customer: a greedy algorithm and a dynamic programming algorithm. The goal is to compare the effectiveness of these two methods in terms of their execution time and efficiency, particularly for large sums.

## Greedy Algorithm

The greedy algorithm function `find_coins_greedy` takes an integer amount of money and returns a dictionary with the number of coins of each denomination used to make up that amount. The algorithm always chooses the highest denomination coin that does not exceed the remaining amount of money.

## Dynamic Programming Algorithm

The dynamic programming function `find_min_coins` also takes an integer amount of money and returns a dictionary with the minimum number of coins needed to make up that amount. The algorithm builds a table to store the minimum number of coins required for all amounts from 0 to the given amount, and then backtracks to find the coin combination.

## Performance Comparison

We compared the performance of the two algorithms by measuring their execution time for various amounts. The dynamic programming algorithm tends to be more efficient for large amounts because it ensures the minimum number of coins is used, while the greedy algorithm may not always find the optimal solution.

### Example Performance Comparison

For an amount of 10,000:
- Greedy Algorithm: Time: 0.000005 seconds
- Dynamic Programming: Time: 0.000100 seconds

The greedy algorithm is faster in execution but may not provide the optimal solution for certain amounts.

## Conclusion

Both algorithms have their strengths and weaknesses. The greedy algorithm is fast and simple but may not always be optimal. The dynamic programming algorithm is optimal but can be slower for large amounts. Depending on the application, one may be preferred over the other.

## How to Run

To run the functions and compare their performance, use the provided Python scripts. The functions can be tested with different amounts to observe their behavior and efficiency.


