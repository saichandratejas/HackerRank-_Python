# Lambda function to find the cube of function
cube = lambda x: pow(x, 3)


def fibonacci(n):
    # return a list of fibonacci numbers
    lis = [0, 1]

    # for loop starting from 2
    for i in range(2, n):
        lis.append(lis[i - 2] + lis[i - 1])
    return (lis[0:n])


if __name__ == '__main__':
    n = int(input())
    print(list(map(cube, fibonacci(n))))
