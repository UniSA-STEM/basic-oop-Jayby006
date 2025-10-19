"""
File: Hacker.py
Description: <A brief description of this Python module.>
Author: Jayanga Madushanka Bandara Bathabure Gedara
ID: 110432974
Username: jayby006
This is my own work as defined by the University's Academic Misconduct Policy.
"""
from asset import Asset
from rig import Rig

Trace_limit = 5

class Hacker:
    def __init__(self,name):
        self.__name = name
        self.__inventory = [Asset("CryptoTocken", "Starter token")]
        self.__rig = None
        self.__trace = 0

    def get_name(self):
        return self.__name

    def get_rig(self):
        return self.__rig

    def get_trace(self):
        return self.__trace

    def get_inventory(self):
        inventory = []
        i = 0
        while i < len(self.__inventory):
            inventory.append(self.__inventory[i])
            i = i + 1
        return inventory
    
    def add_trace(self, amount = 0):
        self.__trace = self.__trace + amount

    def exposed(self):
        return self.__trace > Trace_limit
    
    def scan_inventory(self, name):
        for item in self.__inventory:
            if item.get_name() == name :
                self.__inventory.remove(item)
                return item
        return None 
   
    def acquire_a_rig(self, rig = None):
        token = self.scan_inventory("CryptoToken")

        if token is None:
            return False
        
        if rig is None:
            self.__rig = Rig(self.__name + "Rig")
        else:
            self.__rig = rig
        print( "Rig activation successful:", self.__rig.get_name())

        return True
    
    def launch_data_spike(self, target_rig):
        if self.__rig is None:
            return False
        
        if self.exposed():
            return False
        
        spike = self.__rig.release("Data Spike")
        
        if spike is None:
            return False
        target_rig.take_spike_hit()
        self.__add_trace(1)

        return True
    
    def extract_unencrypted(self, target_rig):
        if self.__rig is None:
            return None
        
        if self.exposed():
            return None
        
        if not target_rig.get_broken():
            return None
        
        drive = self.__rig.release("Removable Drive")

        if drive is None:
            return None
        
        items = target_rig.release_unencrypted()
        i = 0

        while i < len(items):
            self.__inventory.append(items[i])
            i = i + 1
        self.add_trace(1)
        return items
    
    def encrypt_inventory(self, name):
        if self.exposed():
            return False
        chip = self.scan_inventory("Security Chip")
        if chip is None:
            return False
        item = self.scan_inventory(name)
        if item is None:
            self.__inventory.append(chip)
            return False
        item.encrypt()
        self.__inventory.append(item)
        return True
    
    def encrypt_rig(self, name):
        if self.exposed():
            return False
        if self.__rig is None:
            return False
        chip = self.scan_inventory("Security Chip")
        if chip is None:
            return False
        ok = self.__rig.encrypt_in_storage(name)
        if not ok:
            self.__inventory.append(chip)
            return False
        return True
    
    def decrypt_inventory(self, name):
        if self.exposed():
            return False
        chip = self.scan_inventory("Security Chip")
        if chip is None:
            return False
        i = 0
        while i < len(self.__inventory):
            if self.__inventory[i].get_name() == name:
                self.__inventory[i].decrypt()
                return True
            i = i + 1
        self.__inventory.append(chip)
        return False
    
    def decrypt_rig(self, name):
        if self.exposed():
            return False
        if self.__rig is None:
            return False
        chip = self.scan_inventory("Security Chip")
        if chip is None:
            return False
        ok = self.__rig.decrypt_in_storage(name)
        if not ok:
            self.__inventory.append(chip)
            return False
        return True