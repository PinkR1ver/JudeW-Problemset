#include <iostream>
#include <string>
#include <cstdio>

using namespace std;

class Solution {
public:
    int lengthOfLongestSubstring(string s) {
        string tmp("");
        int res = 0;
        int tmp_res = 0;
        for(string::iterator i = s.begin();i != s.end(); i++) {
            tmp += string{*i};
            if (ifNotRepeat(tmp)) {
                tmp_res += 1;
            }
            else {
                tmp.erase(0, 1);
                res = max(res, tmp_res);
            }
        }
        res = max(res, tmp_res);
        return res;
    }

private:
    bool ifNotRepeat(string s) {
        for(string::iterator i = s.begin();i != s.end(); i++) {
            for (string::iterator j = i + 1;j != s.end(); j++) {
                if (*i == *j) {
                    return false;
                }
            }
        }
        return true;
    }
};

int main()
{
    string x = " ";
    Solution a;
    cout << a.lengthOfLongestSubstring(x) << endl;
    return 0;
}