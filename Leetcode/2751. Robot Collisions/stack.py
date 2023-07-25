class Solution:
    def survivedRobotsHealths(self, positions: list[int], healths: list[int], directions: str) -> list[int]:
        
        positions_sort = positions.copy()
        positions_sort.sort()

        position_sort_index = [None] * len(positions)
        for index, element in enumerate(positions_sort):
            position_sort_index[index] = positions.index(element)


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

        index_stack_sort = index_stack.copy()
        index_stack_sort.sort()

        index_stack_index = [None] * len(index_stack)
        for index, element in enumerate(index_stack_sort):
            index_stack_index[index] = index_stack.index(element)
        
        ans = [None] * len(health_stack)
        for iter, index in enumerate(index_stack_index):
            ans[iter] = health_stack[index]

        return ans

if __name__ == '__main__':

    positions = [1,2,3,4]
    healths = [1,1,1,4]
    directions = "RRRL"

    s = Solution()
    print(s.survivedRobotsHealths(positions, healths, directions))