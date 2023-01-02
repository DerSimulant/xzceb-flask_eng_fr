import unittest
from translator import english_to_french, french_to_english

class TestTranslator(unittest.TestCase):

    def test_null_inputFE(self):
        # Test translation with null input
        self.assertIsNone(french_to_english(None))

    def test_null_inputEF(self):
        # Test translation with null input
        self.assertIsNone(english_to_french(None))

    def test_englishToFrench(self):
        # Test English to French translation
        english_text = "Hello"
        expected_french_text = "Bonjour"
        self.assertEqual(english_to_french(english_text), expected_french_text)

    def test_frenchToEnglish(self):
        # Test French to English translation
        french_text = "Bonjour"
        expected_english_text = "Hello"
        self.assertEqual(french_to_english(french_text), expected_english_text)


if __name__ == '__main__':
    unittest.main()