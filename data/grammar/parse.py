import json
from collections import defaultdict, OrderedDict
from operator import itemgetter
from pprint import pprint


def parse_phrases(path):
    with open(path) as f:
        d = json.load(f)

    prods_rules = defaultdict(list)

    for prod, phrases_dict in d.items():
        for phr, freq in phrases_dict.items():
            prods_rules[phr].append((prod, freq))

    for rule, prods in list(prods_rules.items()):
        prods = [(p, f) for p, f in sorted(prods, key=itemgetter(1), reverse=True)[:50] if f > 50]

        prods_rules[rule] = prods

        for p, f in prods:
            print('%s -> %s [%s]' % (rule, p, f))

        print()

    # pprint(prods_rules)


if __name__ == '__main__':
    # parse_phrases('terminal_rules.json')
    parse_phrases('terminal_rules_sents.json')
