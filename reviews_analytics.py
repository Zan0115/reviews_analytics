data = []
with open('reviews.txt', 'r') as file:
    for line in file:
        data.append(line)
print(len(data))