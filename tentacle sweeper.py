myInventory = ["rations", "bow", "sword", "tentacle sweeper", "arrows", "spears", "healing potions"]
print(myInventory)
players_choice=input("what weapons would you like to kill the tentacle sweeper:")

if players_choice in myInventory and players_choice == "tentacle sweeper":
    print("that will kill it")

elif players_choice in myInventory :
    print("that is not gonna work")

else:
    print("i don't have it")

