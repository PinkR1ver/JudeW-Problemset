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
    
    # Euluer Prime Filter
    def isPrime(self, n: int) -> bool:
        isPrime_arr = np.ones(n + 1, dtype=bool)
        
        Prime_arr = []
        iter = 0

        for i in range(2, int(math.sqrt(n)) + 1):
            if isPrime_arr[i]:
                Prime_arr.append(i)
                iter += 1

            for j in range(n):
                if i * Prime_arr[j] > n:
                    break

                isPrime_arr[i * Prime_arr[j]] = False

                if i % Prime_arr[j] == 0:
                    break

        return isPrime_arr[n]



    
    
if __name__ == '__main__':
    s = Solution()
    for n in range(20):
        print(n)
        print(s.countPrimes(n))
        print('----------------------------------')
        print('')
        print('')