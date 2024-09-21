# Programmers. [여행 경로]

"""
문제 설명

주어진 항공권을 모두 이용하여 여행경로를 짜려고 합니다. 항상 "ICN" 공항에서 출발합니다.

항공권 정보가 담긴 2차원 배열 tickets 가 매개변수로 주어질 때, 방문하는 공항 경로를 배열에 담아 return 하도록 solution 함수를 작성해주세요.

[제한사항]

모든 공항은 알파벳 대문자 3글자로 이루어집니다.

주어진 공항 수는 3개 이상 10,000개 이하입니다.

tickets 의 각 행 [a, b]는 a 공항에서 b 공항으로 가는 항공권이 있다는 의미입니다.

주어진 항공권은 모두 사용해야 합니다.

만일 가능한 경로가 2개 이상일 경우 알파벳 순서가 앞서는 경로를 return 합니다.

모든 도시를 방문할 수 없는 경우는 주어지지 않습니다.

입출력 예 설명

예제 #1. [가장 먼 노드]

["ICN", "JFK", "HND", "IAD"] 순으로 방문할 수 있습니다.

예제 #2

["ICN", "SFO", "ATL", "ICN", "ATL", "SFO"] 순으로 방문할 수도 있지만 ["ICN", "ATL", "ICN", "SFO", "ATL", "SFO"] 가 알파벳 순으로 앞섭니다.

"""

#
# def solution(tickets):
#     ans = []
#     start = "ICN"
#     road_dict = {}  # {'ICN': ['SFO', 'ATL'], 'SFO': ['ATL'], 'ATL': ['ICN', 'SFO']}
#     for s, v in tickets:
#         if s in road_dict:
#             road_dict[s].append(v)
#         else:
#             road_dict[s] = [v]
#
#     for key in road_dict.keys():  # 문제에서 만일 가능한 경로가 2개 이상일 경우 알파벳 순서가 앞서는 경로 return 위해 sort작업처리
#         road_dict[key].sort()
#
#
#     def dfs(root, answer):
#         answer.append(root)  # 경로 추가
#         for next_root in road_dict[root]:
#             if next_root in answer:  # 경로에 있으면 컨티뉴
#                 continue
#             answer.append(next_root)
#             dfs(next_root, answer)
#
#     dfs(start, ans)
#     return ans
#
#
# print(solution([["ICN", "SFO"], ["ICN", "ATL"], ["SFO", "ATL"], ["ATL", "ICN"], ["ATL","SFO"]]))

from collections import deque
'''
def solution(tickets):
    ans = []
    start = "ICN"
    road_dict = {}  # {'ICN': ['JFK'], 'HND': ['IAD'], 'JFK': ['HND']}
    visited = {}  # {'ICN': [0], 'HND': [0], 'JFK': [0]}

    for s, v in tickets:
        if s in road_dict:
            road_dict[s].append(v)
            visited[s].append(0)
        else:
            road_dict[s] = [v]
            visited[s] = [0]

    for key in road_dict.keys():  # 문제에서 만일 가능한 경로가 2개 이상일 경우 알파벳 순서가 앞서는 경로 return 위해 sort작업처리
        road_dict[key].sort()

    # {'ICN': ['SFO', 'ATL'], 'SFO': ['ATL'], 'ATL': ['ICN', 'SFO']}

    ans.append(start)
    def dfs(start):

        for next_node in road_dict[start]:
            if next_node in road_dict.keys() and visited[next_node][road_dict[next_node].index(road_dict[next_node])] == 0:
                visited[next_node][road_dict[next_node].index(road_dict[next_node])] == 1. [가장 먼 노드]
                dfs(next_node)



    return ans


'''





def solution(tickets):
    def dfs(start, ans):

        for i in range(len(road_dict[start])):
            if road_dict[start][i] not in road_dict.keys():
                ans.append(road_dict[start][i])
                return

            if visited[start][i]:
                continue
            visited[start][i] = 1
            ans.append(road_dict[start][i])
            dfs(road_dict[start][i], ans)


    ans = []
    start = "ICN"
    road_dict = {}  # {'ICN': ['JFK'], 'HND': ['IAD'], 'JFK': ['HND']}
    visited = {}

    for s, v in tickets:
        if s in road_dict:
            road_dict[s].append(v)
            visited[s].append(0)
        else:
            road_dict[s] = [v]
            visited[s] = [0]

    for key in road_dict.keys():  # 문제에서 만일 가능한 경로가 2개 이상일 경우 알파벳 순서가 앞서는 경로 return 위해 sort작업처리
        road_dict[key].sort()
    # {'ICN': ['ATL', 'SFO'], 'SFO': ['ATL'], 'ATL': ['ICN', 'SFO']}

    ans.append(start)  # 인천 출발

    dfs(start, ans)

    return ans



#print(solution([["ICN", "SFO"], ["ICN", "ATL"], ["SFO", "ATL"], ["ATL", "ICN"], ["ATL","SFO"]]))

#print(solution([["ICN", "JFK"], ["HND", "IAD"], ["JFK", "HND"]]))

print(solution([["ICN", "D"], ["D", "ICN"], ["ICN", "B"]]))