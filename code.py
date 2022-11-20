
import random
import time

def Example(list):
    arr2 = [0,0,0,0,0]
    n = len(list) # n = length of the list
    for i in range(n):
        if list[i] == 0:
            for t1 in range(i,n):
                p1 = t1**(0.5)
                x1 = n + 1
                while x1 >= 1:
                    x1 = x1 // 2
                    arr2[i % 5] += 1

        elif list[i] == 1:
            for t2 in range(n,0,-1):
                for p2 in range(1,n + 1):
                    x2 = n+1
                    while x2 > 0:
                        x2 = x2 // 2
                        arr2[i % 5] += 1

        elif list[i] == 2:
            for t3 in range(1,n+1):
                x3 = t3 + 1
                for p3 in range(0, t3**2):
                    arr2[i % 5] += 1
    return arr2

size = [1, 5, 10, 25, 50, 75, 100, 150, 200, 250]

def count(list):
    count = [0,0,0]
    for i in list:
        count[i] += 1
    return count

for i in size:
    for case in ['best', 'average', 'worst']:
        if case == 'best':
            input = [0] * i
            start = time.time()
            Example(input)
            end = time.time()
            print('Case: ' + str(case) + '\tSize: ' + str(i) + '\tElapsed Time: ' + str(end - start))
        elif case == 'worst':
            input = [2] * i
            start = time.time()
            Example(input)
            end = time.time()
            print('Case: ' + str(case) + '\tSize: ' + str(i) + '\tElapsed Time: ' + str(end - start))
        elif case == 'average':
            totalTime = 0
            for j in range(3):
                input = [random.randint(0, 2) for i in range(i)]
                start = time.time()
                Example(input)
                end = time.time()
                totalTime  += (end - start)
            print('Case: ' + str(case) + '\tSize: ' + str(i) + '\tElapsed Time: ' + str(totalTime / 3))

print(Example(list))
