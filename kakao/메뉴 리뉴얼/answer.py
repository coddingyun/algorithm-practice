from itertools import combinations

def solution(orders, course):
    answer = []
    ordersCombs = [[] for _ in range(len(orders))]
    result = [[] for _ in range(21)]
    visited = []
    for idx, order in enumerate(orders):
        for i in range(2, len(order)+1):
            if i in course:
                combs = list(combinations(order, i))
                ordersCombs[idx] += combs

    for idx, ordersComb in enumerate(ordersCombs):
        for item in ordersComb:
            item = tuple(sorted(list(item)))
            if item not in visited:
                visited.append(item)
                cnt = 1
                for idx2, ordersComb2 in enumerate(ordersCombs):
                    if idx != idx2:
                        for item2 in ordersComb2:
                            item2 = tuple(sorted(list(item2)))
                            if item == item2:
                                cnt += 1
                lengthItem = len(item)
                if lengthItem in course and cnt > 1:
                    if result[lengthItem]:
                        curMax = result[lengthItem][0][0]
                        if curMax == cnt:
                            result[lengthItem].append((cnt, "".join(item)))
                        elif curMax < cnt:
                            result[lengthItem] = []
                            result[lengthItem].append((cnt, "".join(item)))
                    else:
                        result[lengthItem].append((cnt, "".join(item)))
    
    for item in result:
        if item:
            for i in item:
                answer.append(i[1])
    answer.sort()                 
    return answer
