data = []
count = 0
with open('reviews.txt', 'r') as file:
    for line in file:
        data.append(line)
        count += 1
        if count % 1000 == 0:
            print(len(data))
print('檔案讀取完，共有', len(data), '筆資料')

sum_len = 0
for ele in data:
    sum_len = sum_len + len(ele)
print('留言的平均長度為', sum_len / len(data))

short = []
for ele in data:
    if len(ele) < 100:
        short.append(ele)
print('共有', len(short), '筆長度小於100的留言')
print(short[0])

good = []
for ele in data:
    if 'good' in ele:
        good.append(ele)
print('共有', len(good), '筆提到good的留言')
print(good[0])

# 23~26行 可改寫一行 : good = [d for d in data if 'good' in d]