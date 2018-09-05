import json
import os


class Cache:
    grammar_root = os.path.join(os.path.dirname(__file__), '../data/grammar/')

    tags_file = os.path.join(grammar_root, 'observed_tags.json')
    phrases_file = os.path.join(grammar_root, 'terminal_rules.json')
    sentences_file = os.path.join(grammar_root, 'terminal_rules_sents.json')

    @classmethod
    def load_observed_tags(cls):
        if not os.path.exists(cls.tags_file):
            return None

        with open(cls.tags_file, encoding='utf-8') as f:
            try:
                result = json.load(f)

            except:
                result = None

            return result

    @classmethod
    def save_observed_tags(cls, observed_tags_dict):
        with open(cls.tags_file, mode='w', encoding='utf-8') as f:
            json.dump(observed_tags_dict, f)

        return True

    @classmethod
    def load_terminal_rules(cls):
        if not os.path.exists(cls.phrases_file):
            return None

        with open(cls.phrases_file, encoding='utf-8') as f:
            try:
                result = json.load(f)

            except:
                result = None

            return result

    @classmethod
    def load_terminal_rules_sents(cls):
        if not os.path.exists(cls.sentences_file):
            return None

        with open(cls.sentences_file, encoding='utf-8') as f:
            try:
                result = json.load(f)

            except:
                result = None

            return result
