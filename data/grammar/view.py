import json
from collections import defaultdict
from operator import itemgetter


def view_phrases_file(path):
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


if __name__ == '__main__':
    view_phrases_file('terminal_rules.json')
    view_phrases_file('terminal_rules_sents.json')
