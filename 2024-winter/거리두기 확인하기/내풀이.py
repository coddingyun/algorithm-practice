def check(graph, i, j):
    if i+2 < 5 and graph[i+2][j] == 'P':
        if graph[i+1][j] != 'X':
            return False
    if j+2 < 5 and graph[i][j+2] == 'P':
        if graph[i][j+1] != 'X':
            return False
    if i+1 < 5 and graph[i+1][j] == 'P':
        return False
    if j+1 < 5 and graph[i][j+1] == 'P':
        return False
    if i+1 < 5 and j+1 < 5 and graph[i+1][j+1] == 'P':
        if graph[i+1][j] != 'X' or graph[i][j+1] != 'X':
            return False
    if i+1 < 5 and j-1 >= 0 and graph[i+1][j-1] == 'P':
        if graph[i+1][j] != 'X' or graph[i][j-1] != 'X':
            return False
    return True

def solution(places):
    answer = []
    for place in places:
        flag = True
        for i in range(5):
            if flag == False:
                break
            for j in range(5):
                if place[i][j] == 'P':
                    if check(place, i, j) == False:
                        flag = False
                        break
        if flag:
            answer.append(1)
        else:
            answer.append(0)
             
    return answer
