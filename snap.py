import requests, json, sys, re

c = 0


def snapstory(username):
    global c

    try:
        url = 'https://story.snapchat.com/@'

        headers = {
            'User-Agent':
            'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:94.0) Gecko/20100101 Firefox/103.0.2'
        }

        r = requests.get(f"{url}{username}", headers=headers)

        text = r.text
        code = r.status_code
        code if code == 200 else sys.exit('This snap not exists')

        data = re.findall('id="__NEXT_DATA__" type="application/json">(.*?)<',
                          text)[0]

        data = json.loads(data)

        snaplist, snaptype = [], []

        for i in data["props"]["pageProps"]["story"]["snapList"]:
            mediaUrl = i['snapUrls']['mediaUrl']
            snapMediaType = i['snapMediaType']
            snaplist.append(mediaUrl)
            snaptype.append(snapMediaType)

        data = '''{"username": "username", "len": "len", "list":[]}'''
        data2 = json.loads(data)
        data2['username'] = username
        data2['len'] = len(snaplist)
        for url, mtype in zip(snaplist, snaptype):

            data2['list'].append({
                "story": c,
                "urls": url,
                "snapMediaType": mtype
            })
            c += 1
    except:
        return {"Error": code}
    c = 0
    return data2


# print(snapstory("abodka_q8333"))
# print(snapstory(""))