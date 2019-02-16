from nltk.tokenize import RegexpTokenizer
from stop_words import get_stop_words
from nltk.stem.porter import PorterStemmer
from gensim import corpora, models
import os, json
import HTMLParser
import gensim

from HTMLParser import HTMLParser

class MLStripper(HTMLParser):
    def __init__(self):
        self.reset()
        self.fed = []
    def handle_data(self, d):
        self.fed.append(d)
    def get_data(self):
        return ''.join(self.fed)

def strip_tags(html):
    s = MLStripper()
    s.feed(html)
    return s.get_data()

cwd = os.getcwd()
directory = os.path.join(cwd, "parser")
os.chdir(directory)

doc_set = []

for filename in os.listdir(directory):
    if filename.endswith(".json"): 
        print filename
        with open(filename, 'r') as f:
            data = json.load(f)
            doc_set.append(strip_tags(data["content"]))
        # f = open(filename, "r")
        # datax = json.loads(f.read())
        # print(json.dumps(datax, indent=4))
        continue
    else:
        continue

tokenizer = RegexpTokenizer(r'\w+')

# create English stop words list
en_stop = get_stop_words('en')

# Create p_stemmer of class PorterStemmer
p_stemmer = PorterStemmer()
    
# create sample documents
# doc_a = "Brocolli is good to eat. My brother likes to eat good brocolli, but not my mother."
# doc_b = "My mother spends a lot of time driving my brother around to baseball practice."
# doc_c = "Some health experts suggest that driving may cause increased tension and blood pressure."
# doc_d = "I often feel pressure to perform well at school, but my mother never seems to drive my brother to do better."
# doc_e = "Health professionals say that brocolli is good for your health." 

# compile sample documents into a list


# list for tokenized documents in loop
texts = []

# loop through document list
for i in doc_set:
    
    # clean and tokenize document string
    raw = i.lower()
    tokens = tokenizer.tokenize(raw)

    # remove stop words from tokens
    stopped_tokens = [i for i in tokens if not i in en_stop]
    
    # stem tokens
    stemmed_tokens = [p_stemmer.stem(i) for i in stopped_tokens]
    
    # add tokens to list
    texts.append(stopped_tokens)

# turn our tokenized documents into a id <-> term dictionary
dictionary = corpora.Dictionary(texts)
    
# convert tokenized documents into a document-term matrix
corpus = [dictionary.doc2bow(text) for text in texts]

# generate LDA model
ldamodel = gensim.models.ldamodel.LdaModel(corpus, num_topics=15, id2word = dictionary, passes=20)
for i in ldamodel.print_topics(num_topics=15, num_words=10):
    print i
