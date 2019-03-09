# script for a tutorial: https://steemit.com/utopian-io/@blockchainstudio/owner-key-vs-master-password-offline-private-key-derivation-from-master-password-public-key-derivation-from-private-key

try: from beemgraphenebase.account import PrivateKey
except:
    from steem.steem import Steem
    from steembase.account import PrivateKey
import getpass

wif = getpass.getpass("Enter any private key: ")

print("public key: %s" % PrivateKey(wif).pubkey)
