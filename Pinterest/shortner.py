def short_link(lk):
    import requests
    access_token = 'd204ce61f239e25ec4c897bc1ed7b5370f3818cc'
    headers = {"Authorization": f"Bearer {access_token}"}
    guid = 'Bn17dliRqSz'
    while True:
        url = lk
        shorten_res = requests.post("https://api-ssl.bitly.com/v4/shorten", json={"group_guid": guid, "long_url": url},
                                    headers=headers)
        if shorten_res.status_code == 200:
            link = shorten_res.json().get("link")
            break
        else:
            groups_res = requests.get("https://api-ssl.bitly.com/v4/groups", headers=headers)
            if groups_res.status_code == 200:
                # if response is OK, get the GUID
                groups_data = groups_res.json()['groups'][0]
                guid = groups_data['guid']
            else:
                print("[!] Cannot get GUID, exiting...")
                continue
    return link