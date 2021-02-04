data = []
count = 0
with open('reviews.txt','r') as f:
	for line in f:
		data.append(line)
		count += 1
		if count % 100000 == 0:
			print(len(data))

print('資料處理中！')
wc = {}
for d in data:
	words = d.split()
	for word in words:
		if word in wc:
			wc[word] += 1
		else:
			wc[word] = 1
print('done')

for word in wc:
	if wc[word] > 1000000:
		print(word, wc[word])
print(len(wc))

while True:
	word = input('請問你想查什麼英文單字: ')
	if word == 'q':
		print('結束查詢!')
		break
	if word in wc:
		print(word, '出現次數為: ', wc[word])
	else:
		print('沒有出現過！')

sum_len = 0
for d in data:
	sum_len += len(d)
print('平均長度為', sum_len/len(data))

new = []
for d in data:
	if len(d) < 100:
		new.append(d)
print('一共有', len(new), '筆留言大於100個字')

#good = []
#for d in data:
#	if 'good' in d:
#		good.append(d)
#print('一共有', len(good), '筆留言包含good')

#以下為快寫法
good = [d for d in data if 'good' in d]
print('一共有', len(good), '筆留言包含good')