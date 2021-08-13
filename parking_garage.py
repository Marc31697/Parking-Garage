#Parking garage program

class parking():
    """
    Put something here later
    """
    # {1 : [paid/unpaid, availability]}
    def __init__(self, tickets):
        self.tickets = tickets

    # Enter garage and take a ticket : Tae a ticket out of pool : Mark a spot as occupied
    def enterGarage(self):
        

    
    # Opens up a spot : Check if paid : Opens a ticket
    def leaveGarage(self):
    

    #Pay for ticket : Mark dict item as paid
    def payTicket(self):



# garage = parking({10})

def run():

    random = {1 : ['unpaid', 'available'],
        2 : ['unpaid', 'available'],
        3 : ['unpaid', 'available'],
        4 : ['unpaid', 'available'],
        5 : ['unpaid', 'available'],
        6 : ['unpaid', 'available'],
        7 : ['unpaid', 'available'],
        8 : ['unpaid', 'available'],
        9 : ['unpaid', 'available'],
        10 : ['unpaid', 'available'],
    }
    while True:
        response = input("What would you like to do? Enter/Leave/Pay: ")
    
        if response.lower() == 'enter':
            for x in random:
                if random[x][1] == 'available':
                    random[x][1] = 'occupied'
                    print(f'Your ticket is number {x}')
                    break

        elif response.lower() == 'leave':
            ticket = int(input("What is your ticket number? "))
            if random[ticket][0] == 'unpaid':
                print("You must pay to leave.")
            else:
                print("Thank you for coming")
                random[ticket][0] = 'unpaid'
                random[ticket][1] = 'available'

        elif response.lower() == 'pay':
            ticket = int(input("What is your ticket number? "))
            if random[ticket][0] == 'unpaid' and random[ticket][1] == 'occupied':
                paymethod = input("That will be $5 for cash or $6 for credit. What method would you like to use today?")
                if paymethod == 'cash':
                    bills = input("Please insert $5 (type $5): ")
                    if bills == '$5':
                        print("Thank you for paying. Please vacate within 15 minutes.")
                        random[ticket][0] = 'paid'
                    else:
                        print("You have entered an incorrect amount, please try again.")
                else:
                    card = input("Please insert your credit card. (type 'insert')")
                    if card == 'insert':
                        print("Payment accepted, thank you. Please vacate within 15 minutes.")
                        random[ticket][0] = 'paid'
                    else:
                        print("ERROR, please reinsert your card.")
            elif random[ticket][1] != 'occupied':
                print("Not a valid ticket number")
            else:
                print("Thank you for coming")
                random[ticket][0] = 'unpaid'
                random[ticket][1] = 'available'
        

        
run()