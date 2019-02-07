import unittest
import yaml

from ..category_config_parser import CategoryConfigParser

class TestCategoryAttributes(unittest.TestCase):
    def test_should_get_categories(self):
        yaml_string = """
        category1:
          attributes:
            color: 'red'
          matchers:
            - { desc: 'Test 1' }
        category2:
          attributes:
            color: 'blue'
          matchers:
            - { desc: 'Test 2' }
            - { desc: 'Test 3' }
        """
        category_list = CategoryConfigParser.get_categories(
            yaml.load(yaml_string))
        category1_attributes = category_list[0]['attributes']
        self.assertEqual(category1_attributes.name, 'category1')
        self.assertEqual(category1_attributes.color, 'red')
        category1_matchers = category_list[0]['matchers']
        self.assertEqual(len(category1_matchers), 1)
        category2_attributes = category_list[1]['attributes']
        self.assertEqual(category2_attributes.name, 'category2')
        self.assertEqual(category2_attributes.color, 'blue')
        category2_matchers = category_list[1]['matchers']
        self.assertEqual(len(category2_matchers), 2)

if __name__ == '__main__':
    unittest.main()
