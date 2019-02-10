# TODO
# - Validate parsed config

import yaml

from category_attributes import CategoryAttributes
from transaction_record_matcher import TransactionRecordMatcher


class CategoryConfigParser:
    @staticmethod
    def get_categories(parsed_yaml):
        category_list = []
        for category_name in parsed_yaml.keys():
            matcher_list = []
            for matcher in parsed_yaml[category_name]['matchers']:
                matcher_list.append(TransactionRecordMatcher(matcher))
            category_list.append({
                'attributes':
                CategoryAttributes(category_name,
                                   parsed_yaml[category_name]['attributes']),
                'matchers':
                matcher_list
            })
        return category_list

    @staticmethod
    def parse_config_file(yaml_path):
        with open(yaml_path) as f:
            parsed_yaml = yaml.safe_load(f)
            category_list = CategoryConfigParser.get_categories(parsed_yaml)
        return category_list
