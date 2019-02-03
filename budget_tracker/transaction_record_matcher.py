# TODO
# - Deprecate strip_whitespace
# - Abstract json parsing; take an already-parsed json object
import json

class TransactionRecordMatcher:
    @staticmethod
    def strip_whitespace(str):
        #return str.translate(dict.fromkeys(map(ord, whitespace)))
        return str.strip()
    @staticmethod
    def safe_call(param, fn):
        # Return None if param is None, otherwise return fn result
        if param is None:
            return None
        else:
            return fn(param)
    @staticmethod
    def safe_compare(val1, val2):
        if val1 is None or val2 is None:
            return True
        else:
            return val1 == val2
    def __init__(self, json_string):
        parsed_json = json.loads(json_string)
        self.category = self.safe_call(parsed_json.get('category'), self.strip_whitespace)
        self.card_no = self.safe_call(parsed_json.get('card_no'), self.strip_whitespace)
        self.type = self.safe_call(parsed_json.get('type'), self.strip_whitespace)
        self.date = self.safe_call(parsed_json.get('date'), self.strip_whitespace)
        self.amount = self.safe_call(parsed_json.get('amount'), float)
        self.desc = self.safe_call(parsed_json.get('desc'), self.strip_whitespace)
    def match(self, transaction_record):
        return (self.safe_compare(
            self.card_no, transaction_record.card_no)
                and self.safe_compare(
                    self.type, transaction_record.type)
                and self.safe_compare(
                    self.date, transaction_record.date)
                and self.safe_compare(
                    self.amount, transaction_record.amount)
                and self.safe_compare(
                    self.desc, transaction_record.desc))
