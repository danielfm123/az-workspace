#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Nov  1 23:33:56 2018

@author: dfischer
"""

from modules.functions import *
from PySide2.QtWidgets import *
import os
from modules import SettingsManager
import platform
from azure.common.client_factory import get_client_from_cli_profile
from azure.mgmt.compute import ComputeManagementClient
from azure.mgmt.network import NetworkManagementClient

compute_client = get_client_from_cli_profile(ComputeManagementClient)
network_client = get_client_from_cli_profile(NetworkManagementClient)

settings = SettingsManager.settingsManager()

home = os.path.expanduser("~")

class idEc2Form(QDialog):
    def __init__(self,parent):
        super(idEc2Form,self).__init__(parent)
        self.parent = parent
        self.setMinimumWidth(400)
        self.setWindowTitle("AZ API Manager")

        vm = compute_client.virtual_machines.list('DataArts')
        dict = {i.name : i.name  for i in vm}

        self.combo_vm = QComboBox()
        for i in dict.keys():
            self.combo_vm.addItem(dict[i], i)
        try:
            self.combo_vm.setCurrentText(dict[settings.getParam("ec2_id")])
        except:
            pass

        self.os = QComboBox()
        for os in ['Linux','Windows']:
            self.os.addItem(os)

        self.mainLayout = QVBoxLayout()

        self.keys = QGridLayout()
        self.keys.addWidget(QLabel("VM Name"),0,0)
        self.keys.addWidget(self.combo_vm, 0, 1)
        self.keys.addWidget(QLabel("Operating System"), 1, 0)
        self.keys.addWidget(self.os, 1, 1)
        self.user = QLineEdit()
        self.user.setText(settings.getParam('vm_user'))
        self.keys.addWidget(QLabel('VM User'),2,0)
        self.keys.addWidget(self.user, 2, 1)
        self.pwd = QLineEdit()
        self.pwd.setText(settings.getParam('vm_password'))
        self.pwd.setEchoMode(QLineEdit.Password)
        self.keys.addWidget(QLabel("VM Current Password"), 3, 0)
        self.keys.addWidget(self.pwd, 3, 1)
        self.save = QPushButton("Save")
        self.save.clicked.connect(self.save_to_file)

        self.mainLayout.addLayout(self.keys)
        self.mainLayout.addWidget(self.save)

        self.setLayout(self.mainLayout)

    def save_to_file(self):
        id = self.combo_vm.currentData()
        print(self.combo_vm.currentData())
        settings.setParam('vm_name',id)
        settings.setParam('os', self.os.currentText())
        settings.setParam('vm_password', self.pwd.text())
        settings.setParam('vm_user', self.user.text())
        settings.writeParams()
        self.parent.parent.refresh()

        self.close()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = idEc2Form(None)
    window.show()
   # sys.exit(app.exec_())
    app.exec_()





