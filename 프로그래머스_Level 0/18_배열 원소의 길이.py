# 문제 설명
# 문자열 배열 strlist가 매개변수로 주어집니다. strlist 각 원소의 길이를 담은 배열을 retrun하도록 solution 함수를 완성해주세요.

# 입출력 예
# strlist 	result
# ["We", "are", "the", "world!"] 	[2, 3, 3, 6]
# ["I", "Love", "Programmers."] 	[1, 4, 12]


# def solution(strlist):
#     answer = []
#     for i in strlist:
#         answer.append(len(i))
#     return answer


def solution(strlist):
    answer = []
    for i in strlist:
        answer.append(len(i))
    return answer