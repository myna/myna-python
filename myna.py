import httplib
import json

MYNA_PROTOCOL = 'http'
MYNA_HOST     = "api.mynaweb.com"
MYNA_PORT     = "80"

class Suggestion:
    def __init__(self, choice, token):
        self.choice = choice
        self.token  = token

    def reward(amount = 1.0):
        url = "%s://%s:%s/v1/experiment/%s/reward" % (MYNA_PROTOCOL, MYNA_HOST, MYNA_PORT, self.uuid)
        connection = httplib.HTTPConnection(MYNA_HOST, MYNA_PORT)
        connection.request('POST', url,
                           body = "{choice: %s, token: %s}" % (self.choice, self.token),
                           headers = {'Accept': 'application/json'})

        response = connection.getresponse()

        if response.status == 200:
            body = response.read()
            connection.close()
            content = json.loads(body)
            return content
        else:
            connection.close()
            return 'Bummer'

class Experiment:
    def __init__(self, uuid):
        self.uuid = uuid

    def suggest(self):
        url = "%s://%s:%s/v1/experiment/%s/suggest" % (MYNA_PROTOCOL, MYNA_HOST, MYNA_PORT, self.uuid)
        connection = httplib.HTTPConnection(MYNA_HOST, MYNA_PORT)
        connection.request('GET', url, headers = {'Accept': 'application/json'})

        response = connection.getresponse()
#        connection.close()

        if response.status == 200:
            body = response.read()
            connection.close()
            content = json.loads(body)
            return Suggestion(content['choice'], content['token'])
        else:
            connection.close()
            return 'Bummer'


# Test
expt = Experiment('45923780-80ed-47c6-aa46-15e2ae7a0e8c')
resp = expt.suggest()
