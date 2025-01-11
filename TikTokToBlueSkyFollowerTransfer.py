from atproto import Client
import sys
import json
import requests


def main():
    client = Client()
    profile = client.login(sys.argv[1], sys.argv[2])

    with open('user_data_tiktok.json', 'r', encoding="utf8") as file:
        myTikTokJson = json.load(file)
        Following = []
        for followUser in myTikTokJson['Activity']['Following List']['Following']:
            Following.append(followUser['UserName'])
        file.close()

    #print(Following)

    for x in Following:
        url = "https://bsky.social/xrpc/com.atproto.identity.resolveHandle?handle=" + x + ".bsky.social"
        response = requests.get(url)
        if response.status_code == 200:

            print(x + " found. Following...")
            client.follow(response.json()['did']).uri
        elif response.status_code == 400:
            print(x + ".bsky.social" + " Is not a valid Username.")


if __name__ == "__main__":
    main()
