import unittest

from ..category_attributes import CategoryAttributes
from ..category_filter import CategoryFilter
from ..transaction_record import TransactionRecord
from ..transaction_record_matcher import TransactionRecordMatcher


class TestCategoryFilter(unittest.TestCase):
    def test_should_filter_categories(self):
        category_list = [{
            'attributes':
            CategoryAttributes('Category 1', {
                'color': 'blue',
                'show': False
            }),
            'matchers': [TransactionRecordMatcher({'type': 'TYPE 2'})]
        },
                         {
                             'attributes':
                             CategoryAttributes('Category 2',
                                                {'color': 'red'}),
                             'matchers':
                             [TransactionRecordMatcher({'desc': 'Test desc'})]
                         },
                         {
                             'attributes':
                             CategoryAttributes('default', {'color': 'green'}),
                             'matchers': [TransactionRecordMatcher({})]
                         }]
        transaction_record_list = [
            TransactionRecord(
                ['1234567890123456', 'TYPE 1', '20180113', 10.0, 'Test desc']),
            TransactionRecord(
                ['1234567890123456', 'TYPE 2', '20180114', 20.0, 'Test desc']),
            TransactionRecord(
                ['1234567890123456', 'TYPE 1', '20180115', 30.0, 'Test desc']),
            TransactionRecord([
                '1234567890123456', 'TYPE 1', '20180115', 40.0,
                'Different test desc'
            ])
        ]
        category_dict = CategoryFilter.filter_categories(
            transaction_record_list, category_list)
        self.assertEqual(len(category_dict), 2)
        self.assertEqual(category_dict['Category 2']['color'], 'red')
        self.assertEqual(category_dict['Category 2']['amount'], 40.0)
        self.assertEqual(category_dict['default']['color'], 'green')
        self.assertEqual(category_dict['default']['amount'], 40.0)
