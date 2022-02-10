#include <iostream>
#include <vector>

using namespace std;

class Solution {
private:
    double findMedian(vector<int>& nums) 
    {
        if(nums.size() % 2 == 1) {
            return (double)(nums.at(nums.size() / 2));
        }
        else {
            return ((double)(nums.at(nums.size() / 2)) + (double)(nums.at(nums.size() / 2 - 1))) / 2;
        }
    }
public:
    double findMedianSortedArrays(vector<int>& nums1, vector<int>& nums2)
    {
        vector<int> res;
        for (int i = 0, j = 0; i < nums1.size() || j < nums2.size();) {
            if (i == nums1.size()) {
                for (int k = j;k < nums2.size(); k++) {
                    res.push_back(nums2.at(k));
                }
                return findMedian(res);
            }
            else if (j == nums2.size()) {
                for (int k = i;k < nums1.size(); k++) {
                    res.push_back(nums1.at(k));
                }
                return findMedian(res);
            }
            if (nums1.at(i) < nums2.at(j)) {
                res.push_back(nums1.at(i));
                i++;
            }
            else {
                res.push_back(nums2.at(j));
                j++;
            }
        }
        return findMedian(res);
    }
};

int main()
{
    vector<int> nums1{1, 3};
    vector<int> nums2{2};
    Solution s;
    cout << s.findMedianSortedArrays(nums1, nums2) << endl;
    return 0;
}