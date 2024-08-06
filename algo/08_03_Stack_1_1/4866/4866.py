# SWEA 4866 [파이썬 S/W 문제해결 기본] 4일차 - 괄호검사

'''
주어진 입력에서 괄호 {}, ()가 제대로 짝을 이뤘는지 검사하는 프로그램을 만드시오.

예를 들어 {( )}는 제대로 된 짝이지만, {( })는 제대로 된 짝이 아니다. 입력은 한 줄의 파이썬 코드일수도 있고, 괄호만 주어질 수도 있다.

정상적으로 짝을 이룬 경우 1, 그렇지 않으면 0을 출력한다.

print(‘{‘) 같은 경우는 입력으로 주어지지 않으므로 고려하지 않아도 된다.


[입력]


첫 줄에 테스트 케이스 개수 T가 주어진다.  1≤T≤50

다음 줄부터 테스트 케이스 별로 온전한 형태이거나 괄호만 남긴 한 줄의 코드가 주어진다.


[출력]

각 줄마다 "#T" (T는 테스트 케이스 번호)를 출력한 뒤, 답을 출력한다.
'''
import sys
sys.stdin = open('input.txt', 'r')



def search_correct(code):

    subset = []
    matching_dict = {'(': ')', '{': '}', '[': ']'}

    for char in code:   # 인풋값 한글자씩 순회
        if char in matching_dict.keys():
            subset.append(char)     # 열린괄호 더해줌
        elif char in matching_dict.values():
            if not subset or char != matching_dict[subset[-1]]:  # subset이 비었거나 짝이 맞지 않은 괄호 있을 시 False
                return False
            subset.pop()  # 짝이 맞는 최근 열린괄호 삭제
    return not subset   # subset이 비어있으면 True 반환 아니면 False




T = int(input())  # 테스트 케이스 수 T


for case in range(1, T+1):
    input_code = input()  # 파이썬 코드 입력받음

    print(f'#{case}' , end = ' ')
    if search_correct(input_code):  # 짝이 다맞음(subset 비어있음)
        print(1)
    else:
        print(0)