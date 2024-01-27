class Solution:
    def beautifulIndices(self, s: str, a: str, b: str, k: int) -> list[int]:
        
        matches_list_1 = self.kmp_search(s, a)
        matches_list_2 = self.kmp_search(s, b)
        
        matches = []
        
        i, j = 0, 0
        
        while i < len(matches_list_1) and j < len(matches_list_2):
            
            if abs(matches_list_1[i] - matches_list_2[j]) <= k:
                matches.append(matches_list_1[i])
                i += 1
            
            elif matches_list_1[i] - matches_list_2[j] > k:
                j += 1
                
            elif matches_list_1[i] - matches_list_2[j] < -k:
                i += 1
                
        return matches
                
            
            
            
    
    
    def partial_match_table(self, pattern: str) -> list[int]:
        
        table = [0] * len(pattern)
        
        i = 1
        j = 0
        
        while i < len(pattern):
            
            if pattern[i] == pattern[j]:
                table[i] = j + 1
                i += 1
                j += 1
            
            elif j > 0:
                j = 0

            else:
                i += 1
        
        return table
    
    def kmp_search(self, text, pattern):
        
        lps = self.partial_match_table(pattern)
        
        i, j = 0, 0
        matches = []
        
        while i < len(text):
            
            if text[i] == pattern[j]:
                i += 1
                j += 1
                
                if j == len(pattern):
                    matches.append(i - j)
                    j = lps[j - 1]
            
            elif j > 0:
                j = lps[j - 1]
            
            else:
                i += 1
                
        return matches
        
    
    
if __name__ == '__main__':
    
    s = "abcd"
    a = "a"
    b = "a"
    k = 4
    
    method = Solution()
    
    print(method.beautifulIndices(s, a, b, k))