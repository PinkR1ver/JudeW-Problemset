#include <iostream>

using namespace std;

void swap(int *a, int *b) 
{
    int t = *a;
    *a = *b;
    *b = t;
}

int partition(int arr[], int low, int high)
{
    int pivot = arr[high];
    int i = (low - 1);

    for (int j = low; j <= high; j++) {
        if (arr[j] < pivot) {
            i++;
            swap(&arr[i], &arr[j]);
        }
    }
    swap(&arr[i + 1], &arr[high]);
    return (i + 1);
}

void quicksort(int arr[], int low, int high) 
{
    if (low < high){
        int partition_index = partition(arr, low, high);

        quicksort(arr, low, partition_index - 1);
        quicksort(arr, partition_index + 1, high);
    }
}

int main()
{
    int n, q;
    cin >> n >> q;

    int* growth;
    growth = (int*) malloc(sizeof(int) * n);
    for (int i = 0; i < n; i++) {
        cin >> growth[i];
    }

    int* ans;
    ans = (int*) malloc(sizeof(int) * q);

    for (int i = 0; i < q; i++) {
        int l, r;
        cin >> l >> r;
        int length = r - l + 1;
        int* seq;
        seq = (int*) malloc(sizeof(int) * length);
        int index = 0;
        
        for (int j = l - 1; j < r; j++) {
            seq[index] = growth[j];
            index++;
        }

        quicksort(seq, 0, length - 1);
        
        int difference = n;
        for ( int j = 0; j < length - 1; j++) {
            if (seq[j + 1] - seq[j] < difference) {
                difference = seq[j + 1] - seq[j];
            }
        }

        ans[i] = difference;

    }

    for (int i = 0; i < q; i++) {
        cout << ans[i] << endl;
    }
    return 0;
}