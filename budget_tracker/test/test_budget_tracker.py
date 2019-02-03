import unittest

from ..transaction_record import TransactionRecord
from ..transaction_record_matcher import TransactionRecordMatcher

class TestTransactionRecord(unittest.TestCase):
    def setUpTransactionRecord(self):
        mock_csv_row = [
            '1234567890123456',
            'TYPE',
            '20180113',
            '12.34',
            'Mock description'
        ]
        self.transaction_record = TransactionRecord.parse(
            mock_csv_row)
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

class TestTransactionMatcher(unittest.TestCase):
    def setUpTransactionRecord(self):
        mock_csv_row = [
            '1234567890123456',
            'TYPE',
            '20180113',
            '12.34',
            'Mock description'
        ]
        self.transaction_record = TransactionRecord.parse(
            mock_csv_row)
    def setUpTransactionRecordMatcher(self):
        json_string = """
        {
            "category": "TEST_CATEGORY",
            "desc": "Mock description"
        }
        """
        self.transaction_record_matcher = TransactionRecordMatcher(
            json_string)
    def setUpNonmatchingTransactionRecordMatcher(self):
        json_string = """
        {
            "category": "TEST_CATEGORY",
            "desc": "Other mock description"
        }
        """
        self.nonmatching_transaction_record_matcher = TransactionRecordMatcher(
            json_string)
    def setUp(self):
        self.setUpTransactionRecord()
        self.setUpTransactionRecordMatcher()
        self.setUpNonmatchingTransactionRecordMatcher()
    def test_safe_call_should_return_none(self):
        self.assertEqual(
            self.transaction_record_matcher.safe_call(
                None, str), None)
    def test_safe_call_should_return_string(self):
        self.assertEqual(
            self.transaction_record_matcher.safe_call(
                1.1, str), '1.1')
    def test_safe_call_should_return_float(self):
        self.assertTrue(
            self.transaction_record_matcher.safe_call(
                '1.1', float), 1.1)
    def test_safe_compare_should_return_true_when_first_param_none(self):
        self.assertTrue(
            self.transaction_record_matcher.safe_compare(
                None, '123'))
    def test_safe_compare_should_return_true_when_second_param_none(self):
        self.assertTrue(
            self.transaction_record_matcher.safe_compare(
                '123', None))
    def test_safe_compare_should_return_true_when_params_equal(self):
        self.assertTrue(
            self.transaction_record_matcher.safe_compare(
                '123', '123'))
    def test_safe_compare_should_return_false_when_params_unequal(self):
        self.assertFalse(
            self.transaction_record_matcher.safe_compare(
                '123', '321'))
    def test_match_should_return_true(self):
        return self.assertTrue(
            self.transaction_record_matcher.match(
                self.transaction_record))
    def test_match_should_return_false(self):
        return self.assertFalse(
            self.nonmatching_transaction_record_matcher.match(
                self.transaction_record))

if __name__ == '__main__':
    unittest.main()
