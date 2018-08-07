def max_distance(word, dic):
    m = 1
    i = -1
    d = -1
    r = -1
    l_word = len(word) + 1
    l_dic = len(dic) + 1
    A = [[0 for k in range(l_word)] for j in range(l_dic)]
    A[0][0] = 0
    max_distance = 0
    for k in range(l_word):
        A[0][k] = 0
    for j in range(l_dic):
        A[j][0] = 0
    for j in range(1, l_dic):
        for k in range(1, l_word):
            if word[k - 1] == dic[j - 1]:
                A[j][k] = max(0, A[j][k - 1] + d, A[j - 1][k] + i, A[j - 1][k - 1] + m)
            else:
                A[j][k] = max(0, A[j][k - 1] + d, A[j - 1][k] + i, A[j - 1][k - 1] + r)
            if A[j][k] > max_distance:
                max_distance = A[j][k]
    return max_distance


misspell = []
dictionary = []
with open('data/misspell.txt', 'r') as f1:
    for line in f1.readlines():
        line = line.rstrip('\n')
        misspell.append(line)
with open('data/dictionary.txt', 'r') as f2:
    for line in f2.readlines():
        line = line.rstrip('\n')
        dictionary.append(line)

count = -1
LGD = {}

for each_word in misspell:
    prediction = []
    count += 1
    max_dist = -1000

    for each_dic in dictionary:
        max_dist_temp = max_distance(each_word, each_dic)
        if max_dist_temp == max_dist:
            prediction.append(each_dic)
        elif max_dist_temp > max_dist:
            prediction = []#clear all if the max_dist_temp is the biggest for now
            prediction.append(each_dic)
            max_dist = max_dist_temp
    LGD[count] = prediction
    print(count)

    # with open('data/LGD.txt', 'a+') as f3:
    #     f3.write(each_word + ' --' + str(count) + '-- ')
    #     for p in LGD[count]:
    #         # print(p)
    #         f3.write(' '+ p)
    #     f3.write('\n')

#-----------analyse-----------
num_right = 0
correct = []#loading the file for correct word and clean it
with open('data/correct.txt', 'r') as f4:
    for line in f4.readlines():
        line = line.rstrip('\n')
        correct.append(line)
count_c = 0#is the secquence of this word in this file
for each_correct in correct:
    each_correct = each_correct.rstrip('\n')

    for p in LGD.get(count_c):
        if p==each_correct:
            num_right += 1
        count_c +=1
sum_predict = 0#total number of Predicted Word
for value in LGD.items():
    sum_predict += len(value)
sum_correct = len(LGD)
precision = 0.0000
recall = 0.0000
precision = num_right/sum_predict
recall = num_right/sum_correct
print('num_right: ',num_right,'sum_correct: ',sum_correct,'sum_predict: ',sum_predict,
      'precision: ',precision, 'recall: ',recall)
#print(num_right)

# for key, value in LGD.items():
#     print(key, ':', value)
#

