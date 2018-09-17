import os
from gensim.models import TfidfModel
from gensim.corpora import Dictionary
import numpy as np
import pickle
from nltk import *

class Summary:
    def __init__(self,doc,**args):
        self.doc = " ".join(doc.split())
        try:
            with open("static/dictionary.pkl","rb") as file:
                self.dct = pickle.load(file)
        except:
            raise("Cannot load the dictionary")

    def summarize(self):
        lines_ = self.doc.split("।")
        words_per_line = [line.split() for line in lines_]
        frq = FreqDist(word for words in words_per_line for word in words)
        freq_list = frq.most_common(300)
        freq_ls = [item[0] for item in freq_list]
        curated_doc = []
        for d in words_per_line:
            temp = []
            for w in d:
                if w not in freq_ls:
                    temp.append(w)
            curated_doc.append(temp)
        corpus = [self.dct.doc2bow(line) for line in curated_doc]
        model = TfidfModel(corpus)
        val = []
        for ind,sent in enumerate(curated_doc):
            tfidf = model[corpus[ind]]
            sm = 0
            for item in tfidf:
                sm+=item[1]
            val.append((ind,sm))
        val = sorted(val,key=lambda t: t[1],reverse=True)
        res = val[0:3]
        summary = ""
        for lines in res:
            summary+=" ".join(words_per_line[lines[0]]) + ' '

        return summary
