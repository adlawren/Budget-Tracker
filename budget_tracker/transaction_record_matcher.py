import json


class TransactionRecordMatcher:
    @staticmethod
    def safe_equals(val1, val2):
        if val1 is None or val2 is None:
            return True
        else:
            return val1 == val2

    @staticmethod
    def safe_contains(val1, val2):
        if val1 is None or val2 is None:
            return True
        else:
            return val1 in val2

    def __init__(self, attributes):
        category = attributes.get('category')
        self.category = category if category is None else category.strip()
        card_no = attributes.get('card_no')
        self.card_no = card_no if card_no is None else card_no.strip()
        type = attributes.get('type')
        self.type = type if type is None else type.strip()
        date = attributes.get('date')
        self.date = date if date is None else date.strip()
        amount = attributes.get('amount')
        self.amount = amount if amount is None else float(amount)
        desc = attributes.get('desc')
        self.desc = desc if desc is None else desc.strip()

    def match(self, transaction_record):
        return (self.safe_equals(self.card_no, transaction_record.card_no)
                and self.safe_equals(self.type, transaction_record.type)
                and self.safe_equals(self.date, transaction_record.date)
                and self.safe_equals(self.amount, transaction_record.amount)
                and self.safe_contains(self.desc, transaction_record.desc))
