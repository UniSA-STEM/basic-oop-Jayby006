"""
File: Hacker.py
Description: <A brief description of this Python module.>
Author: Jayanga Madushanka Bandara Bathabure Gedara
ID: 110432974
Username: jayby006
This is my own work as defined by the University's Academic Misconduct Policy.
"""
from asset import Asset

Trace_limit = 5

class Hacker:
    def __init__(self,name):
        self.__name = name
        self.__inventory = [Asset("CryptoTocken", "Starter token")]
        self.__rig = None
        self.__trace = 0