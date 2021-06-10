'''
158A - Next Round
By: Ayushi Rawat
'''

keys = input().split()
#print(keys)

scores = []

for i in range(8):
    scores.append(int(input()))
# print(scores)
n, k = 8, 5
score = [10, 9, 8, 7, 7, 7, 5, 5]

count = 0
k = keys[1]
for i in range(keys[0]):
    if score[i] > 0 and score[i] >= score[k]:
        count += 1

print(count)