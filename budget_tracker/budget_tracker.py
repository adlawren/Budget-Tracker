# TODO
# - Make a DatabaseManager class; move methods from here to it
# - Get transaction list from database
# - Define list of Transaction Categories
# - Iterate over Transaction list, add each to a Transaction Category
# - Render the sums for each Transaction Category
# - Use CLI framework
# - Unit test the database functions
# - Separate unit test module into files for each module under test

from string import whitespace

import csv
import matplotlib.pyplot as plt
import sqlite3

# Local imports
from transaction_record import TransactionRecord
from transaction_record_matcher import TransactionRecordMatcher

CSV_PATH = '/home/al/Sync/statement_cleaned.csv'
DB_PATH = '/home/al/Git-Repos/Budget-Tracker/db/transaction_records.db'
DB_HASH_COLUMN_NAME = 'hash'
DB_TABLE_NAME = 'debit1'
HASH_COLLISION_EXCEPTION_TEXT = f'UNIQUE constraint failed: {DB_TABLE_NAME}.{DB_HASH_COLUMN_NAME}'

def insert_transaction_record(cursor, transaction_record):
    values = (transaction_record.hash(),
              transaction_record.card_no,
              transaction_record.type,
              transaction_record.date,
              transaction_record.amount,
              transaction_record.desc)
    cursor.execute(f'insert into {DB_TABLE_NAME} values(?,?,?,?,?,?);', values)

def import_csv(csv_path):
    try:
        conn = sqlite3.connect(DB_PATH)
        c = conn.cursor()
        with open(csv_path, 'r') as csvfile:
            spamreader = csv.reader(csvfile, delimiter=',')
            for row in spamreader:
                tr = TransactionRecord.parse(row)
                try:
                    insert_transaction_record(c, tr)
                except sqlite3.IntegrityError as e:
                    if HASH_COLLISION_EXCEPTION_TEXT in e.args[0]:
                        print('Warning: failed to insert record due to hash collision: {}'.format(tr.str()))
                        continue
                    else:
                        raise
        conn.commit()
    except Exception as e:
        print('Error occurred: {}'.format(e))
    finally:
        conn.close()

def generate_matcher_list():
    # TODO
    return

def get_category(transaction_record):
    # TODO
    return ''

def render_transactions():
    # TODO
    return

# TODO:
# - Parse command line options
#   - Import csv
#   - display diagram [default]
if __name__ == '__main__':
    print('hi')
    #unittest.main()
    #import_csv(CSV_PATH)

# colors = ['yellow', 'red', 'blue', 'green']
# labels = ['Test1', 'Test2', 'Test3', 'Test4']
# sizes = [1, 2, 3, 4]

# plt.pie(sizes, labels=labels, colors=colors)
# plt.axis('equal')
# plt.show()

#import_csv(CSV_PATH)
