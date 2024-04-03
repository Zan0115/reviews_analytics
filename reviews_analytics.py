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