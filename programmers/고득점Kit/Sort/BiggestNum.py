'''
    *문제 설명
    0 또는 양의 정수가 주어졌을 때, 정수를 이어 붙여 만들 수 있는 가장 큰 수를 알아내 주세요.
    예를 들어, 주어진 정수가 [6, 10, 2]라면 [6102, 6210, 1062, 1026, 2610, 2106]를 만들 수 있고, 이중 가장 큰 수는 6210입니다.
    0 또는 양의 정수가 담긴 배열 numbers가 매개변수로 주어질 때,
    순서를 재배치하여 만들 수 있는 가장 큰 수를 문자열로 바꾸어 return 하도록 solution 함수를 작성해주세요.

    *제한 사항
    - numbers의 길이는 1 이상 100,000 이하입니다.
    - numbers의 원소는 0 이상 1,000 이하입니다.
    - 정답이 너무 클 수 있으니 문자열로 바꾸어 return 합니다.

    *입출력 예
    numbers	            return
    [6, 10, 2]	        6210
    [3, 30, 34, 5, 9]	9534330
'''

'''
    * Idea
    0. 숫자가 모두 0이라면 0을 return 한다. => 최종 숫자를 만들어 int로 형변환 한 뒤 다시 string으로 변환.
    1. 숫자의 앞자리를 기준으로 정렬한다.
    2. 한 자리수가 최상위 우선순위를 갖는다.
    3. 두자리 수 와 세자리 수 비교
        36,353 => 36353 > 35336
        36,362 => 36362 > 36236
        36,363 => 36363 > 36336
        36,364 => 36364 < 36436
        36,373 => 36373 < 37336
        36,374 => 36374 < 37436
        36,378 => 36378 < 37836
    
    *문제 해결 방안
    1. 1~9에 해당하는 set 생성 각각의 set에는 자리수 별로 list 할당.
        ex) one = { 'len_1' : [1,1,1,] , 'len_2' : [11,12,13,15], 'len_3' : [123,125,178,190]}
'''


def solution(numbers=[]):
    answer = ''
    return answer
