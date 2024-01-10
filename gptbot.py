# -*- coding: utf-8 -*-
"""
Created on Mon Jan  8 00:36:41 2024

@author: d1a1n
"""

# 導入Discord.py模組
import discord
from openai import OpenAI


# client是跟discord連接，intents是要求機器人的權限
intents = discord.Intents.default()
intents.message_content = True
client = discord.Client(intents = intents)

cli = OpenAI(api_key = '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')

# 調用event函式庫
@client.event
# 當機器人完成啟動
async def on_ready():
    print("chatGPT 已啟動")


@client.event
# 當頻道有新訊息
async def on_message(message):
    # 排除機器人本身的訊息，避免無限循環
    if message.author == client.user:
        return

    if message.content[0:4] == "/gpt":
        response = cli.chat.completions.create(      
            model      = "gpt-3.5-turbo",
            messages   = [{"role": "user", "content": message.content}],
            max_tokens = 1500)
        if response.choices:
            await message.channel.send(response.choices[0].message.content)
        else:
            return
    else:
        return    


    
    
client.run("MTE5MzU4NDM0NzA1NjQ1NTcyMQ.GTZVzz.C89fTcZZjxF6MB0RBAs9OkJp16faDnfOwWNNtA")