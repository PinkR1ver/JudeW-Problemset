def build_segment_tree(arr):
    n = len(arr)
    tree = [0] * (2 * n)  # Create a tree with double the size of the array

    # Fill the leaf nodes with array values
    for i in range(n):
        tree[n + i] = arr[i]

    # Build the tree by calculating parent nodes from leaf nodes
    for i in range(n - 1, 0, -1):
        tree[i] = tree[2 * i] + tree[2 * i + 1]

    return tree


# Example usage
arr = [1, 3, 5, 7, 9, 11]
segment_tree = build_segment_tree(arr)
print(segment_tree)