#!/usr/bin/python3
"""query the reddit api"""

import requests

def number_of_subscribers(subreddit):
    header = {"User-Agent": "Holberton"}
    req = "https/www.reddit.com/r/" + subreddit + "/about/json"
    res = requests.get(req, headers=header)
    if (res.status_code == 200):
        return res.json().get("data", None).get("subscribers", None)
    return 0
if __name__ == "__main__":
    pass
