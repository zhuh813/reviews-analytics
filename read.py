data = [] #建立空清單叫data
count = 0

with open('reviews.txt', 'r') as f:
	for line in f: #每次讀取(讀f)都是讀取一行 另外令一個變數叫作 "line"
		data.append(line) #把讀取的line存入到list裡面

		#以下當程式每讀取1000行時 才印出'讀取進度'
		count +=1
		if count % 1000 == 0:
			print(len(data))

print('檔案讀取完了, 總共有', len(data),'筆資料') #印出整個清單的長度

#以下算出留言平均長度
sum_len = 0
for d in data:
	sum_len += len(d)

print('留言平均長度',sum_len / len(data),)
	





