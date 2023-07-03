from scipy.special import comb

class Solution:
    def countAnagrams(self, s: str) -> int:
        sum = 1
        
        char_list = s.split(' ')
        for word in char_list:
            sum_tmp = 1

            word_len = len(word)
            letter_counts = {}

            for letter in word:
                if letter in letter_counts:
                    letter_counts[letter] += 1
                else:
                    letter_counts[letter] = 1

            iter = 0
            for letter, count in letter_counts.items():
                sum_tmp *= comb(word_len - iter, count, exact=True)
                iter += count

            sum *= sum_tmp

        return sum
    
if __name__ == '__main__':
    s = Solution()
    string = "b okzojaporykbmq tybq zrztwlolvcyumcsq jjuowpp"
    print(s.countAnagrams(string))