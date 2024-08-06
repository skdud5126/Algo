# SWEA 21619. Stack1 - 연습문제 2. 괄호 검사

'''
[입력]


첫 줄에 테스트 케이스 개수 T가 주어진다.  1≤T≤50

다음 줄부터 테스트 케이스 별로 온전한 형태이거나 괄호만 남긴 한 줄의 코드가 주어진다.



[출력]

각 줄마다 "#T" (T는 테스트 케이스 번호)를 출력한 뒤, 답을 출력한다.

'''
import sys
sys.stdin = open('input.txt','r')

T = int(input())   # 테스트 케이스 수

def search_correct(expression):
    subset = []  # 스택 빈 리스트로 초기화

    for char in expression:   # 문자열 하나씩 순회
        if char in ['(']:    # 열린 괄호 딕셔너리에 있는지 확인
            subset.append(char)   # 있으면 subset에 더해줌
        elif char in [')']:   # 닫힌 괄호 확인
            if not subset: # subset이 비어있음 짝이 안맞음
                return False
            subset.pop()  # 짝이 맞으면 삭제

    return not subset  # subset이 비었으면 True 반환, 아니면 False 반환



for case in range(1, T+1):
    bracket = input()
    print(f'#{case}', end = ' ')
    if search_correct(bracket):   # 괄호가 온전한지 안한지 확인하는 함수
        print(1)  # 온전하면 1
    else:
        print(-1)  # 아니면 -1 반환


