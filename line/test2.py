import re
from collections import Counter
from string import ascii_lowercase, ascii_uppercase

def solution(inp_str): # inp_str -> str / '[^A-Za-z0-9~!@#$%\\^&*]'
    answer = []
    condition_2 = re.findall('[^A-Za-z0-9~!@#$%\\^&*]', inp_str)
    condition_3 = set(inp_str)
    condition_5 = Counter(inp_str)
    # 3번 규칙 해소를 위한 값 설정
    num = [str(i) for i in range(10)]
    cap_alpha = list(ascii_uppercase)
    small_alpha = list(ascii_lowercase)
    if len(inp_str) <8 or len(inp_str) > 15: # 조건 1
        answer.append(1)
    if condition_2: # 조건 2
        answer.append(2)
    # 조건 3
    cnt = 0
    for i in condition_3:
        if i in num:
            cnt +=1
        elif i in cap_alpha:
            cnt +=1
        elif i in small_alpha:
            cnt +=1
        elif i in '~!@#$%\\^&*':
            cnt +=1
        else:
            continue
    if cnt <3:
        answer.append(3)
            
    # 조건 4
    if len(inp_str) > 3:
        for i in range(len(inp_str)):
            for j in range(i+4, len(inp_str)):
                if len(set(inp_str[i:j])) == 1:
                    answer.append(4)
                    break
            if 4 in answer:
                break
    # 조건 5
    for key, value in condition_5.items():
        if value > 4:
            answer.append(5)
        break
    # 예외 처리
    if answer == []:
        answer.append(0)
    return answer