
import numpy as np

text = open('alllines.txt', encoding='utf8').read()
c = text.split()
sentence = [np.random.choice(c)] #gotta start somewhere #chose random because diff outputs everytime
n_words = 20
words = {}

def pairs(c):
    for i in range(len(c)-1):
        yield (c[i], c[i+1])
    
pairs = pairs(c)
for fst, snd in pairs:
    if fst in words.keys():
        words[fst].append(snd)
    else:
        words[fst]=[snd]

def create_sentence():
    for i in range(n_words):
        sentence.append(np.random.choice(words[sentence[-1]]))
        ' '.join(sentence)

create_sentence()

print(sentence)
print(' '.join(s for s in sentence))

#when we cannot observe the state themselves but only the result of a probability fn of the states, we utilize HMM.
#The system being modeled is assumed to be a Markov process with unobserved hidden states.
#Three important questions in HMM are
#    What is the probability of an observed sequence?
#    What is the most likely series of states to generate an observed sequence?
#    How can we learn the values for the HMMs parameters A and B given some data?
