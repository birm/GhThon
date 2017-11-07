import requests

class Api(object):
    def __init__(self, username="", password=""):
        # probably not a good auth strategy, good thing it's not needed
        self.auth = (username, password)
    def sanitize(self, text, path=False):
        # TODO actually sanitize
        if path:
            if text[0] != "/":
                text = "/" + text
        else:
            text = text.replace("/", "")
        return text
    def get_content(self, url):
        print url
        return requests.get(url)
    def repos(self, username, org=False):
        username = self.sanitize(username)
        if org:
            content = self.get_content("https://api.github.com/orgs/" +
                                       username + "/repos")
        else:
            content = self.get_content("https://api.github.com/users/" +
                                       username + "/repos")
        return content.json
    def raw_file(self, user, repo, path, branch="master"):
        user = self.sanitize(user)
        branch = self.sanitize(branch)
        repo = self.sanitize(repo)
        path = self.sanitize(path, True)
        content = self.get_content("https://raw.githubusercontent.com/" +
                                   user + "/"+repo + "/" + branch + path)
        return content.text

    #you should fork this and add more methods :)

a = Api("","")
a.repos("birm")
a.raw_file("birm","GhThon","/GhThon/Api.py")
