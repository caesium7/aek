import requests

_builtin_next = next
URL = "https://www.thesportsdb.com/api/v1/json/123/eventsnext.php?id=133753"

print('Welcome to the AEK Athens module in python! Explore by typing in certain commands or type aek.help(). For more details regarding compliance and copyright, please type in aek.copyright().')


def next():
    r = requests.get(URL, headers={"User-Agent": "aek"}, timeout=10)
    data = r.json()

    next_match = _builtin_next(iter(data["events"]))

    x = next_match["strHomeTeam"]
    y = next_match["strAwayTeam"]
    z = next_match["strLeague"]
    a = next_match["strVenue"]
    b = next_match["dateEvent"]
    c = next_match["strTime"]

    print(x, 'vs', y, 'at', c, 'on', b, 'for the', z, sep=' ')


def rank():
    import json
    import urllib.request

    url = "https://www.thesportsdb.com/api/v1/json/123/lookuptable.php?l=4336"
    with urllib.request.urlopen(url) as response:
        data = json.loads(response.read().decode("utf-8"))

    table = data.get("table") or []
    for row in table:
        if row.get("idTeam") == "133753":
            x = int(row["intRank"])
            print(f"AEK Athens are number {x} in the Greek Super League")
            return
    print("AEK Athens are currently outside the top 5 in the Greek Super League")

def stadium():
    print('AEK Athens play at the ALLWYN Arena (Agia Sophia Stadium). It can hold 32,500 people and was built in October 2022.')
def copyright():
    print(
        "aekfc — Unofficial AEK Athens F.C. Python Package\n"
        "Copyright (c) 2026 C Bartsocas (MIT License)\n\n"
        "Disclaimer: This is an unofficial fan-based project and is not endorsed by,\n"
        "affiliated with, or commissioned by AEK Athens F.C. All club names,\n"
        "competition names, and trademarks belong to their respective owners.\n\n"
        "Data Source: TheSportsDB (https://www.thesportsdb.com)"
    )
def help():
    print('Check out the readme on PYPI, at https://pypi.org/project/aekfc/ for more details.')
