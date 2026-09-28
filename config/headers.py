import os


class Headers:
    basic = {
        "Authorization": f"Bearer {os.getenv('API_TOKEN')}",
        "X-Task-ID": "API_KEY"
    }

print(Headers.basic)