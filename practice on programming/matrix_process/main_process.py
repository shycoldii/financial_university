from multiprocessing import Process,Pool
def read_matrix():
    global matrix1,matrix2
    with open('matrix1.txt', 'r') as f:
        matrix1 = [list(map(int, row.split())) for row in f.readlines()]
    with open('matrix2.txt', 'r') as f:
        matrix2 = [list(map(int, row.split())) for row in f.readlines()]
    return matrix1,matrix2
def get_indexes(matrix1,matrix2):
    ind = []
    for i in range(len(matrix1)):
        for j in range(len(matrix2[0])):
            ind.append((i, j))
    return ind
def matrix_process(index,matrix1,matrix2,path):
    res = 0
    matrix = matrix2.copy()
    i, j = index
    for k in range(len(matrix1[0])):
        res += matrix1[i][k] * matrix2[k][j]
    matrix[i][j] = res
    with open(path, "a+", encoding='utf-8') as f:
        if i == j == 0:
            f.write(str(res) + " ")
        elif j == 0:
            f.write("\n" + str(res) + " ")
        else:
            f.write(str(res) + " ")
    return matrix
def main():
    try:
        matrix1, matrix2 = read_matrix()
        p = Pool(7)
        print("Число процессов:", len(matrix1)*len(matrix2[0]))
        ind = get_indexes(matrix1,matrix2)
        for index in ind:
            proc = Process(target=matrix_process, args=(index,matrix1,matrix2,"matrix_process.txt"))
            proc.start()
            proc.join()
            p.apply(matrix_process, (index,matrix1,matrix2,"matrix_pool.txt"))
    except ValueError:
        print("Проверьте данные заданной матрицы")
    except Exception:
        print("Произошла ошибка при вычислении")

if __name__ == '__main__':
    main()