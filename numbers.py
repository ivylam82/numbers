# 產生一個隨機整數1-100
# 讓使用者重複輸入數字去猜
# 猜對的話 印出"終於猜對了!"
# 猜錯的話 要告訴他比答案大或少
import random
start = input ('請決定隨機數字的開始值? ')
end = input ('請決定隨機數字的結束值? ')
start = int(start)
end = int(start)
answer = random.randint (start, end)
count = 0
while True:
	count = count + 1
	num = input ('請猜數字? ')
	num = int(num)
	if num == answer:
		print ('終於猜對了')
		print ('你猜了', count, '次' )
		break
	elif num > answer:
		print ('數字比較小啊! ')
	elif num < answer:
		print ('數字比較大啊! ')
	print ('你猜了', count, '次' )