import requests

class VaingloryApi(object):
    def __init__(self, key, datacenter="dc01"):
        self.key = key
        self.datacenter = datacenter
        self.url = "https://api.{datacenter}.gamelockerapp.com/shards/".format(datacenter=self.datacenter)

    def request(self, endpoint, region, params=None):
        print("Request {0} on region {1} with params: {2}".format(endpoint, region, str(params)))
        headers = {
            "Authorization": "Bearer {}".format(self.key),
            "X-TITLE-ID": "semc-vainglory",
            "Accept": "application/vnd.api+json"
        }
        response = requests.get(self.url+"{0}/{1}".format(region, endpoint),
                            headers=headers,
                            params=params)
        # response.raise_for_status()
        return response.json()

    def query(self, endpoint, region, elid="", params=None):
        return self.request(endpoint + "/" + elid, region=region, params=params)

    def match(self, match_id, region):
        return self.query("matches", region, elid=match_id)

    def player(self, player_id, region):
        return self.query("players", region, elid=player_id)

    def players(self, players, region):
        return self.query("players", region, params={"filter[playerNames]": players})

    def matches(self, region,
                offset=None, limit=None, sort=None,
                createdAtStart=None, createdAtEnd=None,
                player=None, playerId=None, team=None, gameMode=None):

        params = dict()
        if offset:
            params["page[offset]"] = offset
        if limit:
            params["page[limit]"] = limit
        if sort:
            params["sort"] = sort
        if createdAtStart:
            params["filter[createdAt-start]"] = createdAtStart
        if createdAtEnd:
            params["filter[createdAt-end]"] = createdAtEnd
        if player:
            params["filter[playerNames]"] = player
        if playerId:
            params["filter[playerIds]"] = playerId
        if team:
            params["filter[teamNames]"] = team
        if gameMode:
            params["filter[gameMode]"] = gameMode

        return self.query("matches", region=region, params=params)
