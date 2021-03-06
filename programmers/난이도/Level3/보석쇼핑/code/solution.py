"""
    # 문제 해결 단서
    0. 입력 형식 : gems(보석 진열 상태)
    1. 진열된 모든 종류의 보석을 적어도 1개 이상 포함하는 가장 짧은 구간을 찾습니다.
    2. 보석은 진열대의 특정 범위의 물건을 모두 구매합니다.(특정 위치를 건너 뛰지 않습니다.)
    3. Set 자료형을 이용해 중복이 없이 보석의 종류를 알아낼 수 있습니다.

    # 문제 해결 방법
    1. 문제 해설 방법과 동일

    # 카카오 테크 블로그의 문제 해설을 읽어본 뒤 해결하였습니다.
        - Link : https://tech.kakao.com/2020/07/01/2020-internship-test/
"""


def solution(gems=[]):
    gem_list = set(gems)
    min_info = {'length' : len(gems) + 1, 'section':[1,len(gems)]}
    start = 0
    end = 0
    basket = {gems[start] : 1}

    while start < len(gems) and end < len(gems):
        if len(basket) == len(gem_list):
            if end - start + 1 < min_info['length']:
                min_info['length'] = end - start + 1
                min_info['section'] = [start + 1, end + 1]
            basket[gems[start]] -= 1
            if basket[gems[start]] == 0:
                del basket[gems[start]]
            start += 1
        
        else:
            end += 1
            if end >= len(gems):
                break
            if gems[end] in basket :
                basket[gems[end]] += 1
            else:
                basket[gems[end]] = 1

    return min_info['section']