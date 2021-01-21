word = input()
cnt = 0
for i in word:
    print([int(str(int(i)*10000)[:5-cnt])])
    cnt += 1
