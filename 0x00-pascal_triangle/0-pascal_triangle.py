def pascal_triangle(n):
    if n <= 0:
        return []
    if n == 1:
        return [[1]]

    pascal = [[1], [1, 1]]

    for i in range(1, n - 1):
        new_row = [1]
        row_before = pascal[i]

        for j in range(i):
            new_row.append(row_before[j] + row_before[j + 1])
        new_row.append(1)
        pascal.append(new_row)

    return pascal
