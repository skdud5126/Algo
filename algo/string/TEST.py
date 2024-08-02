'''
String vs List
공통점
- iterable 하다. 순회 가능하다는 거다. (for loop.)
- String도 List라고 생각하면서 사용하자
- 인덱싱이나 슬라이싱이 가능하다.
( 인덱싱 : 인덱스로 접근. List_example[3] => str_example[3]
  슬라이싱 : 잘라서 부분만 가져옴. list_example[2:3] => str_example[2:3])

- String : immutable(불변), List : mutable(가변)
- String : 각 요소를 변경할 수 없음. 수정하려면 새로운 문자열을 생성해야 한다.
- List : mutable
각 요소를 변경할 수 있음, 수정 시 원본이 수정되나.


# split()
    - 문자열 -> 리스트로 변환을 한다.
    - 파라미터(구분자)를 기준으로 나누어서 리스트에 넣는다.

# join()
    - 리스트 -> 문자열로 반환
    - iterable (반복가능한, 순회가능한) 객체 요소들을 하나의 문자열로 반환


'''

# String : 각 요소를 변경할 수 없다
str_example = 'hello'
# str_example[0] = 'J'

str_example + 'World'





# import sys
# a = ''
# b = 'a'
# c = 'ab'
# d = 'abc'
#
# print(sys.getsizeof((a)))  # 49
# print(sys.getsizeof((b)))  # 50
# print(sys.getsizeof((c)))  # 51
# print(sys.getsizeof((d)))   # 52
#
# s1 = list(input())
# s2 = input()
#
# print(s1)  # ['a', 'b', 'c']
# print(s2)  # abc
#
# s= input()  # abc
#
# print(s[0])  # a
# print(s[1])  # b