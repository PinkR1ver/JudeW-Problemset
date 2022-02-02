/*
Using Qsort then search
*/

#include <algorithm>
#include <iostream>
#include <vector>

using namespace std;

class Solution {
private:
    vector<int> qsort(vector<int>& nums)
    {
        vector<int> tmp = nums;
        sort(tmp.begin(), tmp.end());
        return tmp;
    }
public:
    vector<int> twoSum(vector<int>& nums, int target)
    {
        vector<int> tmp = qsort(nums);
        for (int i = 0, j = tmp.size() - 1;;) {
            if (tmp.at(i) + tmp.at(j) > target) {
                j--;
            }
            if (tmp.at(i) + tmp.at(j) < target) {
                i++;
            }
            if (tmp.at(i) + tmp.at(j) == target) {
                vector<int> res;
                bool flag1 = true;
                bool flag2 = true;
                for (int k = 0; k < nums.size(); k++) {
                    if (nums.at(k) == tmp.at(i) && flag1 == true) {
                       res.push_back(k);
                       flag1 = false;
                   } 
                    else if (nums.at(k) == tmp.at(j) && flag2 == true) {
                       res.push_back(k);
                       flag2 = false;
                   } 
                    if (flag1 == false && flag2 == false) {
                        return res;
                    } 
                } 
            }
        }
    }
};

int main()
{
    vector<int> nums {3,3};
    int target = 6;
    Solution Res;
    vector<int> res;
    res = Res.twoSum(nums, target);
    for (int i = 0; i < res.size(); i++) {
        cout << res.at(i) << ' ';
    }
    return 0;
}