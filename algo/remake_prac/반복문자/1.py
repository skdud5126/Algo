'''
원겸이는 문자열을 정리하는 게임을 하려고 한다.
문자열에서 같은 문자가 두 개 이상 연속된다면, 그 문자를 모두 제거하고 그 만큼의 점수를 얻는다.
한 번 정리를 한 이후에 다시 연속된 문자가 있다면, 다시 제거할 수 있다.
또한 정리 이후에 두개 이상의 연속하는 문자가 있을 경우 연속한 문자의 길이만큼 점수를 추가로 얻는다.
만약 연속하는 문자가 여러쌍일 경우, 모두 계산한다.
원겸이는 몇점을 얻을까?

다음은 XAAYBBBCDDCZD에서 반복문자를 지우는 경우의 예이다.

XAAYBBBCDDCZD에서 반복문자 AA, BBB, DD를 지우고 각각 2, 3, 2점을 얻는다. 그리고 X Y C CZD를 잇는다.
XYCCZD에서 반복문자 CC를 지우고 2점을 얻는다. 그리고 XY ZD를 잇는다.
XYZD는 반복문자가 없고 XYZ가 연속되므로 3점을 얻는다.
총점 12점을 리턴한다.


[입력]
첫 줄에 테스트 케이스 개수 T가 주어진다.  1 ≤ T ≤ 50
다음 줄부터 테스트 케이스의 별로 길이가 1000이내인 문자열이 주어진다.

[출력]
#과 1번부터인 테스트케이스 번호, 빈칸에 이어 답을 출력한다.

'''
T=int(input())

for case in range(1, T+1):
    exp = input()   # XAAYBBBCDDCZD
    stack = []
    t = []
    for ch in exp:
        if not stack or stack[-1] != ch:
            stack.append(ch)
        else:
            count= 0
            while stack[-1] == ch:
                print(stack)
                stack.pop()
                count+=1
            t.append(count)
    print(t)