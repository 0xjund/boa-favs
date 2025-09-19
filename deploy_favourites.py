import boa 
import os 
from dotenv import load_dotenv
from boa.network import NetworkEnv, EthereumRPC
from eth_account import Account 

load_dotenv()

def main():
   rpc = os.getenv("RPC_URL") 
   env = NetworkEnv(EthereumRPC(rpc))
   boa.set_env(env)

   anvil_key = os.getenv("ANVIL_KEY")
   my_account =Account.from_key(anvil_key)
   boa.env.add_account(my_account, force_eoa=True)

   favourites_contract = boa.load("favourites.vy")

   print("Storing a person")
   favourites_contract.add_person("Alice", 100)
   person_data = favourites_contract.list_of_people(0)
   print(f"Person: {person_data}")

if __name__ == "__main__":
    main()
