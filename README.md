# DiscordBot-GPT
## 介紹
自行架設chatGPT功能的Discord機器人。
![image](https://github.com/PHW22/DiscordBot-GPT/assets/116903114/5e79ea32-1971-4cbf-bb21-7f44c893c3f7)
這會使用到OpenAI的API功能，依照[tokens計費](https://openai.com/pricing#language-models)，與個人訂閱制無關。  
不同的付費層級可以使用不同的[模型](https://platform.openai.com/docs/guides/rate-limits?context=tier-free)。


## 步驟
1. 建立 [Discord API](https://discord.com/developers/applications) 金鑰
2. 建立 [OpenAI API](https://openai.com/blog/openai-api) 金鑰
3. 安裝 [discord.py](https://pypi.org/project/discord.py/) 套件和 [openai](https://pypi.org/project/openai/) 套件。(此功能會在主機後台運行，請使用終端機或內建終端機的編輯器)
4. 於`gptbot.py`中輸入Discord API金鑰和OpenAI API金鑰並執行，出現"chatGPT 已啟動"代表成功上線了。
   ![image](https://github.com/PHW22/DiscordBot-GPT/assets/116903114/c1fa8593-8a1c-4fad-b096-2aea686f0211)


