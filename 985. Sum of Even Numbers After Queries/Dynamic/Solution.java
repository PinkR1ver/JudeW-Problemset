package Dynamic;

import java.util.List;
import java.util.ArrayList;

class Solution {
    public int[] sumEvenAfterQueries(int[] nums, int[][] queries) {
        List<Integer> arr = new ArrayList<>();
        int sum = 0;
        for (int num : nums) {
            if (evenOrNot(num)) {
                sum += num;
            }
        }

        for (int i = 0; i< queries.length; i++) {
            if (evenOrNot(nums[queries[i][1]])) {
                if (evenOrNot(nums[queries[i][1]] + queries[i][0])) {
                    sum += queries[i][0];
                    nums[queries[i][1]] += queries[i][0];
                }
                else {
                    sum -= nums[queries[i][1]];
                    nums[queries[i][1]] += queries[i][0];
                }
            }
            else {
                if (evenOrNot(nums[queries[i][1]] + queries[i][0])) {
                    nums[queries[i][1]] += queries[i][0];
                    sum += nums[queries[i][1]];
                }
                else {
                    nums[queries[i][1]] += queries[i][0];
                }
            }

            arr.add(sum);
        }

        int[] res = new int[arr.size()];
        for (int i = 0; i < arr.size(); i++) {
            res[i] = arr.get(i);
        }

        return res;

    }

    public boolean evenOrNot(int num) {
        if (num % 2 == 0) {
            return true;
        }
        else {
            return false;
        }
    }
}