# 導入Discord.py模組和openai模組
import discord
from openai import OpenAI


# 預設機器人的權限，機器人可以觀看聊天內容
intents = discord.Intents.default()
intents.message_content = True
client = discord.Client(intents = intents)

#輸入OpenAI API金鑰
cli = OpenAI(api_key = 'GPT_API_金鑰')

# 調用event函式庫
@client.event
# 當機器人完成啟動時告知"chatGPT 已啟動"
async def on_ready():
    print("chatGPT 已啟動")

@client.event
# 偵測到Discord聊天頻道有新訊息
async def on_message(message):
    # 排除機器人本身的訊息，避免無限循環
    if message.author == client.user:
        return
    # message.content為Discord內的新訊息，為了與聊天內容區隔開頭需輸入/gpt
    if message.content[0:4] == "/gpt":
        response = cli.chat.completions.create(      
            model      = "gpt-3.5-turbo",                                 #使用模型                                      
            messages   = [{"role": "user", "content": message.content}],  #向GPT詢問內容
            max_tokens = 1500)                                            #GPT回答token限制
        if response.choices:
            await message.channel.send(response.choices[0].message.content)
        else:
            return
    else:
        return    

#輸入Discord API金鑰    
client.run("Discord_API_金鑰")