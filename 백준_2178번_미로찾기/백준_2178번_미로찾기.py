"""
미로 구하기

행열로 이루어진 미로 만들기
최소 이동 거리 구하는 함수

입력
1. N, M (N 행-줄-, M 열-가로-)
# 2<= N, M <= 100
2. 1과 0 : 미로
# 총 개수 N*M

출력
(1,1)에서 (N,M)로 이동한 칸 수 

"""

import queue
import sys
from collections import deque

#입력값 시간 줄이기
input = sys.stdin.readline

#입력 받기
n, m = map(int, input().split())
"""
변수 = input('입력하시오.').split()

- 문법 설명
input() 함수는 입력받는다.
int() 함수는 정수형으로 바꿔준다.
int(input()) 는 입력값을 int로 바꿔준다.
split() 함수는 한 문자열을 나누어 리스트로 구분해준다. (기본은 띄어쓰기)
    hello world 를 입력하면 ['hello', 'world']로 구분해준다.
입력받은 값을 int로 바꾸려면 어떻게 해야할까?
    int(input())을 한다.
그럼 여러 개의 값을 입력받고 int로 바꾸려면 어떻게 해야할까?
    int(input().split())을 한다. >> Error
    Why? int함수는 '리스트'를 입력값으로 바꿀 수 없다.
    How? 이걸 해결하기 위해서 map 함수를 사용한다.
map(적용할 함수, 반복 가능한 자료형-리스트, 튜플 등-) 함수는 인자 하나하나를 함수 적용하는 것이다.
예를 들어 map(int, 리스트A)는 리스트A의 인자 하나하나를 모두 int형으로 바꾸는 것이다.
따라서 map(int, input().split())는
입력받은 값을 띄어쓰기로 구분하여 나누어 list에 저장하고, 그 list의 인자를 int형으로 모두 변환한다.
"""
#입력받은 1,0를 넣을 리스트
graph = []

for _  in range(n):
    graph.append(list(map(int, input().rstrip())))
"""
for와 range 문법

for 변수 in range(횟수):
    반복할 코드

rstrip() 함수는 인자로 전달된 문자를 String의 오른쪽에서 제거한다.
    why? \n을 제외해야 하기 때문이다. 하지만 strip를 사용해도 똑같이 나온다.

list.append() 함수는 리스트 뒤에 값을 추가한다.
맨 뒤값을 제거하고 받은 입력값을 모두 자료형으로 바꿔주고, list로 만든다.
그렇게 만들어진 리스트를 graph에 추가하고, 이 과정을 n번 (n줄) 반복한다.

split()함수를 사용하지 않는 이유?
    split는 공백처리를 하기 때문에 11111 을 입력했을 경우, [11111]로 받는다.
    그러나 strip()함수를 이용하면 11111을 입력하면, [1, 1, 1, 1, 1]로 받는다.

즉, 위 코드를 해석하면
문자를 1개씩 입력받고, int형으로 바꿔 리스트를 1개 만든다.
그 리스트를 graph에 추가하여 [ [], [], [] ]로 만들고, n번 반복한다.

"""

dx = [1, -1, 0, 0]
dy = [0, 0, -1, 1]
"""
동,서,남,북
오, 왼, 하, 상
"""

#BFS 함수 : 최단 거리
def bfs(x, y):

    queue = deque()
    queue.append((x, y))
    """
    queue는 변수
    변수 queue에 큐 자료구조 지정.
    x, y는 현위치.

    queue.append((x, y))
    queue의 시작점을 먼저 설정한다.
    x, y를 넣는 게 아닌, (x, y)를 넣는 것이기 때문에 반드시 괄호를 2개 사용
    """
    
    #len(queue) > 0
    while queue:
        x, y = queue.popleft()
        """
        #왜 변수를 넣는가? 왜 queue가 빈 값이 나올 때까지 반복문을 돌리는 의미인가?
        while문의 조건식에 변수가 들어가면, 그 변수가 NULL이 아닐 경우 True를 반환한다.
        따라서 queue를 하나씩 빼고, 모두 사용해서 더 이상 값이 아니면 break

        queue.popleft() 함수는 큐의 왼쪽에서 값을 뺀다.
        그 값을 x, y에 각각 대입한다.
        queue.popleft의 값, 큐의 가장 왼쪽에 있는 값은 가장 최근에 추가된 값이다.
        즉, 현재 위치는 가장 최근의 값으로 이동한다.
        """

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < n and 0 <= ny < m and graph[nx][ny] == 1:
                queue.append((nx, ny))
                graph[nx][ny] = graph[x][y] + 1

                """
                for i in range(4)
                4번 반복한다. 왜? 동서남북을 확인해야 하므로.
                i가 0,1,2,3 일 때를 순서대로 각각 확인한다.
                즉, i=0일 때 아래식을 수행.
                i=1일 때,,, i=3일 때까지.
                여기서 i는 위에서 설정한 dx[i], dy[i]로 사용한다.

                nx는 x+dx[i]이다. i=0일 때,
                이 말은 x의 위치, 즉 가로(행)은 현재위치+1(동) 이다.
                마찬가지로 ny = y+dy[i]는 현재위치+0(동) 이다.
                nx, ny는 옮기려는 위치이다.

                만약, 옮기려는 위치가 0~n 이고, 그 값이 1이면 (1일 때 움직일 수 있다. 위에서 입력한 미로)
                (쉽게 말해서 옮길 수 있는 위치이면)
                queue 값에 그 위치를 추가하고, 그 위치의 값에 1을 더한다.
                why? 움직이는 위치 값을 구해야 하기 때문이다.
                """

    return graph[n-1][m-1]
    """
    이제 graph의 마지막 위치에서 바로 직전까지의 값을 리턴한다.    
    """

"""
- 함수 문법
def 함수명() :
    수행문장
    return
"""

print (bfs(0,0))