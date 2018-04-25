import traceback
from typing import List, Tuple

from tqdm import tqdm

from utils.grammar_utils import tags_seq_to_symbols
from utils.io import Cache
from utils.ngrams import ngram2str


def parse_phrases(tt_ngrams, n) -> Tuple[List, List[List[Tuple]]]:
    phrases = []
    phrases_types = []

    observed_tags = Cache.load_observed_tags()

    if observed_tags is None:
        observed_tags = dict()

    terminal_rules = Cache.load_terminal_rules()

    for tt_gram in tqdm(tt_ngrams, desc='parsing phrases from %d-grams' % n):
        symbols = tuple(tags_seq_to_symbols([tag
                                             for _, tag in tt_gram]))

        phrase = tt_gram

        # check if tags phrase has been already observed
        tags_str = ngram2str(symbols)

        if tags_str in observed_tags:
            if observed_tags[tags_str] is not None:
                phrases.append(phrase)
                phrases_types.append(observed_tags[tags_str])

            continue

        p_types_dict = terminal_rules.get(tags_str)

        if p_types_dict:
            p_type = max(p_types_dict, key=lambda k: p_types_dict[k])

            phrases.append(phrase)
            phrases_types.append(p_type)

            observed_tags[tags_str] = p_type

        else:
            observed_tags[tags_str] = None

    try:
        Cache.save_observed_tags(observed_tags)

    except Exception as e:
        traceback.print_exc(e)

    return phrases_types, phrases
