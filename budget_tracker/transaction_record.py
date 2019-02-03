import hashlib

class TransactionRecord:
    @staticmethod
    def parse(csv_row):
        return TransactionRecord(csv_row)
    def __init__(self, csv_row):
        self.card_no = csv_row[0].strip()
        self.type = csv_row[1].strip()
        self.date = csv_row[2].strip()
        self.amount = float(csv_row[3])
        self.desc = csv_row[4].strip()
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
