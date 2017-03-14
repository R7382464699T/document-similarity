import pandas as pd
import numpy as np
import sys
from random import randrange

class LSH():

    def __init__(self, n_features, n_minhash=20):
        a_hash = [randrange(sys.maxint) for _ in range(n_minhash)]
        b_hash = [randrange(sys.maxint) for _ in range(n_minhash)]
        self.n_features = n_features
        self.hashes = [lambda(x): np.sum(np.dot(a, x) + b) % n_features for a, b in zip(a_hash, b_hash)]
        self.df = pd.DataFrame(columns=['minhash_{}'.format(i + 1) for i in range(n_minhash)])

    def insert_document(self, v_doc):
        if len(v_doc) != self.n_features:
            raise ValueError("Expected size {}".format(self.n_features))
        index = len(self.df)
        values = [fn_hash(v_doc) for fn_hash in self.hashes]
        self.df.loc[index] = values
        return index

    def get_similarities(self):
        n_docs = len(self.df)
        result = pd.DataFrame(columns=['document_{}'.format(i+1) for i in range(n_docs)])
        for actual_doc in range(n_docs):
            v_actual = self.df.loc[actual_doc]
            result['document_{}'.format(actual_doc + 1)] = [(np.sum(v_actual == self.df.loc[doc2]) / self.n_features) for doc2 in range(n_docs)]
        return result

