# SWEA. 1979 [어디에 단어가 들어갈 수 있을까]

'''
N X N 크기의 단어 퍼즐을 만들려고 한다. 입력으로 단어 퍼즐의 모양이 주어진다.

주어진 퍼즐 모양에서 특정 길이 K를 갖는 단어가 들어갈 수 있는 자리의 수를 출력하는 프로그램을 작성하라.

'''
import sys
sys.stdin = open('input.txt', 'r')

def make_string(puzzle):   # string으로 한줄 입력   /  ['01001', '01011', '11111', '11010', '10011']
    res = []
    for i in puzzle:
        str = ''
        for j in i:
            str += j
        res.append(str)
    return res

def split_zero(puzzle):  # 0을 기준으로 자름 / [['', '1', '', '1'], ['', '1', '11'], ['11111'], ['11', '1', ''], ['1', '', '11']]
    word = []
    for i in make_string(puzzle):
        word.append(i.split('0'))
    return word

T = int(input())  # 테스트 케이스 수

for case in range(1, T+1):
    N, K = map(int,input().split())  # N 가로,세로 퍼즐 크기 / K 단어의 길이
    puzzle = [list(input().split()) for _ in range(N)]  # NXN 크기 퍼즐
    hap = 0
    find_K = '1'*K  # K만큼 연속된 1 찾기 위한 케이스 생성
    sero_puzzle = [[0]*N for _ in range(N)]  # 세로 방향 빈 퍼즐

    for i in range(N):   # 세로 검사 위함
        for j in range(N):
            sero_puzzle[i][j] = puzzle[j][i]   # 전치

    for garo in split_zero(puzzle):
        hap += garo.count(find_K)
    for sero in split_zero(sero_puzzle):
        hap += sero.count(find_K)

    print(f'#{case} {hap}')