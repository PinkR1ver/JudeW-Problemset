import numpy
import random

class Solution:
    def carFleet(self, target: int, position: list[int], speed: list[int]) -> int:
        
        position_sort_index = get_sorted_index_array(position)
        
        fleet = []
        
        
        for index in position_sort_index:
            data = (position[index], speed[index])
            fleet.append(data)
            
        print(fleet)
        
        while True:
            pop_list = []
            flag = 0
            
            for i in range(len(fleet)-1):
                if fleet[i][1] > fleet[i+1][1]:
                    time = (target - fleet[i+1][0]) / fleet[i+1][1]
                    distance = fleet[i][1] * time + fleet[i][0]
                    
                    if distance >= target:
                        pop_list.append(i)
                        flag = 1
 
            for i in range(len(pop_list)-1, -1, -1):
                fleet.pop(pop_list[i])
                
            print(fleet)
                
            if flag == 0:
                break
            
        return len(fleet)
        
        

def partition(arr, low, high):
    random_pivot_index = random.randint(low, high)  # 随机选择pivot的索引
    arr[high], arr[random_pivot_index] = arr[random_pivot_index], arr[high]
    
    i = low - 1
    pivot = arr[high]

    for j in range(low, high):
        if arr[j] <= pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]

    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    return i + 1

def quicksort(arr, low, high):
    if low < high:
        pi = partition(arr, low, high)
        quicksort(arr, low, pi - 1)
        quicksort(arr, pi + 1, high)

def get_sorted_index_array(arr):
    n = len(arr)
    index_array = list(range(n))

    def custom_partition(low, high):
        random_pivot_index = random.randint(low, high)  # 随机选择pivot的索引
        index_array[high], index_array[random_pivot_index] = index_array[random_pivot_index], index_array[high]
        
        i = low - 1
        pivot = arr[index_array[high]]

        for j in range(low, high):
            if arr[index_array[j]] <= pivot:
                i += 1
                index_array[i], index_array[j] = index_array[j], index_array[i]

        index_array[i + 1], index_array[high] = index_array[high], index_array[i + 1]
        return i + 1

    def custom_quicksort(low, high):
        if low < high:
            pi = custom_partition(low, high)
            custom_quicksort(low, pi - 1)
            custom_quicksort(pi + 1, high)

    custom_quicksort(0, n - 1)
    return index_array

if __name__ == '__main__':
    target = 12
    position = [4,0,5,3,1,2]
    speed = [6,10,9,6,7,2]
    s  = Solution()
    print(s.carFleet(target, position, speed))
    