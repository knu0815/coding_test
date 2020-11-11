from typing import List
import sys

# URL:
# https://leetcode.com/problems/best-time-to-buy-and-sell-stock/

# Question:
# Say you have an array for which the ith element is the price of a given stock on day i.

# If you were only permitted to complete at most one transaction
# (i.e., buy one and sell one share of the stock),
# design an algorithm to find the maximum profit.

# Note that you cannot sell a stock before you buy one.

# Runtime: 60 ms
# Memory: 15 MB
class BestTimeToBuyAndSellStock:
    @classmethod
    def my_solution(cls, prices: List[int]) -> int:
        max_profit = 0
        buy = sys.maxsize

        for price in prices:
            buy = min(price, buy)
            profit = price - buy
            max_profit = max(max_profit, profit)

        return max_profit


def main():
    # Answer for number #1
    print(BestTimeToBuyAndSellStock.my_solution([7, 1, 5, 3, 6, 4]))
    print(BestTimeToBuyAndSellStock.my_solution([7, 6, 4, 3, 1]))


if __name__ == "__main__":
    main()