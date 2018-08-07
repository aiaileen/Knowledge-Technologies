# standard_LD.py

r = 1, i = 1, d = 1, m = 0.

First we read dictionary.txt, misspell.txt, correct.txt in as `dictionary`, `test_word`, `correct_word`.

```python
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
```

Then, for each misspelled word, we use Levenshtein.distance() to get the distance value and sort accordingly.

```python
l = []
for word in dictionary:
    l.append(Word(word, Levenshtein.distance(misspelled_word, word)))
l = sorted(l, key=get_distance, reverse=True)
```

We can then get the top K predicts  and  precision for current correction is calculated as follows:
- precision = (number of correct word in predicts) / (length of predicts)
    `predicts.count(correct_word[i]) / len(predicts)`

In the end, we need to average recall ans calculate precision and recall as: 
- precision = (number of correct word in predicts) / (length of predicts)
    `predicts.count(correct_word[i]) / len(predicts)`
- recall = (number of correct predictions) / (total number of words)
    `corrects / len(test_word)`

# standard_LD.py

it is the same as dictance.py, but parameters change:
r = 2, i = 1, d = 1,m = 0

# SpellingCorrection.py

This implements a self-written Local Edit Distance approach, using dict{} as data structure.

#### It is not used in the report.

I find this method is not suitable for this spelling correction case, as I stated in the report.
I placed this file here is just a proof of my work. 
Cheers.