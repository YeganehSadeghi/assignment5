def haha():
    n = int(input("Enter n : "))
    m = int(input("Enter m : "))
    mat = []
    for i in range(n):
        mat.append([])
        for j in range(m):
            if i % 2 == 0:
                if j % 2 == 0:
                    mat[i].append("#")
                else:
                    mat[i].append("*")
            else:
                if j % 2 == 0:
                    mat[i].append("*")
                else:
                    mat[i].append("#")
    for i in range(n):
        for j in range(m):
            print(mat[i][j],end = '')
        print()
haha()