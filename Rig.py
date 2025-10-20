"""
File: Rig.py
Description: <A brief description of this Python module.>
Author: <full name>
ID: <student_id>
Username: <username>
This is my own work as defined by the University's Academic Misconduct Policy.
"""
from asset import Asset

class Rig:
    def __init__(self, name):
        self.__name = name
        self.__damage = 0
        self.__broken = False
        self.__upgrade_level = 0
        self.__storage = [
            Asset("Data Spike", "Offensive payload"),
            Asset("Data Spike", "Offensive payload"),
            Asset("Removable Drive", "For extraction")
        ]
        self.__gen_index = 0

    def get_name(self):
        return self.__name

    def get_damage(self):
        return self.__damage

    def get_broken(self):
        return self.__broken

    def get_upgrade_level(self):
        return self.__upgrade_level
    
    def condition(self):
        if self.__broken:
            state = "Broken"
        elif self.__damage == 0:
            state = "Pristine"
        else:
            state = "Damaged " + str(self.__damage)
        return state + " (Level " + str(self.__upgrade_level) + ")"
    
    def take_spike_hit(self):
        if self.__broken:
            return
        self.__damage = self.__damage + 1
        threshold = 2 + self.__upgrade_level
        if self.__damage >= threshold:
            self.__broken = True

    def repair_with_token(self, token_asset):
        if token_asset is None or token_asset.get_name() != "CryptoToken":
            return False
        if self.__damage == 0 and not self.__broken:
            print("No repair needed.")
            return False
        self.__damage = 0
        self.__broken = False
        return True