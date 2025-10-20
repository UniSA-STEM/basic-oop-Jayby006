from asset import Asset
from Hacker import Hacker
from Rig import Rig

print("=== SETUP ===")
h1 = Hacker("Nyx")
h2 = Hacker("Trinity")
print(h1)
print(h2)

#upgrade without a rig
print("\n=== Upgrade without a rig ===")
# expected False because no rig yet
print("Upgrade without rig:", h1.upgrade_rig())

#acquire rigs (costs a CryptoToken)
print("\n=== Acquire rigs ===")
print("Acquire h1:", h1.acquire_a_rig())
print("Acquire h2:", h2.acquire_a_rig())
print(h1)
print(h2)