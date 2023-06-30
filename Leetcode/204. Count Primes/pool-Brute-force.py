import math
from multiprocessing import Pool


class Solution:
    def countPrimes(self, n: int) -> int:
        if n <= 2:
            return 0
        
        if n==3:
            return 1

        # 创建进程池
        pool = Pool()

        # 将范围拆分成多个子范围
        chunk_size = n // pool._processes  # 根据进程数确定每个进程的处理范围
        ranges = [(i, min(i + chunk_size, n)) for i in range(2, n, chunk_size)]

        # 使用并行计算来判断每个子范围内的数字是否为素数
        results = pool.map(self.isPrime, ranges)

        # 统计素数的数量
        count = sum(results)

        # 关闭进程池
        pool.close()
        pool.join()

        return count
    
    def isPrime(self, range_tuple):
        start, end = range_tuple
        primes = []
        for n in range(start, end):
            if n < 2:
                continue
            for i in range(2, int(math.sqrt(n)) + 1):
                if n % i == 0:
                    break
            else:
                primes.append(n)
        return len(primes)
    
if __name__ == '__main__':
    n = 5000000
    s = Solution()
    print(s.countPrimes(n))