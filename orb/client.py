import requests

BASE_URL = "https://circleci.com/api/v1"

class CircleTokenError(Exception):
    pass

def connect(token=None):
    return Orb(token)

class Orb(object):
    def __init__(self, token=None):
        if token:
            self.token = token
            self.http = requests.Session()
            self.http.headers.update({'Accept': 'application/json'})
        else:
            try:
                with open('~/.orb') as f:
                    self.token = f.read()
            except IOError as e:
                raise CircleTokenError("No valid Circle token passed or found in ~/.orb")

    def get(self, endpoint, params=None):
        url = self.build_url(endpoint)
        if params:
            params['circle-token'] = self.token
        else:
            params = {'circle-token': self.token}
        return self.http.get(url, params=params)

    def post(self, endpoint, params=None, body=None):
        url = self.build_url(endpoint)
        if params:
            params['circle-token'] = self.token
        else:
            params = {'circle-token': self.token}
        return self.http.post(url, params=params, json=body)

    def delete(self, endpoint):
        url = self.build_url(endpoint)
        return self.http.delete(url)

    def build_url(self, endpoint):
        return "{base}{endpoint}".format(base=BASE_URL, endpoint=endpoint)

    def user(self):
        endpoint = '/me'
        response = self.get(endpoint)
        return response.json()

    def list_projects(self):
        endpoint = '/projects'
        response = self.get(endpoint)
        return response.json()

    def describe_project(self, owner, project):
        endpoint = '/project/{username}/{project}'.format(username=owner, project=project)
        response = self.get(endpoint)
        return response.json()

    def recent_builds(self):
        endpoint = '/recent_builds'
        response = self.get(endpoint)
        return response.json()

    def describe_build(self, owner, project, build_number):
        endpoint = '/project/{username}/{project}/{num}'.format(username=owner, project=project, num=build_number)
        response = self.get(endpoint)
        return response.json()

    def describe_build_artifacts(self, owner, project, build_number):
        endpoint = '/project/{username}/{project}/{num}/artifacts'.format(username=owner, project=project, num=build_number)
        response = self.get(endpoint)
        return response.json()

    def retry_build(self, owner, project, build_number):
        endpoint = '/project/{username}/{project}/{num}/retry'.format(username=owner, project=project, num=build_number)
        response = self.post(endpoint)
        return response.json()

    def cancel_build(self, owner, project, build_number):
        endpoint = '/project/{username}/{project}/{num}/cancel'.format(username=owner, project=project, num=build_number)
        response = self.post(endpoint)
        return response.json()

    def create_build(self, owner, project, branch):
        endpoint = '/project/{username}/{project}/tree/{branch}'.format(username=owner, project=project, branch=branch)
        response = self.post(endpoint)
        return response.json()

    def clear_build_cache(self, owner, project, branch):
        endpoint = '/project/{username}/{project}/build-cache'.format(username=owner, project=project)
        response = self.delete(endpoint)
        return response.json()

    def create_ssh_key(self, owner, project):
        endpoint = '/project/{username}/{project}/ssh-key'.format(username=owner, project=project)
        response = self.post(endpoint)
        return response.json()

    def add_circleci_key_to_github(self):
        endpoint = '/user/ssh-key'
        response = self.post(endpoint)
        return response.json()

    def add_heroku_key_to_circleci(self, key):
        endpoint = '/user/heroku-key'
        params = {'apikey': key}
        response = self.post(endpoint, params=params)
        return response.json()


