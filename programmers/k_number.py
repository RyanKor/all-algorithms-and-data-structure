def solution(array, commands):
    answer = []
    for arr in commands:
        start = arr[0] - 1
        end = arr[1]
        result = arr[-1] -1
        temp = array[start:end]
        temp.sort()
        answer.append(temp[result])
        

    return answer