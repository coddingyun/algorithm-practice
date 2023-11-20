## 시도
```python
from collections import deque

def solution(n, k, cmd):
    answer = ['O']*n
    cancelList = deque([])
    curItem = k
    for item in cmd:
        splitedItem = item.split(" ")
        cmdItem = splitedItem[0]
        if cmdItem == 'U':
            move = int(splitedItem[1])
            while move>0:
                curItem -= 1
                if answer[curItem] == 'O':
                    move -= 1
            
        elif cmdItem == 'D':
            move = int(splitedItem[1])
            while move>0:
                curItem += 1
                if answer[curItem] == 'O':
                    move -= 1
            
        elif cmdItem == 'C':
            answer[curItem] = 'X'
            cancelList.append(curItem)
            move = 1
            while move>0 and curItem < n-1:
                curItem += 1
                if answer[curItem] == 'O':
                    move -= 1
            if curItem == n-1 and answer[curItem] == 'X':
                move = 1
                while move>0:
                    curItem -= 1
                    if answer[curItem] == 'O':
                        move -= 1   
            
        else:
            cancelItem = cancelList.pop()
            if cancelItem == curItem:
                secondCancelItem = cancelList.pop()
                answer[secondCancelItem] = 'O'
                cancelList.append(cancelItem)
            else:
                answer[cancelItem] = 'O'

    return "".join(answer)
```
효율성 테스트에서 시간초과
왜냐면 U, D 일때 최악의 경우 O(n)

## 정답
```python
from collections import deque

def solution(n, k, cmd):
    answer = ["O"]*n
    cancelList = deque([])
    table = { i: [i-1, i+1] for i in range(n)}
    table[0] = [None, 1]
    table[n-1] = [n-2, None]
    curItem = k
    for item in cmd:
        splitedItem = item.split(" ")
        cmdItem = splitedItem[0]
        if cmdItem == 'U':
            for _ in range(int(splitedItem[1])):
                curItem = table[curItem][0]
            
        elif cmdItem == 'D':
            for _ in range(int(splitedItem[1])):
                curItem = table[curItem][1]
            
        elif cmdItem == 'C':
            answer[curItem] = "X"
            
            prev, nex = table[curItem]
            cancelList.append((prev, nex, curItem))
            if nex == None:
                curItem = prev
            else:
                curItem = nex
            
            if prev == None:
                table[nex][0] = None
            elif nex == None:
                table[prev][1] = None
            else:
                table[prev][1] = nex
                table[nex][0] = prev
            
        else:
            prev, nex, recoverItem = cancelList.pop()
            answer[recoverItem] = "O"
            if prev == None:
                table[nex][0] = recoverItem
            elif nex == None:
                table[prev][1] = recoverItem
            else:
                table[nex][0] = recoverItem
                table[prev][1] = recoverItem

    return "".join(answer)
```
연결 리스트로 만들어서 시간복잡도를 낮추었다. [참고](https://kjhoon0330.tistory.com/entry/%ED%94%84%EB%A1%9C%EA%B7%B8%EB%9E%98%EB%A8%B8%EC%8A%A4-%ED%91%9C-%ED%8E%B8%EC%A7%91-Python)
