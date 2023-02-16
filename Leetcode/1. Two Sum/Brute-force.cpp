/*
Two Loop to do Brute-force search
*/

#include <iostream>
#include <vector>

using namespace std;

class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target)
    {
        for (int i = 0; i < nums.size(); i++) {
            for (int j = i + 1; j < nums.size(); j++) {
                if (nums.at(i) + nums.at(j) == target) {
                    vector<int> res{i, j};
                    return res;
                }
            }
        }
        vector<int> res{0, 1};
        return res;
    }
};

int main()
{
    vector<int> nums {2,7,11,15};
    int target = 9;
    Solution Res;
    vector<int> res;
    res = Res.twoSum(nums, target);
    for(int i = 0; i < res.size(); i++){
        cout << res.at(i) << ' ';
    }
    return 0;
}