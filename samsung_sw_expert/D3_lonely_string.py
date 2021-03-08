'''
※ SW expert 아카데미의 문제를 무단 복제하는 것을 금지합니다. 

알파벳 소문자 만으로 이루어진 문자열이 주어진다.

이 문자열에서 같은 두 문자들을 짝짓고 남는 문자가 무엇인지 구하는 프로그램을 작성하라.

같은 문자를 여러 번 짝지어서는 안 된다.
 

[입력]

첫 번째 줄에 테스트 케이스의 수 T가 주어진다.

각 테스트 케이스의 첫 번째 줄에는 알파벳 소문자 만으로 이루어진 문자열이 주어진다.

이 문자열의 길이는 1이상 100이하이다.


[출력]

각 테스트 케이스 마다 예제와 같은 형식으로 남는 문자를 사전 순서대로 출력한다.

만약 어떤 문자도 남지 않는다면 “Good”을 출력하도록 한다.


'''

T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    text = list(input())
    text.sort()
    result = []
    for word in text:
        if result and result[-1] ==word:
            result.pop()
        else:
            result.append(word)

    if not result:
        print('#{}'.format(test_case), 'Good')
    else:
        print('#{}'.format(test_case), ''.join(result))