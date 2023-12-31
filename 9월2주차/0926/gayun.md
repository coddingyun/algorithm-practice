## 풀이방법
1. 회색 건물을 dfs로 구한다. dfs로 구하면서 인접해 있는 회색의 개수도 센다. 이때, 6-인접 개수가 벽면의 개수가 된다.

2. 하지만! 회색으로 둘러싸여져있는 경우에는 안쪽 벽면은 제외시켜주어야 한다.
따라서 하얀색 건물을 따로 또 dfs로 구해준다. 이때 똑같이 6-인접개수를 계산해준다. 
하지만 이렇게 구해진 하얀색 건물 클러스터에서 하나의 아이템이라도 지도의 끝에 위치하게 되면 그것은 회색 안쪽이 아니다.

이렇게 해서 **회색 건물의 벽면 개수 - 회색 내부의 하얀색 건물의 벽면 개수** 로 정답을 구할 수 있다.

## 시행착오
1. 처음부터 너무 당연하게 일반 배열처럼 생각하여 w,h을 반대로 두고 풀었다. 이로인해 모든 조건도 반대가 되면서 삽질을 많이 했다. 결국 직접 예제를 그려봐야 했다. 그러니까 처음부터 문제를 잘 읽어야 하고! 종이와 펜 필수..
2. 첫번째 예제를 보면서 회색 건물 내에 하얀색 건물이 있을 때에는 하얀색 건물의 6면다 회색 건물일때라고 단정지어 생각했다. 그래서 처음에 graph돌면서 조건을 찾아서 회색으로 바꾸어주었는데, 예제 2가 틀려서 직접 그리면서 살펴보니 내부의 흰색 건물이 많아질 수 있다는 것을 깨달았다. 예제 2개다 직접 미리 해보고 구현 들어가야 한다!

## 다른 사람의 풀이?
시행착오 2번의 사실을 깨닫고 멘탈이 약해져서 구글링을 좀 했다. 근데 사람들 대부분 발상의 전환 풀이를 썼다. 왼오아래위로 1줄씩 확장시킨 다음 흰색을 대상으로 bfs로 푸는 것이다. 
그리고 회색과 인접할 때마다 계산을 해주는 것이다!

![image](https://github.com/CODING-TEST-PYTHON/SOMA_ALGO/assets/81891345/10461f3a-440e-415a-81cc-623847259019)


즉, 정통방법으로는 너무 복잡해질때는 반대로 생각해보는 것도 중요하다. 하지만 이는 웬만하면 코드 구현전에 모두 마쳐야 한다.. 중간에 바꾸기란 쉽지 않다.
