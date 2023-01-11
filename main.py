import requests, time, json, string, random

user_tokens = [ "" ]

# bot_tokens_file = open("bot_tokens.txt", 'a+')

def worker(token):
    for i in range(20):
        headers_for_token={
            "authorization": user_TOKEN,
            "content-type": "application/json",
            "sec-fetch-dest": "empty",
            "sec-fetch-mode": "cors"
        }

        json_for_create={
            "name": (''.join(random.choice(string.ascii_lowercase) for i in range(8)))
        }

        r_create_app=requests.post(url="https://discord.com/api/v9/applications", headers=headers_for_token, json=json_for_create)
        if(r_create_app.status_code == 429):
            time.sleep(json.loads(str(r_create_app.text))["retry_after"])
            continue

        app_id=json.loads(str(r_create_app.text))['id']

        time.sleep(1)

        r_get_bot=requests.post(url=f"https://discord.com/api/v9/applications/{app_id}/bot", headers=headers_for_token)
        if(r_get_bot.status_code == 429):
            time.sleep(json.loads(str(r_get_bot.text))["retry_after"])
            continue

        time.sleep(1)

        r_resetToken=requests.post(url=f"https://discord.com/api/v9/applications/{app_id}/bot/reset", headers=headers_for_token)
        if(r_resetToken.status_code == 429):
            time.sleep(json.loads(str(r_resetToken.text))["retry_after"])
            continue

        bot_token=json.loads(str(r_resetToken.text))['token']

        print(bot_token)
        # bot_tokens_file.write(bot_token+'\n')
        time.sleep(180)

threads = []

for token in tokens:
    thread = threading.Thread(target=worker, args=(token,))
    thread.start()
    threads.append(thread)

for thread in threads:
    thread.join()
