from collections import deque
import sys
sys.setrecursionlimit(10**9)

def makeTwoNum(number):
    result = deque([])
    while True:
        remainder = number % 2
        number = number // 2
        result.appendleft(remainder)
        if number == 1:
            result.appendleft(1)
            break
    resultArr = ""
    for item in result:
        resultArr += str(item)
    return resultArr

def findDepth(twoNumber):
    length = len(twoNumber)
    i = 0
    while True:
        if 2**i-1 >= length:
            return i
        i+=1

visited = [0]*100
flag = False
        
def findTree(start, end, previous, twoNumber):
    global visited
    global flag
    if start == len(twoNumber)-1:
        return
    if flag:
        return
    if start == end:
        return
    
    length = len(twoNumber)
    index = (start+end)//2

    if visited[index] == 0:
        visited[index] = 1
        value = int(twoNumber[index])
        if previous < value:
            flag = True
            
        findTree(start, index, value, twoNumber)
        findTree(index, end, value, twoNumber)
       

def solution(numbers):
    global visited
    global flag
    answer = []
    for number in numbers:
        visited = [0]*100
        flag = False
        twoNumber = format(number, 'b')
        length = len(twoNumber)
        depth = findDepth(twoNumber)
        twoNumber = "0"*(2**depth-1-length)+twoNumber
        findTree(0, len(twoNumber), 1, twoNumber)
        if flag:
            answer.append(0)
        else:
            answer.append(1)
        #print('end')
        #answer.append(int(findTree(0, length, 1, twoNumber)))
        #print(answer)
    return answer
