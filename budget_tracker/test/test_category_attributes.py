import unittest

from ..category_attributes import CategoryAttributes

class TestCategoryAttributes(unittest.TestCase):
    def setUpCategoryAttributes(self):
        self.category_attributes = CategoryAttributes('category1', { 'color' : 'red' })
    def setUpUnshownCategoryAttributes(self):
        self.unshown_category_attributes = CategoryAttributes('category2', { 'color' : 'red', 'show': False })
    def setUp(self):
        self.setUpCategoryAttributes()
        self.setUpUnshownCategoryAttributes()
    def test_show_should_be_true_by_default(self):
        self.assertTrue(self.category_attributes.show)
    def test_show_should_be_read_from_attributes(self):
        self.assertFalse(self.unshown_category_attributes.show)

if __name__ == '__main__':
    unittest.main()
