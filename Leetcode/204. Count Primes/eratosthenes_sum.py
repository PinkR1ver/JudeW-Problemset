import math
import numpy as np

class Solution:
    def countPrimes(self, n: int) -> int:
        if n <= 2:
            return 0
        
        isPrime_arr = np.ones(n, dtype=bool)

        isPrime_arr[0] = False
        isPrime_arr[1] = False

        for i in range(2, int(math.sqrt(n)) + 1):
            if isPrime_arr[i]:
                isPrime_arr[i*i::i] = False

        return sum(isPrime_arr)

    
if __name__ == '__main__':
    s = Solution()
    for n in range(20):
        print(n)
        print(s.countPrimes(n))
        print('----------------------------------')
        print('')
        print('')