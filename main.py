from tasks.matrix import Matrix

matrix = Matrix([[1, 2, 3], [4, 5, 6], [7, 8, 9]])

if __name__ == '__main__':
    print(matrix.rotate())  # Rotate matrix on 90 degrees
    print(matrix.make_spiral())  # Make spiral from numbers
