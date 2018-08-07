import Levenshtein

dictionary = []

with open('dictionary.txt') as f:
    for word in f:
        dictionary.append(word.strip())

test_word = []
with open('misspell.txt') as f:
    for line in f:
        test_word.append(line.strip())

correct_word = []
with open('correct.txt') as f:
    for line in f:
        correct_word.append(line.strip())

class Word:
    def __init__(self, word, distance):
        self.word = word
        self.distance = distance
    def __str__(self):
        return "{} - {}".format(self.word, self.distance)
    def __repr__(self):
        return "{} - {}".format(self.word, self.distance)

def get_distance(word):
    return word.distance

with open("distance-output.txt", "w") as f:
    pass

corrects = 0
recall = 0
for i, misspelled_word in enumerate(test_word):
    l = []
    for word in dictionary:
        l.append(Word(word, Levenshtein.distance(misspelled_word, word)))
    l = sorted(l, key=get_distance)

    dis = l[0].distance
    predicts = []
    for w in l:
        if w.distance == dis:
            predicts.append(w.word)
        else:
            break
    if correct_word[i] in predicts:
        corrects = corrects + 1
   # accuracy = accuracy + predicts.count(correct_word[i]) / len(predicts)
    #print("{}/{} accuracy: {}".format(i, len(test_word), corrects / (i + 1)))
    #print("{}/{} precision: {}".format(i, len(test_word), predicts.count(correct_word[i]) / len(predicts)))
    with open("distance-output.txt", "a") as f:
        f.write("{} {}\n".format(corrects / (i + 1), predicts.count(correct_word[i]) / len(predicts)))

print("recall: {}".format(corrects / len(test_word)))
print("precision: {}".format(corrects / len(predicts)))
