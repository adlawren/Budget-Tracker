import hashlib

class TransactionRecord:
    @staticmethod
    def parse(attribute_list):
        return TransactionRecord(attribute_list)
    def __init__(self, attribute_list):
        self.card_no = attribute_list[0].strip()
        self.type = attribute_list[1].strip()
        self.date = attribute_list[2].strip()
        self.amount = float(attribute_list[3])
        self.desc = attribute_list[4].strip()
    def hash(self):
        m = hashlib.sha256()
        m.update(self.card_no.encode('utf-8'))
        m.update(self.type.encode('utf-8'))
        m.update(self.date.encode('utf-8'))
        m.update(str('%.2f' % self.amount).encode('utf-8'))
        m.update(self.desc.encode('utf-8'))
        return m.digest()
    def str(self):
        return '{0} {1} {2} {3} {4} {5}'.format(self.hash(), self.card_no, self.type, self.date, self.amount, self.desc)
