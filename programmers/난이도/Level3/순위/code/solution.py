"""
    # 문제 해결 단서
    0. 입력 형식 : n(선수의 수, 1~100명), results(경기 결과, 1개이상 4500개 이하)
        - results 배열 각 행 [A,B]는 A 선수가 B 선수를 이겼다는 의미 입니다.
        - 경기 결과에는 모순이 없습니다.
    1. n명의 권투 선수가 대회에 참여했고 각각 1번 부터 n번 까지 번호를 받았습니다.
    2. 1대1 방식으로 진행이 되었고, A 선수가 B 선수보다 실력이 좋다면 A 선수는 B 선수를 항상 이깁니다.
    3. 심판이 주어진 경기 결과를 보고 선수들의 순위를 매기려합니다.
    4. 유실된 경기결과로 인해 정확한 순위를 매길 수 없는 경우, 확실하게 순위를 매길 수 있는 선수들의 수를 반환합니다.

    # 문제 해결 방법
    1. 주어진 정보들을 이용해서 인접 리스트 형식의 그래프를 생성합니다.
    2. 1번 부터 n번까지 순회를 하며 등수를 정할 수 있는 선수들의 수를 셉니다.
    3. 해당 process에 주어진 선수에 대하여 모든 조상의 수와 자손의 수를 셉니다.
    4. 위에서 구한 수가 n-1인 경우 해당 선수는 등수를 확정 지을 수 있습니다.
"""


def solution(n=0, results=[]):
    answer = 0
    parent = 'parent'
    child = 'child'
    diGraph = {i: {parent: [], child: []} for i in range(1, n+1)}
    checker = [0 for _ in range(n+1)]

    def ancestors(player=0):
        count = 0
        for ans in diGraph[player][parent]:
            if checker[ans] == 0:
                checker[ans] = 1
                count += 1 + ancestors(ans)
        return count

    def descendants(player=0):
        count = 0
        for des in diGraph[player][child]:
            if checker[des] == 0:
                checker[des] = 1
                count += 1 + descendants(des)
        return count

    for winner, loser in results:
        diGraph[winner][child].append(loser)
        diGraph[loser][parent].append(winner)

    for player in range(1, n+1):
        ans = ancestors(player)
        des = descendants(player)
        answer += 1 if ans + des == n-1 else 0
        checker = [0 for _ in range(n+1)]

    return answer


print(solution(5, [[4, 3], [4, 2], [3, 2], [1, 2], [2, 5]]))
