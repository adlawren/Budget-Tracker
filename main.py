# TODO
# - Get transaction list from database
# - Define list of Transaction Categories
# - Iterate over Transaction list, add each to a Transaction Category
# - Render the sums for each Transaction Category

from string import whitespace

import csv
import matplotlib.pyplot as plt
import sqlite3

CSV_PATH = '/home/al/Sync/statement_cleaned.csv'
DB_PATH = '/home/al/Git-Repos/Budget-Tracker/transaction_records.db'

def strip_whitespace(str):
    return str.translate(dict.fromkeys(map(ord, whitespace)))

class TransactionRecord:
    def __init__(self, csv_row):
        self.card_no = strip_whitespace(csv_row[0])
        self.type = strip_whitespace(csv_row[1])
        self.date = strip_whitespace(csv_row[2])
        self.amount = float(csv_row[3])
        self.desc = strip_whitespace(csv_row[4])
    def hash(self):
        # TODO
        return '1234567890123456789012345678901234567890123456789012345678901234'

def parse_transaction_record(csv_row):
    return TransactionRecord(csv_row)

def insert_transaction_record(cursor, transaction_record):
    values = (transaction_record.hash(),
              transaction_record.card_no,
              transaction_record.type,
              transaction_record.date,
              transaction_record.amount,
              transaction_record.desc)
    cursor.execute('insert into debit1 values(?,?,?,?,?,?);', values)

def import_csv(csv_path):
    try:
        conn = sqlite3.connect(DB_PATH)
        c = conn.cursor()
        with open(csv_path, 'r') as csvfile:
            spamreader = csv.reader(csvfile, delimiter=',')
            for row in spamreader:
                tr = parse_transaction_record(row)
                insert_transaction_record(c, tr)
        conn.commit()
    except Exception as e:
        print(e)
    finally:
        conn.close()

# colors = ['yellow', 'red', 'blue', 'green']
# labels = ['Test1', 'Test2', 'Test3', 'Test4']
# sizes = [1, 2, 3, 4]

# plt.pie(sizes, labels=labels, colors=colors)
# plt.axis('equal')
# plt.show()

import_csv(CSV_PATH)
