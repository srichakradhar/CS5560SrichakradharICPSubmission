import nltk
import spacy
import en_core_web_sm

# The dog saw John in the park
sent = "The dog saw John in the park"
print("Sentence >>> ", sent)
print()
# a.Part-of-speech(POS) tagger
tokens = nltk.word_tokenize(sent)
pos = nltk.pos_tag(tokens)
print("Part-of-speech(POS) tags:\n", pos)
print()
# b.Named entity recognizer (NER)
nlp = en_core_web_sm.load()
doc = nlp(sent)
print("Named entity recognizer (NER):\n", [(X, X.ent_iob_, X.ent_type_) for X in doc])
print()
# c.Co-reference resolution system
# used https://huggingface.co/coref

# The little bear saw the fine fat trout in the rocky brook.
sent = "The little bear saw the fine fat trout in the rocky brook."
print("Sentence >>> ", sent)
print()
# a.Part-of-speech(POS) tagger
tokens = nltk.word_tokenize(sent)
pos = nltk.pos_tag(tokens)
print("Part-of-speech(POS) tags:\n", pos)
print()
# b.Named entity recognizer (NER)
nlp = en_core_web_sm.load()
doc = nlp(sent)
print("Named entity recognizer (NER):\n", [(X, X.ent_iob_, X.ent_type_) for X in doc])
