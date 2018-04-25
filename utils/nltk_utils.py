from nltk import WordNetLemmatizer, SnowballStemmer, \
    RegexpTokenizer
from nltk.corpus import wordnet as wn
from nltk.corpus.reader import NOUN


def is_wordnet_tag(tag):
    return tag in [wn.ADJ, wn.ADV, wn.VERB, wn.NOUN]


def is_noun(tag):
    return tag in ['NN', 'NNS', 'NNP', 'NNPS']


def is_verb(tag):
    return tag in ['VB', 'VBD', 'VBG', 'VBN', 'VBP', 'VBZ']


def is_adverb(tag):
    return tag in ['RB', 'RBR', 'RBS']


def is_adjective(tag):
    return tag in ['JJ', 'JJR', 'JJS']


def penn_to_wn(tag: str):
    if is_wordnet_tag(tag):
        return tag
    elif is_adjective(tag):
        return wn.ADJ
    elif is_noun(tag):
        return wn.NOUN
    elif is_adverb(tag):
        return wn.ADV
    elif is_verb(tag):
        return wn.VERB

    # noun by default
    return wn.NOUN


class Lemmatizer(WordNetLemmatizer):
    _exceptions = {
        'at': 'at',
        'as': 'as'
    }

    def __init__(self):
        super().__init__()

    def lemmatize(self, word, pos=NOUN):
        exc = self._exceptions.get(word)
        if exc is not None:
            return exc
        else:
            return super().lemmatize(word, penn_to_wn(pos))


# TreebankWordTokenizer
class Tokenizer(RegexpTokenizer):
    _regexp = '\w+|\S|[!?.]+|\'[dst]'

    def span_tokenize(self, s):
        raise NotImplementedError()

    def __init__(self):
        super().__init__(self._regexp)

    def tokenize(self, text):
        return super().tokenize(text)

    def tokenize_sents(self, strings):
        return super().tokenize_sents(strings)


class Stemmer(SnowballStemmer):
    def __init__(self):
        super().__init__('english', ignore_stopwords=True)

    def stem(self, token):
        return super().stem(token)


class Parser:
    _delimiters = [',', ':', ';', '(', ')', '"', '\'', '.', '?', '!', '-']
    _paired_delimiters = [('(', ')'), ('\'', '\''), ('"', '"')]

    def parse_tokens(self, tokens):
        indexes = []
        last_index = 0

        for i, t in enumerate(tokens):
            if t in self._delimiters:
                if last_index < i:
                    indexes.append(list(range(last_index, i)))
                last_index = i + 1

        if last_index < len(tokens):
            indexes.append(list(range(last_index, len(tokens))))

        return indexes

    def parse_sents_tokens(self, sents_tokens):
        return [self.parse_tokens(s) for s in sents_tokens]
