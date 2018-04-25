import json
import os


class Cache:
    grammar_root = os.path.join(os.path.dirname(__file__), '../data/grammar/')

    observed_tags_file_path = os.path.join(grammar_root, 'observed_tags.json')

    @classmethod
    def load_observed_tags(cls):
        if not os.path.exists(cls.observed_tags_file_path):
            return None

        with open(cls.observed_tags_file_path, encoding='utf-8') as f:
            try:
                result = json.load(f)

            except:
                result = None

            return result

    @classmethod
    def save_observed_tags(cls, observed_tags_dict):
        with open(cls.observed_tags_file_path, mode='w', encoding='utf-8') as f:
            json.dump(observed_tags_dict, f)

        return True

    terminal_rules_file_path = os.path.join(grammar_root, 'terminal_rules.json')

    @classmethod
    def load_terminal_rules(cls):
        if not os.path.exists(cls.terminal_rules_file_path):
            return None

        with open(cls.terminal_rules_file_path, encoding='utf-8') as f:
            try:
                result = json.load(f)

            except:
                result = None

            return result

    terminal_rules_sents_file_path = os.path.join(grammar_root, 'terminal_rules_sents.json')

    @classmethod
    def load_terminal_rules_sents(cls):
        if not os.path.exists(cls.terminal_rules_sents_file_path):
            return None

        with open(cls.terminal_rules_sents_file_path, encoding='utf-8') as f:
            try:
                result = json.load(f)

            except:
                result = None

            return result
