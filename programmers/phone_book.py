def solution(phone_book):
    answer = True
    # phone_book.sort(key=lambda x: len(x))
    # for i in range(len(phone_book)):
    #     for j in range(i+1, len(phone_book)):
    #         if phone_book[i] == phone_book[j][:len(phone_book[i])] or phone_book[j] in phone_book[i][:len(phone_book[j])]:
    #             answer =False
    #         else:
    #             continue  
    phone_book.sort() # 여기서 문자열 길이에 따라 정렬하는 값은 틀림
    for s1,s2 in zip(phone_book,phone_book[1:]):
        if s2.startswith(s1):
            answer = False
    return answer