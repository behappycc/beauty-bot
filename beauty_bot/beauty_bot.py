from pymongo import MongoClient
from database_management import PixnetDatabase
DB_IP = "35.194.174.101"  # 35.194.174.101
DB_PORT = 27017  # default MongoDB port
DB_NAME = "beautybot"  # use the collection
class BeautyBot(object):
    def __init__(self):
        pass
    
    def chat(self, input):
        client = MongoClient(DB_IP, DB_PORT)
        collection_pixnet = client[DB_NAME]["pixnet"]
        collection_ptt = client[DB_NAME]["ptt"]
        p_db = PixnetDatabase()
        if "唇膏" in input:
            if "霧面" in input:
                search_rule = {"category": "lips", "title": {"$regex": "霧面"}}

                article_list = p_db.search_article(collection_pixnet, search_rule)
                pick_pixnet_article_title = [art['title'][:20] + "..." for art in article_list[:3]]
                list_array = ", \n".join(pick_pixnet_article_title)

                ptt_article = p_db.search_article(collection_ptt, search_rule)
                push = sum([art['message_push'] for art in ptt_article[:3]])
                total = sum([art['message_all'] for art in ptt_article[:3]])
                rating = push / total
                pick_ptt_article_title = [art['title'][:20]+"..." for art in ptt_article[:3]]
                ptt_array = ", \n".join(pick_ptt_article_title)

                message = '找到 ' + str(len(article_list)) + ' 篇文章, 前三推荐：\n' + list_array
                message += 'ptt 找到 ' + str(len(ptt_article)) + ' 篇文章, 前三推荐：\n' + ptt_array
                message += '共' + str(total) + '篇回應, 推的比率為' + str(round(rating, 1))
            else:
                message = '你說啥麼？'
        else:
            message = '你說啥麼？'
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
