from rtmbot import RtmBot
from rtmbot.core import Plugin
import re
import random
import secret

response = ["안냥", "웅 앵 냥", "야옹야옹", "냥?", "나는귀엽냥", ":cat: :cat: :cat:", "너 내집사가 돼랑"]
random_response = random.sample(response, 1)[0]

class HelloPlugin(Plugin):
    def process_message(self,data):
        if re.match(r'.*냥.*', data["text"]):
            self.outputs.append([data["channel"], random_response)

config = {
    "SLACK_TOKEN": secret.SLACK_TOKEN,
    "ACTIVE_PLUGINS": ["main.HelloPlugin"]
}
bot = RtmBot(config)
bot.start()


print("안냥")
print("웅 앵 냥")
print("야옹야옹")
print("냥?")
print("나는귀엽냥")
print(":cat: :cat: :cat:")
