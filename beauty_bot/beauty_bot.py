from language_understanding import LanguageUnderstanding
from dialogue_management import DialogueManagement
from natural_language_generation import NaturalLanguageGeneration

class BeautyBot(object):
    def __init__(self):
        pass
    
    def chat(self):
        lu = LanguageUnderstanding()
        lu.test()
        dm = DialogueManagement()
        dm.test()
        nlg = NaturalLanguageGeneration()
        nlg.test()
        return 'hello'


def main():
    lu = LanguageUnderstanding()
    lu.test()
    dm = DialogueManagement()
    dm.test()
    nlg = NaturalLanguageGeneration()
    nlg.test()


if __name__ == '__main__':
    main()
