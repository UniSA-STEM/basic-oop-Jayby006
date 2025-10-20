"""
File: Rig.py
Description: Represents a computer rig that can store assets, take damage, be repaired/upgraded.
Author: Jayanga Madushanka Bandara Bathabure Gedara
ID: 110432974
Username: jayby006
This is my own work as defined by the University's Academic Misconduct Policy.
"""
from asset import Asset

class Rig:
    def __init__(self, name):
        self.__name = name
        self.__damage = 0 # increments when hit
        self.__broken = False
        self.__upgrade_level = 0
        
        self.__storage = [
            Asset("Data Spike", "Offensive payload"),
            Asset("Data Spike", "Offensive payload"),
            Asset("Removable Drive", "For extraction")
        ]
        
    def get_name(self):
        return self.__name

    def get_damage(self):
        return self.__damage

    def get_broken(self):
        return self.__broken

    def get_upgrade_level(self):
        return self.__upgrade_level
    
    def condition(self): #Text condition like 'Pristine (Level 1)' or 'Broken (Level 0)'.

        if self.__broken:
            state = "Broken"
        elif self.__damage == 0:
            state = "Pristine"
        else:
            state = "Damaged " + str(self.__damage)
        return state + " (Level " + str(self.__upgrade_level) + ")"
    
    def take_spike_hit(self):  #Apply one spike hit. Level 0 breaks at 2; threshold = 2 + level.

        if self.__broken:
            return
        self.__damage = self.__damage + 1
        threshold = 2 + self.__upgrade_level
        if self.__damage >= threshold:
            self.__broken = True

    def repair_with_token(self, token_asset): #Repair using CryptoToken. Reset damage; print if nothing to fix.

        if token_asset is None or token_asset.get_name() != "CryptoToken":
            return False
        if self.__damage == 0 and not self.__broken:
            print("No repair needed.")
            return False
        self.__damage = 0
        self.__broken = False
        return True
    
    def upgrade_with_patch(self, patch_asset):  #Upgrade using Hardware Patch. Increases level by 1.
        if patch_asset is None or patch_asset.get_name() != "Hardware Patch":
            return False
        self.__upgrade_level = self.__upgrade_level + 1
        return True
    
    def capacity(self): #Max items rig can store. Base 4 + level.

        return 4 + self.__upgrade_level

    def can_store_more(self): #True if storage has free space.

        return len(self.__storage) < self.capacity()

    def store(self, asset): #Store an unencrypted asset if capacity allows.

        if asset.get_encrypted():
            return False
        if not self.can_store_more():
            return False
        self.__storage.append(asset)
        return True
    
    def release(self, name): #Release one unencrypted asset by name, or None if not present.

        for a in self.__storage:
            if a.get_name() == name and not a.get_encrypted():
                self.__storage.remove(a)
                return a
        return None

    def release_unencrypted(self):  #Release all unencrypted assets, keep encrypted ones in storage.

        items = []
        keep_items = []
        i = 0
        while i < len(self.__storage):
            a = self.__storage[i]
            if a.get_encrypted():
                keep_items.append(a)
            else:
                items.append(a)
            i = i + 1
        self.__storage = keep_items
        return items

    def encrypt_in_storage(self, name): #Encrypt a stored asset
        i = 0
        while i < len(self.__storage):
            if self.__storage[i].get_name() == name:
                self.__storage[i].encrypt()
                return True
            i = i + 1
        return False

    def decrypt_in_storage(self, name): #Decrypt a stored asset
        i = 0
        while i < len(self.__storage):
            if self.__storage[i].get_name() == name:
                self.__storage[i].decrypt()
                return True
            i = i + 1
        return False
   
    def __str__(self):
        i = 0
        items = []
        while i < len(self.__storage):
            items.append(str(self.__storage[i]))
            i = i + 1
        if len(items) == 0:
            items_text = "Empty"
        else:
            items_text = ", ".join(items)
        return "Rig: " + self.__name + " | Condition: " + self.condition() + " | Level: " + str(self.__upgrade_level) + " | Assets: " + items_text