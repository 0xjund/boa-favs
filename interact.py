import os
import boa
from boa.network import EthereumRPC, NetworkEnv
from eth_account import Account 
from dotenv import load_dotenv

load_dotenv()

MY_CONTRACT="0x9fE46736679d2D9a65F0992F2272dE9f3c7fa6e0" 

def main():
   rpc = os.getenv("RPC_URL") 
   env = NetworkEnv(EthereumRPC(rpc))
   boa.set_env(env)

   anvil_key = os.getenv("ANVIL_KEY")
   my_account = Account.from_key(anvil_key)
   boa.env.add_account(my_account, force_eoa=True)

   favourite_deployer = boa.load_partial("favourites.vy")
   favourites_contract = favourite_deployer.at(MY_CONTRACT)

   favourite_number = favourites_contract.retrieve()
   print(f"Favourite number is {favourite_number}")

   favourites_contract.store(22)
   favourite_number_updated = favourites_contract.retrieve()

   print(f"Favourite number is now: {favourite_number_updated} ")
   
if __name__ == "__main__":
    main()

