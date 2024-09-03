import crypt
import json
import logging

from cartesi import DApp, Rollup, RollupData, URLRouter
from cartesi.models import _str2hex
from cartesi.wallet.ether import EtherWallet

from store import Account, AccountStore, Charity, CharityStore

LOGGER = logging.getLogger(__name__)
logging.basicConfig(level=logging.DEBUG)
dapp = DApp()
url_router = URLRouter()
account_store = AccountStore()
charity_story = CharityStore()


def str2hex(str):
    """Encodes a string as a hex string"""
    return "0x" + str.encode("utf-8").hex()


pending_transactions = {}

ETHER_PORTAL_ADDRESS = "0xffdbe43d4c855bf7e0f105c400a50857f53ab044"


ether_wallet = EtherWallet(portal_address=ETHER_PORTAL_ADDRESS)
dapp.add_router(ether_wallet)


@dapp.advance()
def handle_advance(rollup: Rollup, data: RollupData) -> bool:
    rollup.report("")
    raw_payload = data.str_payload()
    payload = json.loads(raw_payload)
    command = payload.get("command")
    if command == "CREATE_ACCOUNT":
        account = Account(
            payload["data"]["address"], payload["data"]["name"], payload["data"]["meta"]
        )

        private_key = account_store.add_account(account)

        rollup.notice(
            f"Your account has been created and your private key is {private_key}"
        )

    elif command == "MAKE_DONATION":
        account = account_store.get_account(payload["data"]["private_key"])
        charity = charity_story.get_charity(payload["data"]["charity_address"])
        if charity and account:
            pending_transactions[account.address] = {
                "charity": charity.name,
                "amount": payload["data"]["amount"],
            }

            rollup.notice(
                f"Pending Deposit Created for user {account.name} to charity {charity.name} for amount {payload['data']['amount']}"
            )

            report_data = {
                "message": "pending transactions",
                "data": pending_transactions,
            }

            rollup.report(f"{str(report_data)}")
        else:
            rollup.notice("Invalid charity or account")

    elif command == "START_CHARITY":
        charity = Charity(
            payload["data"]["address"], payload["data"]["name"], payload["data"]["meta"]
        )
        charity_story.add_charity(charity)
        rollup.notice(f"Charity {charity.name} has been created")

    else:
        rollup.notice("Invalid command")

    return True


@url_router.inspect("/account/:private_key")
def get_account(private_key):
    account = account_store.get_account(private_key)
    if account:
        return account.to_dict()
    return {"error": "Account not found"}


@url_router.inspect("/charity/:address")
def get_charity(address):
    charity = charity_story.get_charity(address)
    if charity:
        return charity.to_dict()
    return {"error": "Charity not found"}


@url_router.inspect("/pending_transactions/:address")
def get_pending_transactions(address):
    return pending_transactions.get(address)


if __name__ == "__main__":
    dapp.run()
