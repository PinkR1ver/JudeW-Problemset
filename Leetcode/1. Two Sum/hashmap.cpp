/*
hash table
*/

#include <algorithm>
#include <iostream>
#include <vector>
#include <map>
#include <unordered_map>

using namespace std;

class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target)
    {
        unordered_map<int, int> m;
        for (int i = 0; i < nums.size(); i++) {
            m[nums.at(i)] = i;
        }

        for (int i = 0; i < nums.size(); i++) {
            int complement = target - nums.at(i);
            if (m.count(complement) && m.find(complement)->second != i) {
                return vector<int> {i, m.find(complement)->second};
            }
        }
        return vector<int> {};
    }
};

int main()
{
    vector<int> nums {3, 2, 4};
    int target = 6;
    Solution Res;
    vector<int> res;
    res = Res.twoSum(nums, target);
    for (int i = 0; i < res.size(); i++) {
        cout << res.at(i) << ' ';
    }
    return 0;
}