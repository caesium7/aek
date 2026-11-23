import requests

_builtin_next = next
URL = "https://www.thesportsdb.com/api/v1/json/123/eventsnext.php?id=133753"


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
