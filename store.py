# data structure to store user accounts
# todo switch to using a database like sqlite for this

# from crypt import encrypt, generate_key
import crypt
from typing import Dict

ENCRYPT_KEY = crypt.generate_key()


class Account:
    def __init__(self, address: str, name: str, meta: Dict):
        self.address = address
        self.name = name
        self.occupation = meta.get("occupation", "N/A")
        self.address = meta.get("address", "N/A")
        self.contactNo = meta.get("contactNo", "N/A")
        self.keepPrivate = meta.get("keepPrivate", False)
        self.numDonations = 0

    def __str__(self):
        return str(self.__dict__)


class Charity:
    def __init__(self, address: str, name: str, meta: Dict):
        self.address = address
        self.name = name
        self.description = meta.get("description", "N/A")


class CharityStore:
    def __init__(self):
        self.charities = {}

    def add_charity(self, charity: Charity):
        self.charities[charity.address] = charity

    def get_charity(self, address: str):
        return self.charities.get(address)

    def __str__(self):
        return str(self.charities)

    def __repr__(self):
        return str(self.charities)


class AccountStore:
    def __init__(self):
        self.accounts = {}

    def add_account(self, account: Account):
        private_key = crypt.encrypt(account.address, ENCRYPT_KEY)
        self.accounts[private_key] = account
        return private_key

    def get_account(self, private_key: str):
        return self.accounts.get(private_key)

    def __str__(self):
        return str(self.accounts)

    def __repr__(self):
        return str(self.accounts)
