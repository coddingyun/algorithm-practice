def solution(today, terms, privacies):
    answer = []
    dictArr = {}
    year, month, date = today.split(".")
    for item in terms:
        a, b = item.split(" ")
        b = int(b)
        dictArr[a] = int(b)
    for idx, privacy in enumerate(privacies):
        a, b = privacy.split(" ")
        pYear, pMonth, pDate = a.split(".")
        monthPeriod = dictArr[b]
        expiredDate = []
        dividend = (int(pMonth) + monthPeriod)//12
        remainder = (int(pMonth) + monthPeriod)%12
        if dividend > 0:
            if remainder == 0:
                expiredDate = [int(pYear)+dividend-1, int(pMonth)+monthPeriod-12*(dividend-1), int(pDate)]
            else:
                expiredDate = [int(pYear)+dividend, int(pMonth)+monthPeriod-12*dividend, int(pDate)]
        else:
            expiredDate = [int(pYear), int(pMonth)+monthPeriod, int(pDate)]
        eYear, eMonth, eDate = expiredDate
        if int(year) > eYear:
            answer.append(idx+1)
        elif int(year) == eYear and int(month) > eMonth:
            answer.append(idx+1)
        elif int(year) == eYear and int(month) == eMonth and int(date) >= eDate:
            answer.append(idx+1)
        
        
    return answer
