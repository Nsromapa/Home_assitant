from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer
from nltk import pos_tag
from nltk.corpus import wordnet
from collections import defaultdict
from sklearn.feature_extraction.text import TfidfVectorizer
import pandas as pd

#Reading dataset
data = pd.read_csv('data1.csv')


#creating instances
vectorizer = TfidfVectorizer()
stop_words = stopwords.words('english')
lemmatizer = WordNetLemmatizer()

tag_map = defaultdict(lambda: wordnet.NOUN)
tag_map['J'] = wordnet.ADJ
tag_map['V'] = wordnet.VERB
tag_map['R'] = wordnet.ADV


def lemmatize(tokenized_list):
    new_list = []
    for (word, tag) in pos_tag(tokenized_list):
        text = lemmatizer.lemmatize(word, tag_map[tag[0]])
        new_list.append(text)
    return new_list

vectorizer.fit(data['statement'])

def input_process(text):
    text = word_tokenize(text)
    a_1 =[]
    for w in text:
        if w.lower() not in stop_words:
            a_1.append(w.lower())
    text = []
    for x in a_1:
        if x.isalpha():
            text.append(x)
    user_input = [str(lemmatize(text))]
    user_input = vectorizer.transform(user_input)
    
    return user_input