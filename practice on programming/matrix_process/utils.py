class Matrix_util:

    @staticmethod
    def read_matrix():
        global matrix1,matrix2
        with open('matrix1.txt', 'r') as f:
            matrix1 = [list(map(int, row.split())) for row in f.readlines()]
        with open('matrix2.txt', 'r') as f:
            matrix2 = [list(map(int, row.split())) for row in f.readlines()]
        return matrix1,matrix2
    @staticmethod
    def get_indexes(matrix1, matrix2):
        ind = []
        for i in range(len(matrix1)):
            for j in range(len(matrix2[0])):
                ind.append((i, j))
        return ind
