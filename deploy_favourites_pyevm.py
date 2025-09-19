import boa 

def main():
    print("Let's read in the vyper code and deploy it")
    favourites_contract = boa.load('favourites.vy')

    starting_favourite_number = favourites_contract.retrieve()
    print(f"The starting favourite number is: {starting_favourite_number}") 

    favourites_contract.store(5)
    ending_favourite_number = favourites_contract.retrieve()
    print(f"The ending favourite number is: {ending_favourite_number}") 

    
if __name__ == "__main__":
    main() 
