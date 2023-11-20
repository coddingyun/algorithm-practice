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
