from chatbot import Chat, register_call
import wikipedia
import duckduckpy
import os
import time
import warnings
import subprocess
import datetime
import sys
from googletrans import Translator
translator = Translator()

if len(sys.argv) < 2:
    print('You need to specify the path to be listed')
    sys.exit()

input = sys.argv[1]
print(input)

warnings.filterwarnings("ignore")

def speak(msg):
    subprocess.call(["./simple-google-tts/simple_google_tts", "en", msg])

def get_time():
    return time.strftime('%l:%M')

def get_date():
    today = datetime.date.today()
    return today.strftime("%b %d %Y")

def get_day():
    today = datetime.date.today()
    return today.strftime("%A")

class MyChat(Chat):
    def converse(self, first_question=None, quit="quit", session_id="general"):
        """
        Conversation initiator
        :type first_question: str
        :param first_question: Start up message
        :type quit: str
        :param quit: Conversation termination command
        :type session_id: str
        :param session_id: Current User session when used for multi user scenario
        :rtype: str
        """
        if first_question:
            self.conversation[session_id].append(first_question)
            message = self.respond(first_question, session_id=session_id)
            x = translator.translate(message, dest='hi')
            print(x.text)
            speak(x.text)

        """ Only for command-line usage
        input_sentence = ""
        while input_sentence != quit:
            # Read Input source
            input_sentence = input("> ")
            if input_sentence:
                self.conversation[session_id].append(input_sentence)
                input_sentence = input_sentence.rstrip("!.")
                message = self.respond(input_sentence, session_id=session_id)
                self.conversation[session_id].append(message)
                # call output function
                print(message)
                speak(message)
        """

@register_call("duckduckgo")
def google_it(q, session_id="general"):
    response = duckduckpy.query(q, container="dict")
    if(len(response["related_topics"]) > 0):
        for result in response["related_topics"]:
            print("Text: "+result["text"])
            print("URL: "+ result["first_url"])
        return "Here's some results from DuckDuckGo"
    else:
        return "No results found"

@register_call("liver")
def spe(query, session_id="general"):
    return: ('ok here you go')
    
@register_call("specific")
def spec(query, session_id="general"):
    query = query.strip()
    specification = {
        "time": get_time(),
        "date": get_date(),
        "day": get_day()
    }
    return specification.get(query, "I have no idea.")


@register_call("whoIs")
def who_is(query, session_id="general"):
    try:
        return wikipedia.summary(query)
    except Exception:
        for new_query in wikipedia.search(query):
            try:
                return wikipedia.summary(new_query)
            except Exception:
                pass
    return "I don't know about "+query

chat = MyChat(os.path.join(os.path.dirname(os.path.abspath(__file__)), "bot.template"))
chat.converse(input)
