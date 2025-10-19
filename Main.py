from asset import Asset
from Hacker import Hacker

print("=== Acquire rig and __str__ ===")
h1 = Hacker("Nyx")
print("Before:", str(h1))
acq_ok = h1.acquire_a_rig()   # costs one CryptoToken
print("Acquire returned:", acq_ok)
print("After:", str(h1))