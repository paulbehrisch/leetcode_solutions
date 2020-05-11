from typing import List
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        stock = []
        profit = 0
        for i, current_price in enumerate(prices):
            # check if current index is not the last element of list
            if(i < len(prices) -1):
                #print(f"{i} = {j}"
                next_price = prices[i+1]
                if next_price < current_price:
                    if(len(stock) > 0):
                        value_of_stock = stock.pop()
                        #print(f"sold at: {current_price} -> bought at:{value_of_stock}")
                        profit +=  current_price - value_of_stock
                elif next_price > current_price:
                    if(len(stock) == 0):
                        stock.append(current_price)
                        #print(f"bought at {current_price}")

            else:
                #no element left
                if(len(stock) > 0):
                    value_of_stock = stock.pop()
                    #print(f"sold at: {current_price} -> bought at:{value_of_stock}")
                    profit +=  current_price - value_of_stock

        return profit

x = Solution()
print(x.maxProfit([7,1,5,3,6,4]))
print(x.maxProfit([1,2,3,4,5]))
print(x.maxProfit([7,6,4,3,1]))

