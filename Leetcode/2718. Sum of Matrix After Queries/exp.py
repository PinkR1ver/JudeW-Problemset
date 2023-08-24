# your list of lists
lst = [[1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12]]

# calculate sum of column 2
sum_col_2 = sum(row[1] for row in lst)

print(sum_col_2) # output should be 2+5+8+11=26