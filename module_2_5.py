def get_matrix(n, m, value):
    matrix = []
    for i in range(n):
        line = []
        for j in range(m):
            line.append(value)
        matrix.append(line)
    return matrix

result1 = get_matrix(2, 2, 10)
result2 = get_matrix(3, 5, 42)
result3 = get_matrix(4, 2, 13)
print(result1)
print(result2)
print(result3)

lines = int(input("Сколько строк?"))
columns = int(input("Сколько столбцов?"))
meaning = int(input("Чем заполним?"))

try_to_create = get_matrix(n=lines, m=columns, value=meaning)
print (try_to_create)


