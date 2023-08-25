#include <iostream>
#include <vector>

using namespace std;

class Solution {
public:
    long long matrixSumQueries(int n, vector<vector<int>>& queries) {
        vector<int> row(n, -1);
        vector<int> col(n, -1);
        int row_count = 0;
        int col_count = 0;
        long long ans = 0;

        for (int i = queries.size() - 1; i >= 0; i--) {
            if (row_count == n && col_count == n) {
                break;
            }

            if (queries[i][0] == 0) {
                if (row[queries[i][1]] == -1) {
                    row[queries[i][1]] = queries[i][2];
                    ans += queries[i][2] * (n - row_count);
                    col_count += 1;
                }
            }

            if (queries[i][0] == 1) {
                if (col[queries[i][1]] == -1) {
                    col[queries[i][1]] = queries[i][2];
                    ans += queries[i][2] * (n - col_count);
                    row_count += 1;
                }
            }
        }

        return ans;
    }
};

int main() {
    int n = 2;
    vector<vector<int>> queries = {{1,1,1},{1,0,7},{0,0,0}};
    cout << Solution().matrixSumQueries(n, queries) << std::endl;
    cin.get();
    return 0;
}
