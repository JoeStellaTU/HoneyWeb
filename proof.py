# Recursive Honeypot Network Proof of Concept

import random
import time

class Honeypot:
    def __init__(self, name):
        self.name = name
        self.spawned_honeypots = []

    def engage(self, attacker_ip):
        print(f"{self.name} engaged by {attacker_ip}")
        # Log attacker's actions or simulate responses here

        # Simulate spawning new honeypots
        if random.random() < 0.5:
            new_honeypot = Honeypot(f"{self.name}_spawned_{len(self.spawned_honeypots) + 1}")
            self.spawned_honeypots.append(new_honeypot)
            print(f"New honeypot '{new_honeypot.name}' spawned!")

            # Recursively engage the new honeypot
            new_honeypot.engage(attacker_ip)

def main():
    initial_honeypot = Honeypot("Initial_Honeypot")
    print(f"Deployed initial honeypot: {initial_honeypot.name}")

    while True:
        attacker_ip = input("Enter attacker IP (or 'exit' to quit): ")
        if attacker_ip.lower() == "exit":
            break

        # Engage the initial honeypot
        initial_honeypot.engage(attacker_ip)

if __name__ == "__main__":
    main()

