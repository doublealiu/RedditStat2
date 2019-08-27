import yaml

class Config:
    def __init__(self):
        stream = open("config.yml", "r")
        if(stream.mode != 'r'):
            return
        contents = yaml.load(stream)
        keys = contents.keys
        self.subreddits = {}
        for key, value in keys:
            self.subreddits[key] = value