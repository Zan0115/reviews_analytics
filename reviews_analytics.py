import time
import progressbar 

data = []
count = 0
bar = progressbar.ProgressBar(max_value=1000000)
with open('reviews.txt', 'r') as file:
    for line in file:
        data.append(line)
        count += 1
        bar.update(count) # 使用第三方套件(讀取進度條)
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

good = []
for ele in data:
    if 'good' in ele:
        good.append(ele)
print('共有', len(good), '筆提到good的留言')

# 文字計數
start_time = time.time()
wc = {} # word_count
for d in data:
    words = d.split(' ')
    for word in words:
        if word in wc:
            wc[word] += 1 # 該字的count +1
        else:
            wc[word] = 1 # 新增新的key進wc字典
end_time = time.time()
print('花了', end_time - start_time, 'seconds')

# 印出出現過1000000次的單字
for word in wc:
    if wc[word] > 1000000:
        print(word, wc[word])

# 查詢某字出現過的次數
while True:
    word = input('請問你想查什麼字? : ')
    if word == 'q':
        break
    if word in wc:
        print(word, '出現過的次數為 :', wc[word])
    else:
        print('這個字沒有出現過哦')