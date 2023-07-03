class Solution:
    def minimumLines(self, stockPrices: list[list[int]]) -> int:

        if len(stockPrices) <= 1:
            return 0

        count = 0

        stockPrices.sort(key=lambda x: x[0])

        for i in range(1, len(stockPrices) - 1):
            if (stockPrices[i + 1][1] - stockPrices[i][1]) * (stockPrices[i][0] - stockPrices[i - 1][0]) != (stockPrices[i][1] - stockPrices[i - 1][1]) * (stockPrices[i + 1][0] - stockPrices[i][0]):
                count += 1

        return count + 1 
    
if __name__ == '__main__':
    s = Solution()
    stockPrices = [[1,1],[500000000,499999999],[1000000000,999999998]]
    print(s.minimumLines(stockPrices))

