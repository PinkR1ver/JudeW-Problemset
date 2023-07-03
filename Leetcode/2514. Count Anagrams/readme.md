# Method

计算每个单词的anagrams后相乘，考虑相同字母的情况
每次放同一个字母，可能性是：
$$
C_{\text{Blank Position}}^{\text{char counts}}
$$
然后剩余空位减去这个字母数量，考虑下个字母的可能性，将所有字母的可能性相乘，就是这个单词anagrams的所有可能性


## 因此引出第二个知识点，除法取模(求逆元)

TODO...