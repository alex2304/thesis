import pandas as pd


def get_test_keywords(path):
    df = pd.read_csv(path, header=None)[[0]]

    d_words = df.as_matrix().reshape(df.shape[0])

    d_words = set([p.lower().replace(',', '').strip() for w in d_words for p in w.split(' ')])

    return d_words
