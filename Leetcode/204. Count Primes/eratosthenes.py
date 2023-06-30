import math
import numpy as np

class Solution:
    def countPrimes(self, n: int) -> int:
        if n <= 2:
            return 0
        
        count = 0
        for i in range(2, n):
            if self.isPrime(i):
                count += 1
        return count
    
    def isPrime(self, n: int) -> bool:
        isPrime_arr = np.ones(n + 1, dtype=bool)

        for i in range(2, int(math.sqrt(n)) + 1):
            if isPrime_arr[i]:
                isPrime_arr[i*i::i] = False
                
                '''
                这个代码行的含义是将一个布尔数组（或列表）中从索引 i*i 开始，以步长 i 的元素设置为 False。通常，该代码用于生成一个素数筛选器，用于确定在某个范围内的数字是否为素数。

                让我详细解释一下这行代码的含义：

                isPrime_arr：这是一个布尔数组（或列表），用于表示每个数字是否为素数。初始时，所有的元素都被默认设置为 True，表示所有的数字都被假设为素数。
                i：这是当前的迭代变量，用于表示要筛选的数字或筛选步长。
                isPrime_arr[i*i::i]：这是切片操作符，用于从索引 i*i 开始，以步长 i 对数组进行切片。这将选择所有索引为 i*i、i*i+i、i*i+2i、i*i+3i 等的元素。
                False：这是要将选择的元素设置为的值，即将这些索引处的元素标记为非素数。
                这行代码的作用是通过每次迭代将当前素数的倍数标记为非素数。在循环的每个迭代步骤中，它将从当前素数的平方开始，将所有该素数的倍数设置为 False。通过这种方式，最终剩下的 True 值对应于素数。

                这是一个常见的算法，称为埃拉托斯特尼筛法（Sieve of Eratosthenes），用于生成一系列素数。
                '''

        return isPrime_arr[n]
    
if __name__ == '__main__':
    s = Solution()
    for n in range(10):
        print(n)
        print(s.countPrimes(n))
        print('----------------------------------')
        print('')
        print('')