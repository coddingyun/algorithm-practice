def findCandidateAnswer(start, end, sticker):
    dp = [0]*end
    dp[start] = sticker[start]
    dp[start+1] = max(sticker[start], sticker[start+1])
    for i in range(start+2, end-1):
        dp[i] = max(dp[i-2] + sticker[i], dp[i-1])
    return dp[end-2]

def solution(sticker):
    answer = 0
    length = len(sticker)
    if length == 1:
        return sticker[0]
    if length == 2:
        return max(sticker[0], sticker[1])
    answer1 = findCandidateAnswer(0, length, sticker)
    answer2 = findCandidateAnswer(1, length+1, sticker)
    return max(answer1, answer2)
