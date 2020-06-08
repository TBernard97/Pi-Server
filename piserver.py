from pyftpdlib.handlers import FTPHandler
from pyftpdlib.servers import FTPServer
from pyftpdlib.authorizers import DummyAuthorizer
import json

class MyHandler(FTPHandler):


    def on_login(self, username):
        # do something when user login
        print("{} connected".format(username))
        pass

    def on_incomplete_file_received(self, file):
        # remove partially uploaded files
        import os
        os.remove(file)


def main():

    # JSON file 
    f = open ('config.json', "r") 
    
    # Reading from file 
    config = json.loads(f.read()) 

    authorizer = DummyAuthorizer()
    authorizer.add_user(config["client"]['user'], config["client"]['password'], homedir=config["server"]['homedir'], perm='elradfmwMT')

    handler = MyHandler
    handler.authorizer = authorizer
    server = FTPServer((config["server"]['ip'], config["server"]['port']), handler)
    server.serve_forever()

if __name__ == "__main__":
    main()