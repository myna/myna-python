import httplib
import json

MYNA_PROTOCOL = 'http'
MYNA_HOST     = "api.mynaweb.com"
MYNA_PORT     = "80"

# Version number of this library
MYNA_VERSION  = 1.0

class MynaError(Exception):
    def __init__(self, code, messages):
        self.code = code
        self.messages = messages

    @classmethod
    def parse(self, json_str):
        parsed = json.loads(json_str)
        return MynaError.from_json(parsed)

    @classmethod
    def from_json(self, json):
        return MynaError(json['subtype'], json['messages'])


class Suggestion:
    def __init__(self, expt, choice, token):
        self.expt   = expt
        self.choice = choice
        self.token  = token

    def reward(self, amount = 1.0):
        url = "%s://%s:%s/v1/experiment/%s/reward" % (MYNA_PROTOCOL, MYNA_HOST, MYNA_PORT, self.expt.uuid)
        connection = httplib.HTTPConnection(MYNA_HOST, MYNA_PORT)
        try:
            connection.request('POST', url,
                               body = '{"choice": "%s", "token": "%s"}' % (self.choice, self.token),
                               headers = {'Accept': 'application/json'})

            response = connection.getresponse()
            body = response.read()
            content = json.loads(body)

            if response.status == 200:
                return True
            elif content['typename'] == 'problem':
                raise MynaError.from_json(content)
            else:
                raise IOError("Error communicating with the Myna server: "+body)
        finally:
            connection.close()


class Experiment:
    def __init__(self, uuid):
        self.uuid = uuid

    def suggest(self):
        url = "%s://%s:%s/v1/experiment/%s/suggest" % (MYNA_PROTOCOL, MYNA_HOST, MYNA_PORT, self.uuid)
        connection = httplib.HTTPConnection(MYNA_HOST, MYNA_PORT)
        try:
            connection.request('GET', url, headers = {'Accept': 'application/json'})

            response = connection.getresponse()
            body = response.read()
            content = json.loads(body)

            if content['typename'] == 'problem':
                raise MynaError.from_json(content)
            else:
                return Suggestion(self, content['choice'], content['token'])
        finally:
            connection.close()
