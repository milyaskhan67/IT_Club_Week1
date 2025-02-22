import numpy as np

def initialize(name):
    rows = int(input("Enter Number Of Rows: "))
    cols = int(input("Enter Number Of Columns: "))
    print(f"Enter the elements for the {rows}x{cols} matrix {name}:")
    
    matrix = []
    for i in range(rows):
        row = []
        for j in range(cols):
            row.append(int(input(f"Element [{i+1}][{j+1}]: ")))
        matrix.append(row)
    return np.array(matrix)

def main():

    print("\nSelect an operation:")
    print("1) Addition")
    print("2) Subtraction")
    print("3) Multiplication (dot product)")
    op = input("Enter your choice (1/2/3): ")

    
    if op == '1':
        print("Input 1st Matrix:")
        A = initialize('A')
        print("\nInput 2nd Matrix:")
        B = initialize('B')
        print("\nMatrix A:")
        print(A)
        print("\nMatrix B:")
        print(B)
        if A.shape == B.shape:
            print("\nA + B =")
            print(A + B)
        else:
            print("\nAddition is not possible (matrices must have the same dimensions).")
    elif op == '2':
        print("Input 1st Matrix:")
        A = initialize('A')
        print("\nInput 2nd Matrix:")
        B = initialize('B')
        print("\nMatrix A:")
        print(A)
        print("\nMatrix B:")
        print(B)    
        if A.shape == B.shape:
            print("\nA - B =")
            print(A - B)
        else:
            print("\nSubtraction is not possible (matrices must have the same dimensions).")
    elif op == '3':
        print("Input 1st Matrix:")
        A = initialize('A')
        print("\nInput 2nd Matrix:")
        B = initialize('B')
        print("\nMatrix A:")
        print(A)
        print("\nMatrix B:")
        print(B)
        if A.shape[1] == B.shape[0]:
            product = np.dot(A, B)
            print("\nA * B (dot product) =")
            print(product)
        else:
            print("\nMultiplication is not possible (number of columns in A must equal number of rows in B).")
    else:
        print("\nInvalid operation selected.")

main()
