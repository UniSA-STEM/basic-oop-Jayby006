from asset import Asset
from Hacker import Hacker
from Rig import Rig


def main():
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

    # Encrypt without a Security Chip
    print("\n--- Test: Encrypt without Security Chip ---")
    encryption = h1.encrypt_inventory("Anything")
    print("Encrypt inventory without chip :", encryption)

    # Prepare defender with a plain unencrypted asset
    h2.get_rig().store(Asset("Data", "Valuable file"))

    # BATTLE - h1 attacks h2 until broken 

    print("\n--- Battle ---")
    tries = 0
    while tries < 5:
        if h2.get_rig().get_broken():
            break
        ok = h1.launch_data_spike(h2.get_rig())
        print("Spike", tries + 1, "->", ok)
        tries = tries + 1

        print("Defender broken:", h2.get_rig().get_broken())
        print("Defender condition:", h2.get_rig().condition())

    # Extraction after broken

    print("\n--- Extraction ---")
    print()
    stolen = h1.extract_unencrypted(h2.get_rig())
    if not stolen:
        print("Extracted items:")
    else:
        names = []
        i = 0
        while i < len(stolen):
            names.append(stolen[i].get_name())
            i = i + 1
        print("Extracted items:", ", ".join(names))
    print(h1)

    print("\n--- Test: Attack with High Trace ---")
    print()
    h1.add_trace(6)  # push trace over 5
    print("Hacker exposed:", h1.exposed())
    blocked = h1.launch_data_spike(h2.get_rig())
    print("Attack while exposed (expected False):", blocked)

    # REPAIR with CryptoToken
    print("\n--- Repair ---")
    print()
    repair_token = Asset("CryptoToken", "For repair")
    print("Repair success:", h2.get_rig().repair_with_token(repair_token))
    print("Rig condition:", h2.get_rig().condition())

    # UPGRADE with Hardware Patch
    print("\n--- Upgrade ---")
    print()
    patch = Asset("Hardware Patch", "Upgrade part")
    print("Upgrade success:", h2.get_rig().upgrade_with_patch(patch))
    print("Rig condition:", h2.get_rig().condition())

    print("\n=== DONE ===")

if __name__ == "__main__":
    main()
