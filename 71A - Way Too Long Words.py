# '''
# 71A - Way Too Long Words
# '''
words = int(input())
all_words = []

for word in range(words):
    temp = input()
    all_words.append(temp)

# # print(all_words)
# all_words = ['word', 'localization', 'internationalization', 'pneumonoultramicroscopicsilicovolcanoconiosis']

for i in range(len(all_words)):
    if len(all_words[i]) > 10:
        temp = all_words[i]
        all_words[i] = temp[0] + str(len(temp[1:-1])) + temp[-1]

    print(all_words[i])