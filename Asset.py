"""
File: Asset.py
Description: Defines the Asset class with name, description, and encrypted flag.
Author: Jayanga Madushanka Bandara Bathabure Gedara
ID: 110432974
Username: jayby006
This is my own work as defined by the University's Academic Misconduct Policy.
"""
class Asset:
    def __init__(self, name, description, encrypted=False):
        self.__name = name
        self.__description = description
        self.__encrypted = encrypted 

    def get_name(self):
        return self.__name

    def get_description(self):
        return self.__description

    def get_encrypted(self):
        return self.__encrypted

    def set_description(self, text):
        self.__description = text

    def encrypt(self): 
        self.__encrypted = True

    def decrypt(self):
        self.__encrypted = False

    def __str__(self):
        base = self.__name + ": " + self.__description
        if self.__encrypted:
            return base + " Encrypted"
        return base