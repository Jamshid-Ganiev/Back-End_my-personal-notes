import unittest
import cap

class Test_Cap(unittest.TestCase):

    def test_one_word(self):
        text = 'muhammad'
        result = cap.cap_text(text)
        self.assertEqual(result,'Muhammad')
    def test_multiple_words(self):
        text = 'muhammad Allohning rasuli'
        result = cap.cap_text(text)
        self.assertEqual(result,"Muhammad Allohning Rasuli")

if __name__ == '__main__':
    unittest.main()
