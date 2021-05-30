'''
231A - Team
'''

problems = int(input())
data = []

for i in range(problems):
    temp = input()
    data.append(temp)

# data = ['1 1 0', '1 1 1', '0 0 1']
# print(data)
count = 0
for i in range(len(data)):

    temp = data[i].split()
    print('temp', temp)

    sum = 0

    for i in range(len(temp)):
        sum += int(temp[i])

    if sum>1:
        count += 1

print(count)