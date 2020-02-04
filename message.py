#算總字數
data = []
count = 0
with open('reviews.txt','r') as message:
	for line in message:
		data.append(line)
		count += 1
		if count % 10000 == 0:
			print(len(data))
print('共',len(data),'筆資料')

#每筆留言平均長度
sum_len = 0
for d in data:
	sum_len += len(d)
print('留言平均長度:', sum_len / len(data))