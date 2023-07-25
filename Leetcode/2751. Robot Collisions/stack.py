import random

class Solution:
    def survivedRobotsHealths(self, positions: list[int], healths: list[int], directions: str) -> list[int]:
        

        position_sort_index = get_sorted_index_array(positions)

        health_stack = []
        movement_stack = []
        index_stack = []
        for index in position_sort_index:

            health_stack.append(healths[index])
            movement_stack.append(directions[index])
            index_stack.append(index)

            while True:
                if len(movement_stack) >= 2:
                    if movement_stack[-1] == 'L' and movement_stack[-2] == 'R':
                        if health_stack[-1] > health_stack[-2]:
                            health_stack.pop(-2)
                            movement_stack.pop(-2)
                            index_stack.pop(-2)
                            health_stack[-1] -= 1

                            if health_stack[-1] == 0:
                                health_stack.pop(-1)
                                movement_stack.pop(-1)
                                index_stack.pop(-1)

                        elif health_stack [-1] < health_stack[-2]:
                            health_stack.pop(-1)
                            movement_stack.pop(-1)
                            index_stack.pop(-1)
                            health_stack[-1] -= 1

                            if health_stack[-1] == 0:
                                health_stack.pop(-1)
                                movement_stack.pop(-1)
                                index_stack.pop(-1)

                        elif health_stack[-1] == health_stack[-2]:
                            
                            health_stack.pop(-1)
                            movement_stack.pop(-1)
                            index_stack.pop(-1)
                            health_stack.pop(-1)
                            movement_stack.pop(-1)
                            index_stack.pop(-1)

                    else:
                        break
                else:
                    break

        index_stack_index = get_sorted_index_array(index_stack)
        
        ans = [None] * len(health_stack)
        for iter, index in enumerate(index_stack_index):
            ans[iter] = health_stack[index]

        return ans
    
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

    positions = [3,5,2,6]
    healths = [10,10,15,12]
    directions = "RLRL"

    s = Solution()
    print(s.survivedRobotsHealths(positions, healths, directions))