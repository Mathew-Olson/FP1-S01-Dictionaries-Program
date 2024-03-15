##################################################################
# FP1-S01 - Dictionaries Program
# Mathew Thomas Olson
# 14 March 2024
##################################################################
#Dictionaries
shopping_list = {'apples': 2.56, 'pears': 10}

#Variables
progress = True


#Main code here

print("Lets create a shopping list!")
while progress == True:
    choice = int(input("""1 = Add Item
2 = Remove Item
3 = edit items
4 = View
5 = Quit
What would you like to do? """))
    
    if choice == 1: #adding items to the dictionary
        new_item = input("what would you like to add?")
        item_price = float(input("how much does that cost? $"))
        shopping_list[new_item] = item_price
    
    elif choice == 2: #removing from the dictionary
        removed_item = input("what would you like to remove?")
        while removed_item not in shopping_list:
            print("That was not in the list. Try again.")
            removed_item = input("what would you like to remove?")
        shopping_list.pop(removed_item)
        
    elif choice == 3: #changing items in the dictionary
        choice = input("what item would you like to change?\n")
        while choice not in shopping_list:
            print("that is not an option")
            choice = input("what item would you like to change?\n  ")
        which = input("""1 = change item
2 = change cost""")
        
        while which != '1' and which != '2': #making sure they use they right numbers
            print("that was not an option")
            which = input("""1 = change item
2 = change cost""")
        
        if which == '1':# changing the name but not cost (could be used fro typos)
            new_name = input("what is the new name of your item?\n")
            item_cost = shopping_list[choice]
            del shopping_list[choice]
            shopping_list[new_name] = item_cost
            print(f"Your item is now called {new_name} and costs {item_cost}.")
            pointless = input("hit enter to coninue")
            
        elif which == '2': #changing the cost but not the name
            new_cost = float(input("what is the new cost of your item?\n"))
            shopping_list[choice] = new_cost
            print(f"The new cost of {choice} is $[new_cost]")
            pointless = input("hit enter to coninue")
            
        
        
    
        
    elif choice == 4: #viewing the dictionary
        if len(shopping_list) > 0:
            print("Your list contains:")
            for i, v in shopping_list.items():
                print(i, "which costs $", v)
        print("You have", len(shopping_list), "items.")
        total_cost = sum(shopping_list.values())
        print(f"Your total cost of the items in your list is {total_cost}") 
        pointless = input("hit enter to coninue")
            
        
    elif choice == 5: #exiting
        print("Quit")
        progress = False
    
    else:
        print("that was not an option") #if they don't use the right numbers
    
    
