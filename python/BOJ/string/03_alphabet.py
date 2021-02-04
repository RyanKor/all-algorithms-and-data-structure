import sys
alphabet = sys.stdin.readline().rstrip()

# result = [0] * 27
result = [-1] * 26
english = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l',
           'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

# 알파벳 순서를 출력하는 경우라면, 이렇게 출력한다.
# for word in alphabet:
#     if word in english:
#         result[english.index(word)+1] = english.index(word)+1


# for i in range(1, len(result)):
#     if result[i] == 0:
#         result[i] = -1
#     print(result[i], end=" ")

# 입력한 단어에서의 인덱스 출력

for word in range(len(alphabet)):
    if result[english.index(alphabet[word])] == -1:
        result[english.index(alphabet[word])] = word

for i in result:
    print(i, end=" ")
