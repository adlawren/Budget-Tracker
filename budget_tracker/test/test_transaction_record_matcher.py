import unittest

from ..transaction_record import TransactionRecord
from ..transaction_record_matcher import TransactionRecordMatcher


class TestTransactionRecordMatcher(unittest.TestCase):
    def setUpTransactionRecord(self):
        mock_csv_row = [
            '1234567890123456', 'TYPE', '20180113', '12.34', 'Mock description'
        ]
        self.transaction_record = TransactionRecord.parse(mock_csv_row)

    def setUpTransactionRecordMatcher(self):
        attributes = {'category': 'TEST_CATEGORY', 'desc': 'Mock description'}
        self.transaction_record_matcher = TransactionRecordMatcher(attributes)

    def setUpNonmatchingTransactionRecordMatcher(self):
        attributes = {
            'category': 'TEST_CATEGORY',
            'desc': 'Other mock description'
        }
        self.nonmatching_transaction_record_matcher = TransactionRecordMatcher(
            attributes)

    def setUpPartiallyMatchingTransactionRecordMatcher(self):
        attributes = {'category': 'TEST_CATEGORY', 'desc': 'Mock desc'}
        self.partially_matching_transaction_record_matcher = TransactionRecordMatcher(
            attributes)

    def setUp(self):
        self.setUpTransactionRecord()
        self.setUpTransactionRecordMatcher()
        self.setUpNonmatchingTransactionRecordMatcher()
        self.setUpPartiallyMatchingTransactionRecordMatcher()

    def test_safe_equals_should_return_true_when_first_param_none(self):
        self.assertTrue(
            self.transaction_record_matcher.safe_equals(None, '123'))

    def test_safe_contains_should_return_true_when_first_param_none(self):
        self.assertTrue(
            self.transaction_record_matcher.safe_contains(None, '123'))

    def test_safe_equals_should_return_true_when_second_param_none(self):
        self.assertTrue(
            self.transaction_record_matcher.safe_equals('123', None))

    def test_safe_contains_should_return_true_when_second_param_none(self):
        self.assertTrue(
            self.transaction_record_matcher.safe_contains('123', None))

    def test_safe_equals_should_return_true_when_params_equal(self):
        self.assertTrue(
            self.transaction_record_matcher.safe_equals('123', '123'))

    def test_safe_contains_should_return_true_when_first_param_contains_second_param(
            self):
        self.assertTrue(
            self.transaction_record_matcher.safe_contains('12', '123'))

    def test_safe_equals_should_return_false_when_params_unequal(self):
        self.assertFalse(
            self.transaction_record_matcher.safe_equals('123', '321'))

    def test_safe_contains_should_return_false_when_second_param_does_not_contain_first_param(
            self):
        self.assertFalse(
            self.transaction_record_matcher.safe_equals('123', '12'))

    def test_match_should_return_true(self):
        return self.assertTrue(
            self.transaction_record_matcher.match(self.transaction_record))

    def test_match_should_return_false(self):
        return self.assertFalse(
            self.nonmatching_transaction_record_matcher.match(
                self.transaction_record))

    def test_partial_match_should_return_true(self):
        return self.assertTrue(
            self.partially_matching_transaction_record_matcher.match(
                self.transaction_record))


if __name__ == '__main__':
    unittest.main()
