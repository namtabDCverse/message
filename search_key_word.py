#算總字數
data = []
count = 0
with open('reviews.txt','r') as message:
	for line in message:
		data.append(line)
		count += 1
		if count % 10000 == 0:
			print(len(data))

#計算字出現數目
word_dic = {}
for d in data:
	words = d.split()
	for word in words:
		if word in word_dic:
			word_dic[word] += 1
		else:
			word_dic[word] = 1
print(len(word_dic))

for word in word_dic:
	if word_dic[word] > 10000:
		print(word, word_dic[word])
	
#找關鍵字
while True:
	word = input("請輸入單字:")
	if word == '/':
		break
	elif word in word_dic:
		print(word,'共出現',word_dic[word],'次')
	else:
		print(word,'共出現0次')
print('感謝使用本系統')
