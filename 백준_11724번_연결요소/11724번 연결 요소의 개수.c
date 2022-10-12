#include<stdio.h>
#define SZ 1001 //정점의 최대 개수 (이런 게 있으면 일일히 조건을 수정하지 않아도 된다.)

int N, M;
int map[SZ][SZ]; //배열(리스트) 크기를 미리 만들어야 한다. 정적.
int visited[SZ] = { 0 };
int ans_cnt = 0; //연결 요소 개수
 
//깊이 우선 탐색 -> 방문 체크
void do_dfs(int v) {
    visited[v] = 1; //노드 1의 값은 1, 즉 방문한 것으로 표시한다.
    for (int k = 1; k <= N; k++) {
        if (visited[k] == 0 && map[v][k] == 1) { //노드 2의 값이 0이고, map[1][1,2,3,,최대 정점] == 1 (방문을 안 한 노드 중에 간선이 있으면, 예를 들어 [1][2-k-]==1 즉, 1과 2이 연결되어 있으면)
            do_dfs(k); //do_dfs(2)로 이동하고, 그럼 노드 2를 조사한다. 즉, 하나를 물면 끝까지 파고 드는 것.
        }
    }
}
 
void solution() {
    for (int i = 1; i <= N; i++) { //정점 개수
    //방문 노드 표시하기
        if (visited[i] == 0) { //만약 1을 방문하지 않았으면
            ans_cnt++; //일단 연결요소 1개 추가 > why? 방문하지 않은 노드가 있다는 건 연결 요소가 최소 1개 있다는 것이기 때문이다. > 방문하는 건 do_dfs에서 표시할 것이다.
            do_dfs(i); //깊이 우선 탐색으로 1을 조사한다.
        }
    }
}
 
int main() {
    scanf("%d %d", &N, &M); //정점, 간선의 개수 입력

    int u, v; //어떤 정점끼리 연결되는지 입력
    for (int i = 1; i <= M; i++) {
        scanf("%d %d", &u, &v);
        map[u][v] = 1; //인접 리스트
        map[v][u] = 1; //양방향이기 때문에 두 개 설정
    }
 
    solution(); //연결 요소를 만드는 함수로 이동
    for (int i = 1; i <= N; i++) {
        printf("%d ", visited[i]);
    }
    printf("%d", ans_cnt);
}

//그럼 방향이 있는 그래프의 연결 개수를 구해보자.