import requests


def get_bot_updates(limit, offset):
    url = "https://api.telegram.org/bot620076620:AAFUBTpg_NS-ssyLj2jvVbGJvDWH_7bORRk/getUpdates"
    par = {'limit': limit, 'offset': offset} 
    result = requests.get(url,params=par)
    decoded = result.json()
    return decoded['result']
#print(get_bot_updates(6,0))
#update_id=get_bot_updates(6,0)[2]

def sender(chat_id,text):
    url = "https://api.telegram.org/bot620076620:AAFUBTpg_NS-ssyLj2jvVbGJvDWH_7bORRk/sendMessage"
    par = {'chat_id': chat_id, 'text': text} 
    result=requests.get(url,params=par)
    decoded = result.json()
    return decoded


#sender(update_id,"hello")
def rates(coin):
    url = "https://api.cryptonator.com/api/full/{}-usd".format(coin) 
    result = requests.get(url)
    decoded = result.json()

    return decoded['ticker']['price']
offset = 0
while True:
    updates=get_bot_updates(5,offset)
    if len(updates)==0:
        continue
    else:
        for update in updates:
            text = update['message']['text']
            update_id = update['update_id']
            chat_id = update['message']['from']['id']
        
            if text == "/start":
                sender(chat_id,"Enter /btc for bitcoin or /eth for ehterium")
            elif text== "/btc":
                sender(chat_id,"btc: "+rates("btc"))
            elif text== "/eth":
                sender(chat_id,"eth: "+rates("eth"))
        offset = update_id+1