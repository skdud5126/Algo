# SWEA. 5185 [이진수]

'''
16진수 1자리는 2진수 4자리로 표시된다.

N자리 16진수가 주어지면 각 자리 수를 4자리 2진수로 표시하는 프로그램을 만드시오.

단, 2진수의 앞자리 0도 반드시 출력한다.

예를 들어 47FE라는 16진수를 2진수로 표시하면 다음과 같다.

0100011111111110


[입력]

첫 줄에 테스트케이스의 수 T가 주어진다. 1. [가장 먼 노드]<=T<=50

다음 줄부터 테스트 케이스의 별로 자리 수 N과 N자리 16진수가 주어진다. 1. [가장 먼 노드]<=N<=100

16진수 A부터 F는 대문자로 표시된다.

[출력]

각 줄마다 "#T" (T는 테스트 케이스 번호)를 출력한 뒤, 답을 출력한다.
'''
import sys
sys.stdin = open('input.txt', 'r')

dict = {f'{i:X}' : f'{i:04b}' for i in range(16)}   # 16진수를 키 값으로 2진수 value가지는 dict

T = int(input())  # 테스트 케이스 수

for case in range(1, T+1):
    N, decimal = input().split()
    res = []
    for i in range(int(N)):
        res.append(dict[decimal[i]])

    print(f'#{case} {"".join(res)}')
