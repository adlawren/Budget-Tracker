import unittest

from ..transaction_record import TransactionRecord


class TestTransactionRecord(unittest.TestCase):
    def setUpTransactionRecord(self):
        mock_csv_row = [
            '1234567890123456', 'TYPE', '20180113', '12.34', 'Mock description'
        ]
        self.transaction_record = TransactionRecord.parse(mock_csv_row)

    def setUp(self):
        self.setUpTransactionRecord()

    def test_parse_should_set_attributes(self):
        self.assertEqual(self.transaction_record.card_no, '1234567890123456')
        self.assertEqual(self.transaction_record.type, 'TYPE')
        self.assertEqual(self.transaction_record.date, '20180113')
        self.assertEqual(self.transaction_record.amount, 12.34)
        self.assertEqual(self.transaction_record.desc, 'Mock description')

    def test_hash_should_return_32_character_string(self):
        self.assertEqual(len(self.transaction_record.hash()), 32)


if __name__ == '__main__':
    unittest.main()
