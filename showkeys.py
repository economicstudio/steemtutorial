# script for a tutorial: https://steemit.com/utopian-io/@blockchainstudio/owner-key-vs-master-password-offline-private-key-derivation-from-master-password-public-key-derivation-from-private-key

try: from beemgraphenebase.account import PasswordKey
except:
    from steem.steem import Steem
    from steembase.account import PasswordKey
import getpass

roles = ["posting", "active", "memo", "owner"]

print("Warning! This will show your private keys on the screen if you enter your master password correctly.")
print("To show that key derivations can be done offline, it will not check whether the password is correct.")

account = input("Enter account name: ")
password = getpass.getpass("Enter master password: ")

for role in roles:
    print("%s key" % role)

    pk = PasswordKey(account, password, role=role)

    print("  public:  %s" % pk.get_public())
    print("  private: %s" % pk.get_private())
