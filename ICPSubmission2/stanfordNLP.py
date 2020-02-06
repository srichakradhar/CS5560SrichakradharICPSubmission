import json
from stanfordcorenlp import StanfordCoreNLP

props = {
         'annotators': 'sentiment, ner, pos, coref',
         'pipelineLanguage': 'en',
         'outputFormat': 'json',
         'timeout': 15000,
         }

host = 'http://localhost'
port = 9000
nlp = StanfordCoreNLP(host, port=port, timeout=15000)

# The sentence you want to parse
f = open('SherlockHolmes.txt', 'r')
text = f.read()
f.close()

# POS
print('POS：', nlp.pos_tag(text))

# NER
print('NER：', nlp.ner(text))
print()
# Co-reference resolution system
print("Co-reference resolution:")
result = json.loads(nlp.annotate(text, properties=props))
mentionChain = list(result['corefs'].items())
for num, mentions in mentionChain:
	print(' <-> '.join([mention['text'] for mention in mentions]))
print()
# Sentiment Analysis
print("Sentiment Analysis:")
for s in result["sentences"]:
    print("{}: '{}': {} (Sentiment Value) {} (Sentiment)".format(
        s["index"],
        " ".join([t["word"] for t in s["tokens"]]),
        s["sentimentValue"], s["sentiment"]))

# Close Stanford Parser
nlp.close()
