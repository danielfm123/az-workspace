import json
import os
from azure.common.client_factory import get_client_from_cli_profile
from azure.mgmt.compute import ComputeManagementClient
from azure.mgmt.network import NetworkManagementClient

compute_client = get_client_from_cli_profile(ComputeManagementClient)
network_client = get_client_from_cli_profile(NetworkManagementClient)

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

    def getVM(self):
        return compute_client.virtual_machines.get(self.getParam('az_group'),self.getParam('vm_name'))


    def getIP(self):
        try:
            self.ip = 1
            return self.ip
        except:
            return None

