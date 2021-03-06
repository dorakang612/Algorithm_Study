"""
    # 문제 해결 단서
    0. 입력 형식 : n(500,000,000이하의 자연수)
    1. 숫자의 표현은 1,2,4 만을 이용해서 진행합니다.
        ex) 1(10진수) = 1(124나라)
            2(10진수) = 2(124나라)
            3(10진수) = 4(124나라)
            4(10진수) = 1(124나라)
            5(10진수) = 12(124나라)
            6(10진수) = 14(124나라)
    2. 숫자 n이 입려되면 124나라의 수로 변환하여 반환합니다.(반환하는 자료형은 문자열입니다.)
    3. 3진법을 계산할 때와 동일하게 진행합니다.

    # 문제 해결 방법
    1. n을 3으로 나눈 나머지를 이용해 진수변환을 진행합니다.
    2. n을 3으로 나누었을 때 몫으로 갱신합니다.
"""


def solution(n=0):
    answer = ""
    digits = ["4", "1", "2"]

    while n > 0:
        remainder = n % 3
        answer = digits[remainder] + answer
        remainder = remainder if remainder != 0 else 1
        n = (n-remainder) // 3
    return answer
