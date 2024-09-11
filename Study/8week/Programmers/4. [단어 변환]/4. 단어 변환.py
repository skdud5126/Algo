# Programmers. [단어 변환]
'''
두 개의 단어 begin, target과 단어의 집합 words가 있습니다.

아래와 같은 규칙을 이용하여 begin에서 target으로 변환하는 가장 짧은 변환 과정을 찾으려고 합니다.

1. 한 번에 한 개의 알파벳만 바꿀 수 있습니다.

2. words에 있는 단어로만 변환할 수 있습니다.

예를 들어 begin이 "hit", target가 "cog", words가 ["hot","dot","dog","lot","log","cog"]라면 "hit" -> "hot" -> "dot" -> "dog" -> "cog"와 같이 4단계를 거쳐 변환할 수 있습니다.

두 개의 단어 begin, target과 단어의 집합 words가 매개변수로 주어질 때, 최소 몇 단계의 과정을 거쳐 begin을 target으로 변환할 수 있는지 return 하도록 solution 함수를 작성해주세요.

[제한사항]

각 단어는 알파벳 소문자로만 이루어져 있습니다.

각 단어의 길이는 3 이상 10 이하이며 모든 단어의 길이는 같습니다.

words에는 3개 이상 50개 이하의 단어가 있으며 중복되는 단어는 없습니다.

begin과 target은 같지 않습니다.

변환할 수 없는 경우에는 0를 return 합니다.

'''

# def solution(begin, target, words):
#     answer = 0
#     if target not in words:   # target이 words 목록에 없으면 함수 실행 필요 없음
#         answer = 0
#         return answer
#
#
#
#     return answer

# 일단 words에 target이 없으면 돌릴 필요없음 retrun
# 만약 words에 target이 있으면 포문 돌려서 한개씩 차이나는 단어를 찾고 begin을 새로 갱신 cnt+=1 그렇게 갱신하다가 target이랑 같아지면 return cnt
# bfs로 접근해야겠다


begin = 'hit'
target= 'cog'
words = ['hot','dot','dog','lot','log','cog']
tree = []
cnt = 0

for w in words:
    count = 0
    for i in range(len(begin)):
        if begin[i] != w[i]:
            count+=1
            cnt+=1
            if count == 1:
                tree.append([w,cnt])
                break

print(tree)