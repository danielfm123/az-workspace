import json
import os


home = os.path.expanduser("~")

settings_path = home+'/.az-workspace.json'


def getParams():
    try:
        with open(settings_path, 'r') as f:
            params = json.load(f)
    except:
        with open(settings_path, 'w+') as f:
            f.writelines(["{}"])
        with open(settings_path, 'r') as f:
            params = json.load(f)
    return params

params = getParams()

class settingsManager():

    def __init__(self):
        pass

    def setParam(self, key, value):
        global params
        params[key] = str(value)

    def writeParams(self):
        global params

        with open(settings_path, 'w') as f:
            json.dump(params,f)

    def refresh(self):
        getParams()

    def getParam(self,key):
        if key == "settings_path":
            global settings_path
            return settings_path

        global params

        try:
            return(params[key])
        except:
            return("")

    def getInstance(self):
        try:
            session = self.getSession()
            ec2 = session.resource("ec2",use_ssl=False)
            self.instance = ec2.Instance(id=self.getParam('ec2_id'))
            return self.instance
        except:
            return None

    def getIP(self):
        try:
            self.ip = 1
            return self.ip
        except:
            return None

