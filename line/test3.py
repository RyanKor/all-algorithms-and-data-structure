def solution(program, flag_rules, commands):
    answer = [] # 정답이 되는 boolean 넣기
    temp = [] # commnad를 list 형태로 받기
    flag_lst = [] # flag_rules에 정의된 값들 딕셔너리 형태로 삽입
    
    for cmd in commands: # 1. commands list형태로 만들기
        cmd = list(cmd.split(' '))
        temp.append(cmd)
    for flag in flag_rules:
        flag = flag.split(' ')
        flag_lst.append(flag[0])
    
    for name in temp:
        dic = {} # 각 테스트 케이스마다 딕셔너리 초기화
        if name[0] != program:
            answer.append(False)
            break
        if len(name[1:]) == 1 and name[-1] != 'e':
            answer.append(False)
            break
        else:
            for i in range(0,len(name[1:]), 2): 
                # 어차피 주어진 테스트 케이스 배열의 요소 값이 적기 때문에 2중 배열로 loop를 돌아도 무방하다.
                for j in range(0, len(name[2:]),2):
                    if i != len(name) -1 and name[i] != '-e':
                        dic[name[i]] = name[j]
                    else:
                        dic[name[i]] = None
        print(dic)
        for key, value in dic.items():
            if key == '-n':
                if value.isdigit() != True:
                    answer.append(False)
                break
            if key == '-e':
                if value.isnull() != True:
                    answer.append(False)             
                break
            if key == '-s':
                if value.isalpha() != True:
                    answer.append(False)                      
                break
            else:
                answer.append(True)
                break
    return answer
solution('line', ["-s STRING", "-n NUMBER", "-e NULL"], ["line -n 100 -s hi -e", "lien -s Bye"])
solution('line', ["-s STRING", "-n NUMBER", "-e NULL"], ["line -s 123 -n HI", "line fun"])