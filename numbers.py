# 產生一個隨機整數1-100
# 讓使用者重複輸入數字去猜
# 猜對的話 印出"終於猜對了!"
# 猜錯的話 要告訴他比答案大或少
import random
answer = random.randint (1, 100)
while True:
	num = input ('請猜數字? ')
	num = int(num)
	if num == answer:
		print ('終於猜對了')
		break
	elif num > answer:
		print ('數字比較小啊! ')
	elif num < answer:
		print ('數字比較大啊! ')