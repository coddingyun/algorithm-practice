graph = [[""]*52 for _ in range(52)]
mergeList = []

def changeMergedCell(r, c, value):
    for item in mergeList:
        for location in item:
            rl, cl = location
            if (rl == r and cl == c):
                for location in item:
                    rl, cl = location
                    graph[rl][cl] = value
                return
    graph[r][c] = value

def updateLocation(r, c, value):
    r, c = int(r), int(c)
    changeMergedCell(r, c, value);

def updateValue(v1, v2):
    for i in range(52):
        for j in range(52):
            if graph[i][j] == v1:
                changeMergedCell(i, j, v2)

def mergeTwoCell(item1, r, c, nr, nc):
    for item in mergeList:
        for location in item:
            rl, cl = location
            if (rl == nr) and (cl == nc):
                if item == item1:
                    return
                newItem = item1 + item
                mergeList.remove(item)
                mergeList.remove(item1)
                mergeList.append(newItem)
                return True
    return False

def changeTwoCell(r1, c1, r2, c2):
    if graph[r1][c1]:
        for item in mergeList:
            for location in item:
                rl, cl = location
                if (rl == r2) and (cl == c2):
                    for location in item:
                        rl, cl = location
                        graph[rl][cl] = graph[r1][c1]
    elif graph[r2][c2]:
        for item in mergeList:
            for location in item:
                rl, cl = location
                if (rl == r1) and (cl == c1):
                    for location in item:
                        rl, cl = location
                        graph[rl][cl] = graph[r2][c2]

def merge(r1, c1, r2, c2):
    r1, c1, r2, c2 = int(r1), int(c1), int(r2), int(c2)
    if r1==r2 and c1==c2:
        return
    for item in mergeList:
        for location in item:
            rl, cl = location
            if (rl==r1 and cl==c1) and (rl==r2 and cl==c2):
                continue
            elif (rl==r1 and cl==c1) or (rl==r2 and cl==c2):
                flag = False
                if (rl==r1 and cl==c1):
                    if mergeTwoCell(item, r1, c1, r2, c2) == False:        
                        item.append((r2, c2))
                        flag = True
                else:
                    if mergeTwoCell(item, r2, c2, r1, c1) == False:        
                        item.append((r1, c1))
                        flag = True
                if flag == True:
                    if graph[r1][c1]:
                        for location in item:
                            rl, cl = location
                            graph[rl][cl] = graph[r1][c1]
                    elif graph[r2][c2]:
                        for location in item:
                            rl, cl = location
                            graph[rl][cl] = graph[r2][c2]
                else:
                    changeTwoCell(r1, c1, r2, c2)
                return
                             
    mergeList.append([(r1, c1), (r2, c2)])
    if graph[r1][c1]:
        graph[r2][c2] = graph[r1][c1]
    elif graph[r2][c2]:
        graph[r1][c1] = graph[r2][c2]

def unmerge(r, c):
    r, c = int(r), int(c)
    for item in mergeList:
        for location in item:
            rl, cl = location
            if (rl==r and cl==c):
                for location in item:
                    rl, cl = location
                    if (rl!=r or cl!=c):
                        graph[rl][cl] = ""
                mergeList.remove(item)
                return

def printValue(r, c):
    r, c = int(r), int(c)
    if graph[r][c] != "":
        return graph[r][c]
    else:
        return "EMPTY"

def solution(commands):
    answer = []
    for item in commands:
        commandArr = item.split(" ")
        command = commandArr[0]
        length = len(commandArr)
        if command == "UPDATE" and length == 4:
            updateLocation(commandArr[1], commandArr[2], commandArr[3])
        elif command == "UPDATE" and length == 3:
            updateValue(commandArr[1], commandArr[2])
        elif command == "MERGE":
            merge(commandArr[1], commandArr[2], commandArr[3], commandArr[4])
        elif command == "UNMERGE":
            unmerge(commandArr[1], commandArr[2])
        elif command == "PRINT":
            value = printValue(commandArr[1], commandArr[2])
            answer.append(value)
        
    return answer
