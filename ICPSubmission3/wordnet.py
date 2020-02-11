# importing the library
from nltk.corpus import wordnet

# lets use word paint as an exqmple
syns = wordnet.synsets("paint")

# An example of a synset:
print(syns[0].name())
print('\n')
# Just the word:
print(syns[0].lemmas()[0].name())
print('\n')

# Definition of that first synset:
print(syns[0].definition())
print('\n')
# Examples of the word in use in sentences:
print(syns[0].examples())
print('\n')

# synonyms and antonyms using wordnet using word
synonyms = []
antonyms = []

for syn in wordnet.synsets("good"):
    for l in syn.lemmas():
        synonyms.append(l.name())
        if l.antonyms():
            antonyms.append(l.antonyms()[0].name())
print('The synonyms of good are: ')
print(set(synonyms))
print('\n')
print('The antonyms of good are: ')
print(set(antonyms))
print('\n')



# comparison/ similarity score between 2 words
w1 = wordnet.synset('ship.n.01')
w2 = wordnet.synset('boat.n.01') # n denotes noun
print("The similarity score betwee ship and boat is =",w1.wup_similarity(w2))