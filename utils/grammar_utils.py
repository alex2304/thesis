from typing import Union

sents_tags = ['S']

phrases_tags = ['NP', 'VP', 'PP', 'ADJP', 'ADVP']

pos_tags = ['CC',
            'CD',
            'DT',
            'EX',
            'FW',
            'IN',
            'JJ',
            'JJR',
            'JJS',
            'LS',
            'MD',
            'NN',
            'NNS',
            'NNP',
            'NNPS',
            'PDT',
            'POS',
            'PRP',
            'PRP$',
            'RB',
            'RBR',
            'RBS',
            'RP',
            'SYM',
            'TO',
            'UH',
            'VB',
            'VBD',
            'VBG',
            'VBN',
            'VBP',
            'VBZ',
            'WDT',
            'WP',
            'WP$',
            'WRB']

marks_tags = [',',
              ':',
              ';',
              '.',
              '?',
              '!',
              '-',
              '—']

tags_to_symbols = {
    'PRP$': 'PRPS',
    'WP$': 'WPS',
    ',': 'COMMA',
    '-': 'DASH',
    '—': 'DASH',
    '?': 'QUESTION',
    '!': 'EXCLAM',
    '.': 'DOT',
    ':': 'COLON',
    ';': 'SEMICOLON'
}


# symbols which will be considered as terminals
terminals = marks_tags + pos_tags

# symbols which will be considered as not-terminals
not_terminals = phrases_tags

# rules in which tags not from accepted are faced, will be ignored
accepted_tags = terminals + not_terminals


symbols_to_tags = {symbol: tag
                   for tag, symbol in tags_to_symbols.items()}


def tag_to_symbol(tag):
    return tags_to_symbols.get(tag, tag)


def symbol_to_tag(symbol):
    return symbols_to_tags.get(symbol, symbol)


def symbols_seq_to_tags(symbols_sequence):
    tags = []

    for s in symbols_sequence:
        tag = symbol_to_tag(s)

        if tag not in accepted_tags:
            return tuple()

    return tuple(tags)


def tags_seq_to_symbols(tags_sequence: Union[tuple, list]) -> tuple:
    symbols = []

    for tag in tags_sequence:
        if tag not in accepted_tags:
            return tuple()

        symbols.append(tag_to_symbol(tag))

    return tuple(symbols)
