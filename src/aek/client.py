import json
import urllib.request

try:
    import requests
    HAS_REQUESTS = True
except ImportError:
    HAS_REQUESTS = False

_builtin_next = next
NEXT_URL = "https://www.thesportsdb.com/api/v1/json/123/eventsnext.php?id=133753"
TABLE_URL = "https://www.thesportsdb.com/api/v1/json/123/lookuptable.php?l=4336"

print('Welcome to the AEK Athens module in python! Explore by typing in certain commands or type aek.help(). For more details regarding compliance and copyright, please type in aek.copyright().')


def _fetch_json(url: str) -> dict:
    headers = {"User-Agent": "aek"}
    if HAS_REQUESTS:
        r = requests.get(url, headers=headers, timeout=10)
        r.raise_for_status()
        return r.json()

    req = urllib.request.Request(url, headers=headers)
    with urllib.request.urlopen(req, timeout=10) as response:
        return json.loads(response.read().decode("utf-8"))


def next():
    data = _fetch_json(NEXT_URL)

    next_match = _builtin_next(iter(data["events"]))

    x = next_match["strHomeTeam"]
    y = next_match["strAwayTeam"]
    z = next_match["strLeague"]
    a = next_match["strVenue"]
    b = next_match["dateEvent"]
    c = next_match["strTime"]

    print(x, 'vs', y, 'at', c, 'on', b, 'for the', z, sep=' ')


def rank():
    data = _fetch_json(TABLE_URL)

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
