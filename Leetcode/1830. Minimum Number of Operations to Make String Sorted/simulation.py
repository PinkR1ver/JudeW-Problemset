class Solution:
    def makeStringSorted(self, s: str) -> int:

        s = list(s)
        count = 0

        while(True):
            
            swap_index1 = None
            swap_index2 = None

            for i in range(1, len(s)):
                if s[i] < s[i-1]:
                    swap_index1 = i

            if swap_index1 == None:
                break 
        
            for j in range(swap_index1, len(s)):
                flag = 0
                for k in range(swap_index1, j + 1):
                    if s[k] >= s[swap_index1 - 1]:
                        flag = 1
                        break
                    
                if flag == 0:
                    swap_index2 = j

            s[swap_index1 - 1], s[swap_index2] = self.swap_variables(s[swap_index1 - 1], s[swap_index2])
            s = self.reverse_suffix(s, swap_index1)
            count += 1

        return count % (10**9 + 7)
                
    def swap_variables(self, a, b):
        return b, a
    
    def reverse_suffix(self, s: list, index: int) -> list:
        return s[:index] + s[index:][::-1]

    
if __name__ == '__main__':
    s = Solution()
    print(s.makeStringSorted("cbad"))

