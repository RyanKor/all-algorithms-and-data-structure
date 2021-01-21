# num = input().split()
# wave_calculator = int(num[0])*int(num[1])*int(num[2])*int(num[3])
# mb_convert = 8*(1024**2)
# print(round(wave_calculator/mb_convert, 1), "MB")


num = input().split()
wave_calculator = int(num[0])*int(num[1])*int(num[2])
mb_convert = 8*(1024**2)

print('%.2f' % (wave_calculator/mb_convert), "MB")
