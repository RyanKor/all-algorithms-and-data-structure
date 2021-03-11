'''
※ SW expert 아카데미의 문제를 무단 복제하는 것을 금지합니다.

 

카드 유효기간은 대개 월(01에서 12)과 년도 뒤 두자리(2021년이면 21)의 순서대로 나타나는데, 예를 들어 2021년 7월은 0721로 나타낸다.
그러나 가끔 년, 월 순서대로, 2107을 유효기간으로 표시하는 곳도 있다. 이 때, 전자를 MMYY표기, 후자를 YYMM표기라고 하자.

 

21은 1월에서 12월일 수 없기 때문에 0721은 MMYY표기라는 것을 알 수 있다.
하지만 2007년 5월을 예로 들었다면, 어떤 사람들은 이 날의 MMYY표기 0507를 YYMM표기로 받아들여 2005년 7월이라고 해석할 수 있다.

 

어떤 유효기간 표기 네 자리가 주어질 때, 이 유효기간이 어떤 표기로 나타낸 기간인지 판별하는 프로그램을 작성하라.

 

 

[입력]

첫 번째 줄에 테스트 케이스의 수 가 주어진다. 각 테스트 케이스의 첫 번째 줄에는 네 자리 아라비아 숫자로 이루어진 문자열이 주어진다.

 

 

[출력]

각 테스트 케이스마다 주어진 표기가 MMYY표기와 YYMM표기가 둘 다 될 수 있다면 “AMBIGUOUS”를, MMYY표기만 될 수 있다면 “MMYY”를, YYMM표기만 될 수 있다면 “YYMM”을, 둘 중 어떤 표기로도 나올 수 없다면 “NA”를 출력하라.
'''

T = int(input())

for test_case in range(1, T+1):
    case = input()
    if int(case[:2]) < 13 and  int(case[2:]) < 13:
        print('#{}'.format(test_case), 'AMBIGUOUS')
    elif int(case[:2]) < 13 and  int(case[2:]) > 12:
        print('#{}'.format(test_case), 'MMYY')
    elif int(case[:2]) > 12 and  int(case[2:]) < 13:
        print('#{}'.format(test_case), 'YYMM')
    else:
        print('#{}'.format(test_case), 'NA')