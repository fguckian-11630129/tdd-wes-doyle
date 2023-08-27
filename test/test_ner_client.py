import unittest
from ner_client import NamedEntityClient

class TestNerClient(unittest.TestCase):

    def test_get_ents_returns_dictionary_given_empty_string(self):
        ner = NamedEntityClient()
        ents = ner.get_ents("")
        self.assertIsInstance(ents, dict)

    def test_get_ents_returns_dictionary_given_nonempty_string(self):
        ner = NamedEntityClient()
        ents = ner.get_ents("Hello from Blue River New South Wales")
        self.assertIsInstance(ents, dict)
