import csv
import sqlite3

from transaction_record import TransactionRecord

DB_HASH_COLUMN_NAME = 'hash'
DB_TABLE_NAME = 'debit1'
HASH_COLLISION_EXCEPTION_TEXT = f'UNIQUE constraint failed: {DB_TABLE_NAME}.{DB_HASH_COLUMN_NAME}'


class TransactionRecordDatabaseManager:
    @staticmethod
    def insert_transaction_record(cursor, transaction_record):
        values = (transaction_record.hash(), transaction_record.card_no,
                  transaction_record.type, transaction_record.date,
                  transaction_record.amount, transaction_record.desc)
        cursor.execute(f'insert into {DB_TABLE_NAME} values(?,?,?,?,?,?);',
                       values)

    @staticmethod
    def import_csv(db_path, csv_path):
        try:
            conn = sqlite3.connect(db_path)
            c = conn.cursor()
            with open(csv_path, 'r') as csvfile:
                spamreader = csv.reader(csvfile, delimiter=',')
                for row in spamreader:
                    tr = TransactionRecord.parse(row)
                    try:
                        TransactionRecordDatabaseManager.insert_transaction_record(
                            c, tr)
                    except sqlite3.IntegrityError as e:
                        if HASH_COLLISION_EXCEPTION_TEXT in e.args[0]:
                            print(
                                'Warning: failed to insert record due to hash collision: {}'
                                .format(tr.str()))
                            continue
                        else:
                            raise
                    conn.commit()
        except Exception as e:
            print('Error occurred: {}'.format(e))
        finally:
            conn.close()

    @staticmethod
    def get_current_month(cursor):
        row = cursor.execute(
            f'select * from {DB_TABLE_NAME} order by date desc limit 1;'
        ).fetchone()
        newest_transaction_record = TransactionRecord(row[1:])
        newest_transaction_record_year = newest_transaction_record.date[0:4]
        newest_transaction_record_month = newest_transaction_record.date[4:6]
        if newest_transaction_record_month == '01':
            # Wrap year
            return f'{int(newest_transaction_record_year) - 1}12'
        else:
            updated_month = str(int(newest_transaction_record_month) - 1)
            padded_updated_month = updated_month if len(
                updated_month) is 2 else f'0{updated_month}'
            return f'{newest_transaction_record_year}{padded_updated_month}'

    @staticmethod
    def get_transaction_records(db_path):
        conn = sqlite3.connect(db_path)
        c = conn.cursor()
        current_month = TransactionRecordDatabaseManager.get_current_month(c)
        date_lower_limit = f'{current_month}00'
        date_upper_limit = f'{current_month}99'
        transaction_record_list = []
        for row in c.execute(
                f'select * from {DB_TABLE_NAME} where date > ? and date < ? order by date desc;',
            (date_lower_limit, date_upper_limit)):
            transaction_record_list.append(TransactionRecord(row[1:]))
        return transaction_record_list
