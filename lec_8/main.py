class CustomMatrix:
    def __init__(self, rows, cols):
        self.rows = rows
        self.cols = cols
        self.data = [[0] * cols for _ in range(rows)]

    def display(self):
        for row in self.data:
            print(row)

    def calculate_mean(self):
        total = sum(sum(row) for row in self.data)
        return total / (self.rows * self.cols)

    def calculate_row_sum(self, row_idx):
        if 0 <= row_idx < self.rows:
            return sum(self.data[row_idx])
        else:
            return None

    def calculate_column_average(self, col_idx):
        if 0 <= col_idx < self.cols:
            total = sum(row[col_idx] for row in self.data)
            return total / self.rows
        else:
            return None

    def display_submatrix(self, indices):
        col_start, col_end, row_start, row_end = indices
        if 0 <= col_start < col_end <= self.cols and 0 <= row_start < row_end <= self.rows:
            submatrix = [row[col_start:col_end] for row in self.data[row_start:row_end]]
            for row in submatrix:
                print(row)
        else:
            print("Invalid submatrix indices.")

rows = 4
cols = 3
matrix = CustomMatrix(rows, cols)

matrix.data = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9],
    [10, 11, 12]
]

print("Custom Matrix:")
matrix.display()

mean = matrix.calculate_mean()
print(f"Mean of the matrix: {mean}")

row_sum = matrix.calculate_row_sum(2)  
if row_sum is not None:
    print(f"Sum of row 2: {row_sum}")
else:
    print("Invalid row index.")

col_average = matrix.calculate_column_average(1)  
if col_average is not None:
    print(f"Average of column 1: {col_average}")
else:
    print("Invalid column index.")

print("Custom Submatrix:")
matrix.display_submatrix([1, 3, 0, 2])
