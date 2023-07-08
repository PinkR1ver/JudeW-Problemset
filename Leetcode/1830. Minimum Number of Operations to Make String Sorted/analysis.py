class Solution(object):
    def makeStringSorted(self, s: str) -> int:
        """
        :type s: str
        :rtype: int
        """
        ans = 0

        count_dict = {}

        for char in s:
            if char in count_dict:
                count_dict[char][0] += 1
            else:
                count_dict[char] = [1, 0]

        sort_count_dict = dict(sorted(count_dict.items()))

        sum = 0
        for char in sort_count_dict.keys():
            sort_count_dict[char][1] = sum + sort_count_dict[char][0]
            sum += sort_count_dict[char][0]

        dominantor = 1
        
        for char in sort_count_dict.keys():
            dominantor *= self.factorial(sort_count_dict[char][0])

        for i, char in enumerate(s):
            numerator = (sort_count_dict[char][1] - sort_count_dict[char][0]) * self.factorial(len(s) - i - 1)
            ans += numerator // dominantor

            dominantor = dominantor // sort_count_dict[char][0]
            
            sort_count_dict[char][0] -= 1

            if sort_count_dict[char][0] == 0:
                del sort_count_dict[char]
            else:
                dominantor *= self.factorial(sort_count_dict[char][0])

            for char_tmp in sort_count_dict.keys():
                if char_tmp >= char:
                    sort_count_dict[char_tmp][1] -= 1

        return ans % (10**9 + 7)

    def factorial(self, n: int) -> int:
        if n == 0:
            return 1
        else:
            return n * self.factorial(n - 1)

        
if __name__ == '__main__':
    s = Solution()
    print(s.makeStringSorted("aabaa"))