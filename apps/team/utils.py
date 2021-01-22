import requests
import json

def send_push_notification(title, content, recipient_id):
    print(content)
    header = {
        "Content-Type": "application/json; charset=utf-8",
        "Authorization": "Basic MjBhMjIwZWItZmNhMS00YzMyLWE2NDMtODRiZjkzMzBjYzgx"
    }
    req_players = requests.get(
        "https://onesignal.com/api/v1/players?app_id=dd43cf2f-c90a-4e93-bd23-16e2b0687f61&limit=300&offset=0",
        headers=header)
    print(req_players)
    list_profiles_id = []
    list_players_recipients = []

    for req_player in req_players.json()['players']:
        print('player external user id')
        print(str(req_player['external_user_id']))
        if str(req_player['external_user_id']) == str(recipient_id):
            list_players_recipients.append(req_player['id'])

    print('list ids')
    print(list_profiles_id)
    print('list players to sent')
    print(list_players_recipients)

    payload = {
        "app_id": "dd43cf2f-c90a-4e93-bd23-16e2b0687f61",
        "include_player_ids": list_players_recipients,
        "contents": {
            "en": content
        },
        "content-available": 1,
        "headings": {
            "en": title # Titolo notifica
        },
        "data": {
            "custom_data": "",
        },
        "small_icon": "ic_stat_onesignal_default"
    }

    # "android_channel_id": "8d3bd99c-1755-4a33-a043-60a92c8b153c",
    # "wp_wns_sound": "erotic_girl_sound",
    # "android_sound": "erotic_girl_sound",

    req = requests.post("https://onesignal.com/api/v1/notifications", headers=header, data=json.dumps(payload))
    print(req.status_code, req.reason)