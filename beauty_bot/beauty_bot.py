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
        message = 'hello'
        message_attachments = [
            {
                "fallback": "Upgrade your Slack client to use messages like these.",
                "color": "#3AA3E3",
                "attachment_type": "default",
                "callback_id": "menu_options_2319",
                "actions": [
                    {
                        "name": "games_list",
                        "text": "Pick a game...",
                        "type": "select",
                        "data_source": "external"
                    }
                ]
            }
        ]
        return message, message_attachments


def main():
    lu = LanguageUnderstanding()
    lu.test()
    dm = DialogueManagement()
    dm.test()
    nlg = NaturalLanguageGeneration()
    nlg.test()


if __name__ == '__main__':
    main()
