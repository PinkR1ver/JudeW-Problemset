class Solution:
    def shortestBeautifulSubstring(self, s: str, k: int) -> str:
        
        min_len = float('inf')
        min_str = ""
        
        
        while len(s) >= k:
            for i in range(len(s) + 1):
                if i > min_len:
                    break
                
                if s[:i].count('1') == k:
                    slide_window_len = i
                    if slide_window_len < min_len:
                        min_len = slide_window_len
                        min_str = s[:i]
 
                        for i in range(1, len(s) - slide_window_len + 1):
                            if s[i:i + slide_window_len].count('1') == k:
                                if s[i:i + slide_window_len] < min_str:
                                    min_str = s[i:i + slide_window_len]
                                    
                        break
                    
                    elif slide_window_len == min_len:
                        
                        for i in range(len(s) - slide_window_len + 1):
                            if s[i:i + slide_window_len].count('1') == k:
                                if s[i:i + slide_window_len] < min_str:
                                    min_str = s[i:i + slide_window_len]
                                    
                        break
                        
                                
            s = s[1:]
                            
        return min_str
    

if __name__ == '__main__':
        
        s = Solution()
        string = "0111111100011111101"
        k = 12
        
        print(s.shortestBeautifulSubstring(string, k))