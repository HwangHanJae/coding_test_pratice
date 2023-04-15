<h1>지우개 - 21756번</h1>

<h2>문제</h2>

$N$개의 칸에 $1$ 부터 $N$ 까지의 수들이 왼쪽부터 순서대로 저장되어 있다. 또, 각 칸은 왼쪽부터 $1$ 부터 $N$까지 순서대로 번호가 붙어 있다. 즉, 처음에는 각 칸의 번호와 각 칸에 저장된 수가 같다.

아래 그림은 $N = 7$일 때의 예이다.

<p style="text-align: center;"><img alt="" src="https://upload.acmicpc.net/1587dd00-130c-42a0-af6e-68b3b484a1b8/-/preview/" style="width: 361px; height: 90px;"/>

다음 작업을 수가 정확히 하나가 남을 때 까지 반복한다.

(A) 홀수번 칸의 수들을 모두 지운다 (B) 남은 수들을 왼쪽으로 모은다.

제일 첫 작업의 (A) 단계가 끝나면 칸들의 상태는 다음과 같을 것이다.

<p style="text-align: center;"><img alt="" src="https://upload.acmicpc.net/1bedbcf7-ee56-4bb0-a83b-d6abbb34ae46/-/preview/" style="width: 361px; height: 90px;"/>

(B) 단계가 끝나면 다음과 같을 것이다.

<p style="text-align: center;"><img alt="" src="https://upload.acmicpc.net/7f311585-5dd0-4033-ada3-5fb9aa0df18b/-/preview/" style="width: 361px; height: 90px;"/>

두번째 작업이 진행되면 칸들은 아래 두 그림과 같이 바뀔 것이다.

<p style="text-align: center;"><img alt="" src="https://upload.acmicpc.net/e070dc76-59fc-4fa6-a0b3-bf310f78dccd/-/preview/" style="width: 361px; height: 90px;"/>

<p style="text-align: center;"><img alt="" src="https://upload.acmicpc.net/e7c0cbf8-ab7d-4b7c-bdac-28b433c83c95/-/preview/" style="width: 361px; height: 90px;"/>

이제 수가 하나 남았으므로 작업은 더 이상 진행되지 않는다.

$N$을 입력으로 받아 위와 같이 작업을 진행했을 때 마지막으로 남는 수를 계산하는 프로그램을 작성하라.

<h2>입력</h2>

첫 번째 줄에 정수 $N$이 주어진다.

<h2>출력</h2>

마지막으로 남는 수를 한 줄에 출력한다.

<h2>출처</h2>

문제링크 : [백준 21756](https://www.acmicpc.net/problem/21756)

풀이법 : https://my-develop-note.tistory.com/