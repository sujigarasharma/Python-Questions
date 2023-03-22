complan_pack = int(input("Enter the number of Complan 1 kg packs purchased: "))

if 0 < complan_pack <= 500:
    free_packs = complan_pack // 5  
    if free_packs > 0:
        total_packs = complan_pack + free_packs
        if free_packs % 5 == 0:
            additional_packs = free_packs // 5
            total_packs += additional_packs
        print(f"You will get {total_packs} Complan 1 kg packs in your hand.")
    else:
        print("You did not qualify for any free packs.")
else:
    print("Invalid input. The number of Complan 1 kg packs purchased should be between 1 and 500.")
