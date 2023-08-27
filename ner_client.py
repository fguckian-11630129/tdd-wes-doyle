import spacy

class NamedEntityClient:
    def __init__(self):
        self.model = spacy.load("em_core_web_sm")

    def get_ents(self, sentenct):
        return {}