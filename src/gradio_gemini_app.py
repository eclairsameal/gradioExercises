import configparser
import os
import google.generativeai as genai
import gradio as gr
from PIL import Image
import time
from typing import List, Tuple, Optional

# 獲取當前腳本的目錄
script_dir = os.path.dirname(os.path.realpath(__file__))
# 使用相對路徑組合出配置文件的路徑
config_path = os.path.join(script_dir, "../config.ini")

config = configparser.ConfigParser()
config.read(config_path)

# 從配置文件中讀取 Google API 金鑰
GOOGLE_API_KEY = config["DEFAULT"]["GOOGLE_API_KEY"]

# 如果找不到金鑰，可以提供一個默認值或者報錯
if not GOOGLE_API_KEY:
    raise ValueError("No GOOGLE_API_KEY found in config.ini. Please make sure to set it.")

# 初始化 GenerativeAI
genai.configure(api_key=GOOGLE_API_KEY)
model = genai.GenerativeModel('gemini-pro')

""" Gradio 相關的 """

AVATAR_IMAGES = (
    None,
    "image.png"
)

# 定義 Gradio 的 input 和 output 函數
def generate_response(input_text):
    response = model.generate_content(input_text)
    return response.text

app = gr.Interface(
    fn=generate_response,
    inputs="textbox",
    outputs="textbox",
    title="""<h1 align="center">GenerativeAI Demo</h1>""",
    description="這是一個使用 GenerativeAI 的簡單示範，輸入你的問題，它將生成回答。",
)

# 啟動 Gradio 介面
if __name__ == "__main__":
    app.launch()