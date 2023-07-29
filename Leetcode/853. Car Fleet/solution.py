import numpy
import random

class Solution:
    def carFleet(self, target: int, position: list[int], speed: list[int]) -> int:
        
        position_sort_index = get_sorted_index_array(position)
        
        fleet = [[]]
        iter = 0
        index = 0
        
        while True:
            while True:
                
                if fleet[iter] == []:
                    data = (position[position_sort_index[index]], speed[position_sort_index[index]])
                    fleet[iter].append(data)
                    index += 1
                    if index >= len(position):
                        break
                    
                
                data = (position[position_sort_index[index]], speed[position_sort_index[index]])
                if data[1] >= fleet[iter][-1][1]:
                    break
                else:
                    fleet[iter].append(data)
                    index += 1
                    if index >= len(position):
                        break
                    
            iter += 1
            fleet.append([])
            
            if index >= len(position):
                fleet.pop()
                break
        
        print(fleet)
        
        return fleet_number(target, fleet)
        
def fleet_number(target, fleet_list):
    
    new_fleet = []
    
    for i in range(len(fleet_list)):
        
        if len(fleet_list[i]) == 1:
            new_fleet.append(fleet_list[i][0])
            continue
        
        fleet = fleet_list[i]
        point = []
        
        time = (target - fleet[-1][0]) / fleet[-1][1]
        pop_list = []
        
        for j in range(len(fleet) - 2, -1, -1):
            
            distance = fleet[j][1] * time + fleet[j][0]
            if distance >= target:
                pop_list.append(j)
            else:
                point.append(fleet[j])
                time = (target - fleet[j][0]) / fleet[j][1]
            
        for iter, k in enumerate(range(len(pop_list)-1, -1, -1)):
            fleet.pop(pop_list[k] - iter)
        
        if point == []:
            new_fleet.append(fleet[0])
            continue
        else:
            for data in point:
                new_fleet.append(data)
            new_fleet.append(fleet[-1])
            
    print(new_fleet)
    
    while True:
        pop_list = []
        flag = 0
        
        for i in range(len(new_fleet)-1):
            if new_fleet[i][1] > new_fleet[i+1][1]:
                time = (target - new_fleet[i+1][0]) / new_fleet[i+1][1]
                distance = new_fleet[i][1] * time + new_fleet[i][0]
                
                if distance >= target:
                    pop_list.append(i)
                    flag = 1
                    
        print(pop_list)
        for i in range(len(pop_list)-1, -1, -1):
            new_fleet.pop(pop_list[i])
            
        print(new_fleet)
            
        if flag == 0:
            break
                
    return len(new_fleet)
        

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
    