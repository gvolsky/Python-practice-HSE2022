import unittest
from converter import prepare_md_titles

class TestConverter(unittest.TestCase):


    def test_prepare_md_titles(self):
        data = '# title Title\n# description Description'
        title, description = prepare_md_titles(data)
        self.assertEqual(title, 'Title')
        self.assertEqual(description, 'Description')

    def test_prepare_md_titles_with_empty_data(self):
        data = ''
        title, description = prepare_md_titles(data)
        self.assertEqual(title, None)
        self.assertEqual(description, None)

    def test_prepare_md_titles_with_extra_data(self):
        data = '# title Title\n# description Description\n# Body'
        title, description = prepare_md_titles(data)
        self.assertEqual(title, 'Title')
        self.assertEqual(description, 'Description')


if __name__ == "__main__":
    unittest.main()
