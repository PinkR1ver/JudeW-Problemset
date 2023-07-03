import math
import numpy as np

class Solution:
    def countPrimes(self, n: int) -> int:
        if n <= 2:
            return 0
        
        isPrime_arr = np.ones(n, dtype=bool)

        isPrime_arr[0] = False
        isPrime_arr[1] = False
        
        Prime_arr = []
        iter = 0

        for i in range(2, n):
            
            if isPrime_arr[i]:
                Prime_arr.append(i)
                iter += 1

            for j in range(iter):
                if i * Prime_arr[j] > n - 1:
                    break
                
                isPrime_arr[i * Prime_arr[j]] = False

                if i % Prime_arr[j] == 0:
                    break

                

        return sum(isPrime_arr)




    
    
if __name__ == '__main__':
    s = Solution()
    for n in range(11):
        print(n)
        print(s.countPrimes(n))
        print('----------------------------------')
        print('')
        print('')