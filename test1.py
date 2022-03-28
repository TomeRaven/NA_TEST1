

def printr(rat,a1,a2):
    res=[[1,0,0],[0,1,0],[0,0,1]]

    n=len(res)

    for i in range(n):
        for j in range(n):
            if i==a1 and j==a2:
                res[i][j]=rat

    return res


def gauss(a,b):
    n=len(a)
    for i in range(n):

        for j in range(i + 1, n):
            ratio = a[j][i] / a[i][i]

            print(printr(ratio,i,j),end = " * ")
            print(a,end=" = ")

            for k in range(n):
                a[j][k] = a[j][k] - ratio * a[i][k]

            print(a)
            b[j]=b[j]-ratio*b[i]


    x=[[0,0,0],[0,0,0],[0,0,0]]

    x[n - 1] = b[n - 1] / a[n - 1][n - 1]

    for i in range(n - 2, -1, -1):
        x[i] = b[i]

        for j in range(i + 1, n):

            x[i] = x[i] - a[i][j] * x[j]

        x[i] = x[i] / a[i][i]



    return x


X=[[1,1/2,1/3],[1/2,1/3,1/4],[1/3,1/4,1/5]]
b=[1,0,0]

res = gauss(X,b)
print("")
print("final result is: ",res)

