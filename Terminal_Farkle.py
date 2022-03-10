from random import randint
import time


class Dice:
    def __init__(self):
        self.score = randint(1, 6)

    def __repr__(self):
       return self.score

    def __str__(self):
        if self.score == 1:
            return """
            -  -  -
            -  o  -
            -  -  -"""
        if self.score == 2:
            return """
            -  -  o
            -  -  -
            o  -  -"""
        if self.score == 3:
            return """
            -  -  o
            -  o  -
            o  -  -"""
        if self.score == 4:
            return """
            o  -  o
            -  -  -
            o  -  o"""
        if self.score == 5:
            return """
            o  -  o
            -  o  -
            o  -  o"""
        if self.score == 6:
            return """
            o  -  o
            o  -  o
            o  -  o"""

class Player:
    def __init__(self, name, score):
        self.name = name
        self.score = score
        self.thethrow = []

    def throw(self):
        print("""

        Here are the dice of {name}: 
        """.format(name = self.name))
        for i in range(6):
            rDice = Dice()
            self.thethrow.append(rDice.score) 
            print(rDice)

    def clear_the_hand(self):
        self.thethrow = []
        
def Input_validation(chosen_dice, hand): #There is a problem when I enter i.e. 1 1 or 5 5 and then something sane like 1 2
    counter = 0
    stopper_first_condition = True
    while counter != 1:
        while stopper_first_condition:
            counter = 0
            for i in range(0, len(chosen_dice)):
                if chosen_dice[i] > len(hand) or chosen_dice[i] < 1 or chosen_dice.count(chosen_dice[i]) > 1 or len(chosen_dice) > len(hand):
                    chosen_dice = input("You've chosen the devil's dice, the one that does not exist in our world. There's still a chance to choose again: ").strip().split(" ") 
                    for i in range(0, len(chosen_dice)):
                        chosen_dice[i] = int(chosen_dice[i])
            final_checker = 0 
            for i in range(0, len(chosen_dice)):
                if chosen_dice[i] < 7 and chosen_dice[i] > 0 and chosen_dice.count(chosen_dice[i]) == 1:
                    final_checker += 1
            if final_checker == len(chosen_dice):
                counter += 1
                stopper_first_condition = False
            else:
                print("Something is wrong with your pick")
    return chosen_dice


def Throw_of_the_dice(Player1):
    # print("Welcome, {name1} and {name2}. Sit yourself for a game of Farkle! On the edge of your seat that is... prepare to throw the dice.".format(name1 = Player1.name, name2 = Player2.name))
    # print("It's {name1}'s turn. ".format(name1 = Player1.name))
    Player1.throw()
    print("""
    Your throw consists of """, Player1.thethrow)
    hand = Player1.thethrow 
    ########################################################
    #hand = [1, 2, 3, 4, 5, 1] #TEST
    ########################################################
    chosen_dice = input("Please pick your dice. Input numbers of your selected dice in a format \"1 2 6\" here: ").strip().split(" ")
    #print(chosen_dice)
    for i in range(0, len(chosen_dice)):
        chosen_dice[i] = int(chosen_dice[i])
    #print(chosen_dice)

    chosen_dice = Input_validation(chosen_dice, hand)
    
    #Shifting the chosen dice to indices:
    for i in range(0, len(chosen_dice)):
        chosen_dice[i] = chosen_dice[i] -1
    #print(chosen_dice)
    chosen_dice_values = []
    for each_dice_number in chosen_dice:
        chosen_dice_values.append(hand[each_dice_number])
    print("Chosen dice values: ", chosen_dice_values)
    #Now, the rules.
    turn_continues = True
    #Check if it's a full straight
    while turn_continues == True:
        counter_full_straight = 0
        counter_partial_straight = 0
        for i in range(0, len(chosen_dice)):
            if hand.count(hand[chosen_dice[i]]) == 1:
                counter_full_straight += 1
            # if hand.count(hand[chosen_dice[i]]) == 2:
            #     counter_partial_straight += 1
        if counter_full_straight == 6:
            Player1.score += 1500
            print("Congratulations are due! You've got a full straight! {name}'s score now is {score}".format(name = Player1.name, score = Player1.score))
            dice_to_remove = []
            for chosen_one in chosen_dice:
                dice_to_remove.append(hand[chosen_one]) 
            for each_dice_to_remove in dice_to_remove:
                hand.remove(each_dice_to_remove)
            print("Your hand is now empty. But you're entitled to another throw.")
            stop_the_turn = input("Do you want to continue your turn? (Y/N)").upper()
            if stop_the_turn == "N":
                turn_continues = False #If he says Y the dice should be thrown again
            else:
                Player1.clear_the_hand()
                Player1.throw()
                hand = Player1.thethrow
                print("""
                Your throw consists of """, hand)

                chosen_dice = input("Please pick your dice. Input numbers of your selected dice in a format \"1 2 6\" here: ").strip().split(" ")
                for i in range(0, len(chosen_dice)):
                    chosen_dice[i] = int(chosen_dice[i])

                chosen_dice = Input_validation(chosen_dice, hand)

                for i in range(0, len(chosen_dice)):
                    chosen_dice[i] = chosen_dice[i] -1
                chosen_dice_values = []
                for each_dice_number in chosen_dice:
                    chosen_dice_values.append(hand[each_dice_number])
                print("Chosen dice values: ", chosen_dice_values)


            #if it's a partial straight 1-5
        elif counter_full_straight == 4 and len(chosen_dice) == 5 and chosen_dice_values.count(1) == 1:
            Player1.score += 500 
            print("You've got a partial 1-5 straight! {name}'s score now is {score}".format(name = Player1.name, score = Player1.score))
            dice_to_remove = []
            for chosen_one in chosen_dice:
                dice_to_remove.append(hand[chosen_one]) 
            for each_dice_to_remove in dice_to_remove:
                hand.remove(each_dice_to_remove)
            print("""
                Your throw consists of """, hand)
            stop_the_turn = input("Do you want to continue your turn? (Y/N)").upper()
            if stop_the_turn == "N":
                turn_continues = False
            else:
                if len(hand) == 0:
                    Player1.clear_the_hand()
                    Player1.throw()
                    hand = Player1.thethrow
                    print("""
                    Your throw consists of """, hand)
                
                chosen_dice = input("Please pick your dice. Input numbers of your selected dice in a format \"1 2 6\" here: ").strip().split(" ")
                for i in range(0, len(chosen_dice)):
                    chosen_dice[i] = int(chosen_dice[i])

                chosen_dice = Input_validation(chosen_dice, hand)

                for i in range(0, len(chosen_dice)):
                    chosen_dice[i] = chosen_dice[i] -1
                chosen_dice_values = []
                for each_dice_number in chosen_dice:
                    chosen_dice_values.append(hand[each_dice_number])
                print("Chosen dice values: ", chosen_dice_values)

        elif counter_full_straight == 4 and len(chosen_dice) == 5 and chosen_dice_values.count(1) == 0:
            Player1.score += 750 
            print("You've got a partial 2-6 straight! {name}'s score now is {score}".format(name = Player1.name, score = Player1.score))
            dice_to_remove = []
            for chosen_one in chosen_dice:
                dice_to_remove.append(hand[chosen_one]) 
            for each_dice_to_remove in dice_to_remove:
                hand.remove(each_dice_to_remove)
            print("""
                Your throw consists of """, hand)
            stop_the_turn = input("Do you want to continue your turn? (Y/N)").upper()
            if stop_the_turn == "N":
                turn_continues = False

            else:
                if len(hand) == 0:
                    Player1.clear_the_hand()
                    Player1.throw()
                    hand = Player1.thethrow
                    print("""
                    Your throw consists of """, hand)
                
                chosen_dice = input("Please pick your dice. Input numbers of your selected dice in a format \"1 2 6\" here: ").strip().split(" ")
                for i in range(0, len(chosen_dice)):
                    chosen_dice[i] = int(chosen_dice[i])

                chosen_dice = Input_validation(chosen_dice, hand)

                for i in range(0, len(chosen_dice)):
                    chosen_dice[i] = chosen_dice[i] -1
                chosen_dice_values = []
                for each_dice_number in chosen_dice:
                    chosen_dice_values.append(hand[each_dice_number])
                print("Chosen dice values: ", chosen_dice_values)
        

        elif len(chosen_dice) == 3 and chosen_dice_values.count(chosen_dice_values[0]) == 3:
            if chosen_dice_values[0] == 1:
                Player1.score += 1000
                print("You've got three ones! {name}'s score now is {score}".format(name = Player1.name, score = Player1.score))
                dice_to_remove = []
                for chosen_one in chosen_dice:
                    dice_to_remove.append(hand[chosen_one]) 
                for each_dice_to_remove in dice_to_remove:
                    hand.remove(each_dice_to_remove)
                print("""
                Your throw consists of """, hand)
                stop_the_turn = input("Do you want to continue your turn? (Y/N)").upper()
                if stop_the_turn == "N":
                    turn_continues = False
                else:
                    if len(hand) == 0:
                        Player1.clear_the_hand()
                        Player1.throw()
                        hand = Player1.thethrow
                        print("""
                        Your throw consists of """, hand)

                    chosen_dice = input("Please pick your dice. Input numbers of your selected dice in a format \"1 2 6\" here: ").strip().split(" ")
                    for i in range(0, len(chosen_dice)):
                        chosen_dice[i] = int(chosen_dice[i])

                    chosen_dice = Input_validation(chosen_dice, hand)

                    for i in range(0, len(chosen_dice)):
                        chosen_dice[i] = chosen_dice[i] -1
                    chosen_dice_values = []
                    for each_dice_number in chosen_dice:
                        chosen_dice_values.append(hand[each_dice_number])
                    print("Chosen dice values: ", chosen_dice_values)
            else:
                Player1.score += (100*chosen_dice_values[0])
                print("You've got three of a kind! {name}'s score now is {score}".format(name = Player1.name, score = Player1.score))
                dice_to_remove = []
                for chosen_one in chosen_dice:
                    dice_to_remove.append(hand[chosen_one]) 
                for each_dice_to_remove in dice_to_remove:
                    hand.remove(each_dice_to_remove)
                print("""
                Your throw consists of """, hand)
                stop_the_turn = input("Do you want to continue your turn? (Y/N)").upper()
                if stop_the_turn == "N":
                    turn_continues = False
                else:
                    if len(hand) == 0:
                        Player1.clear_the_hand()
                        Player1.throw()
                        hand = Player1.thethrow
                        print("""
                        Your throw consists of """, hand)
                
                    chosen_dice = input("Please pick your dice. Input numbers of your selected dice in a format \"1 2 6\" here: ").strip().split(" ")
                    for i in range(0, len(chosen_dice)):
                        chosen_dice[i] = int(chosen_dice[i])

                    chosen_dice = Input_validation(chosen_dice, hand)

                    for i in range(0, len(chosen_dice)):
                        chosen_dice[i] = chosen_dice[i] -1
                    chosen_dice_values = []
                    for each_dice_number in chosen_dice:
                        chosen_dice_values.append(hand[each_dice_number])
                    print("Chosen dice values: ", chosen_dice_values)
                    
        elif len(chosen_dice) == 4 and chosen_dice_values.count(chosen_dice_values[0]) == 4:
            Player1.score += chosen_dice_values[0]*100*2 
            print("You've got four of a kind! {name}'s score now is {score}".format(name = Player1.name, score = Player1.score))
            dice_to_remove = []
            for chosen_one in chosen_dice:
                dice_to_remove.append(hand[chosen_one]) 
            for each_dice_to_remove in dice_to_remove:
                hand.remove(each_dice_to_remove)
            print("""
                Your throw consists of """, hand)
            stop_the_turn = input("Do you want to continue your turn? (Y/N)").upper()
            if stop_the_turn == "N":
                turn_continues = False

            else:
                if len(hand) == 0:
                    Player1.clear_the_hand()
                    Player1.throw()
                    hand = Player1.thethrow
                    print("""
                    Your throw consists of """, hand)

                chosen_dice = input("Please pick your dice. Input numbers of your selected dice in a format \"1 2 6\" here: ").strip().split(" ")
                for i in range(0, len(chosen_dice)):
                    chosen_dice[i] = int(chosen_dice[i])

                chosen_dice = Input_validation(chosen_dice, hand)

                for i in range(0, len(chosen_dice)):
                    chosen_dice[i] = chosen_dice[i] -1
                chosen_dice_values = []
                for each_dice_number in chosen_dice:
                    chosen_dice_values.append(hand[each_dice_number])
                print("Chosen dice values: ", chosen_dice_values)

        elif len(chosen_dice) == 5 and chosen_dice_values.count(chosen_dice_values[0]) == 5:
            Player1.score += chosen_dice_values[0]*100*4 
            print("You've got five of a kind! {name}'s score now is {score}".format(name = Player1.name, score = Player1.score))
            dice_to_remove = []
            for chosen_one in chosen_dice:
                dice_to_remove.append(hand[chosen_one]) 
            for each_dice_to_remove in dice_to_remove:
                hand.remove(each_dice_to_remove)
            print("""
                Your throw consists of """, hand)
            stop_the_turn = input("Do you want to continue your turn? (Y/N)").upper()
            if stop_the_turn == "N":
                turn_continues = False

            else:

                if len(hand) == 0:
                    Player1.clear_the_hand()
                    Player1.throw()
                    hand = Player1.thethrow
                    print("""
                    Your throw consists of """, hand)
            
                chosen_dice = input("Please pick your dice. Input numbers of your selected dice in a format \"1 2 6\" here: ").strip().split(" ")
                for i in range(0, len(chosen_dice)):
                    chosen_dice[i] = int(chosen_dice[i])

                chosen_dice = Input_validation(chosen_dice, hand)

                for i in range(0, len(chosen_dice)):
                    chosen_dice[i] = chosen_dice[i] -1
                chosen_dice_values = []
                for each_dice_number in chosen_dice:
                    chosen_dice_values.append(hand[each_dice_number])
                print("Chosen dice values: ", chosen_dice_values) 

        elif len(chosen_dice) == 6 and chosen_dice_values.count(chosen_dice_values[0]) == 6:
            Player1.score += chosen_dice_values[0]*100*8 
            print("You've got six of a kind! {name}'s score now is {score}".format(name = Player1.name, score = Player1.score))
            dice_to_remove = []
            for chosen_one in chosen_dice:
                dice_to_remove.append(hand[chosen_one]) 
            for each_dice_to_remove in dice_to_remove:
                hand.remove(each_dice_to_remove)
            print("""
                Your throw consists of """, hand)
            stop_the_turn = input("Do you want to continue your turn? (Y/N)").upper()
            if stop_the_turn == "N":
                turn_continues = False

            else:
                
                if len(hand) == 0:
                    Player1.clear_the_hand()
                    Player1.throw()
                    hand = Player1.thethrow
                    print("""
                    Your throw consists of """, hand)

                chosen_dice = input("Please pick your dice. Input numbers of your selected dice in a format \"1 2 6\" here: ").strip().split(" ")
                for i in range(0, len(chosen_dice)):
                    chosen_dice[i] = int(chosen_dice[i])

                chosen_dice = Input_validation(chosen_dice, hand)

                for i in range(0, len(chosen_dice)):
                    chosen_dice[i] = chosen_dice[i] -1
                chosen_dice_values = []
                for each_dice_number in chosen_dice:
                    chosen_dice_values.append(hand[each_dice_number])
                print("Chosen dice values: ", chosen_dice_values)

            
        elif len(chosen_dice) == 1 and chosen_dice_values[0] == 1:
            Player1.score += 100

            print("Just a single dice for a hundred! {name}'s score now is {score}".format(name = Player1.name, score = Player1.score))
            dice_to_remove = []
            for chosen_one in chosen_dice:
                dice_to_remove.append(hand[chosen_one]) 
            for each_dice_to_remove in dice_to_remove:
                hand.remove(each_dice_to_remove)
            print("""
                Your throw consists of """, hand)
            stop_the_turn = input("Do you want to continue your turn? (Y/N)").upper()
            if stop_the_turn == "N":
                turn_continues = False
                break

            else:

                if len(hand) == 0:
                    Player1.clear_the_hand()
                    Player1.throw()
                    hand = Player1.thethrow
                    print("""
                    Your throw consists of """, hand)
                
                chosen_dice = input("Please pick your dice. Input numbers of your selected dice in a format \"1 2 6\" here: ").strip().split(" ")
                for i in range(0, len(chosen_dice)):
                    chosen_dice[i] = int(chosen_dice[i])

                chosen_dice = Input_validation(chosen_dice, hand)

                for i in range(0, len(chosen_dice)):
                    chosen_dice[i] = chosen_dice[i] -1
                chosen_dice_values = []
                for each_dice_number in chosen_dice:
                    chosen_dice_values.append(hand[each_dice_number])
                print("Chosen dice values: ", chosen_dice_values)

        elif len(chosen_dice) == 1 and chosen_dice_values[0] == 5:
            Player1.score += 50

            print("Just a single dice for a fifty! {name}'s score now is {score}".format(name = Player1.name, score = Player1.score))
            dice_to_remove = []
            for chosen_one in chosen_dice:
                dice_to_remove.append(hand[chosen_one]) 
            for each_dice_to_remove in dice_to_remove:
                hand.remove(each_dice_to_remove)
            print("""
                Your throw consists of """, hand)
            stop_the_turn = input("Do you want to continue your turn? (Y/N)").upper()
            if stop_the_turn == "N":
                turn_continues = False
                break

            else:
                
                if len(hand) == 0:
                    Player1.clear_the_hand()
                    Player1.throw()
                    hand = Player1.thethrow
                    print("""
                    Your throw consists of """, hand)

                chosen_dice = input("Please pick your dice. Input numbers of your selected dice in a format \"1 2 6\" here: ").strip().split(" ")
                for i in range(0, len(chosen_dice)):
                    chosen_dice[i] = int(chosen_dice[i])

                chosen_dice = Input_validation(chosen_dice, hand)

                for i in range(0, len(chosen_dice)):
                    chosen_dice[i] = chosen_dice[i] -1
                chosen_dice_values = []
                for each_dice_number in chosen_dice:
                    chosen_dice_values.append(hand[each_dice_number])
                print("Chosen dice values: ", chosen_dice_values)
        elif len(chosen_dice) == 1 and chosen_dice_values[0] != 5 and chosen_dice_values[0] != 1:
            print("Bitch that's nothing")
            stop_the_turn = input("Do you want to continue your pathetic turn? (Y/N)").upper()
            if stop_the_turn == "N":
                turn_continues = False
                break


            chosen_dice = input("Please pick your dice AGAIN, dummy. Input numbers of your selected dice in a format \"1 2 6\" here: ").strip().split(" ")
            for i in range(0, len(chosen_dice)):
                chosen_dice[i] = int(chosen_dice[i])

            chosen_dice = Input_validation(chosen_dice, hand)

            for i in range(0, len(chosen_dice)):
                chosen_dice[i] = chosen_dice[i] -1
            chosen_dice_values = []
            for each_dice_number in chosen_dice:
                chosen_dice_values.append(hand[each_dice_number])
            print("Chosen dice values: ", chosen_dice_values)


        else:
            if len(hand) != 0:
                print("Your dice has no winning combinations.")
                turn_continues = False
            if hand == []:
                Player1.clear_the_hand()
                Player1.throw()
                hand = Player1.thethrow
                print("""
                Your throw consists of """, hand)

                chosen_dice = input("Please pick your dice. Input numbers of your selected dice in a format \"1 2 6\" here: ").strip().split(" ")
                for i in range(0, len(chosen_dice)):
                    chosen_dice[i] = int(chosen_dice[i])
                chosen_dice = Input_validation(chosen_dice, hand)

                for i in range(0, len(chosen_dice)):
                    chosen_dice[i] = chosen_dice[i] -1
                chosen_dice_values = []
                for each_dice_number in chosen_dice:
                    chosen_dice_values.append(hand[each_dice_number])
                print("Chosen dice values: ", chosen_dice_values)
                
        
    #End of the turn
    print("""
______________________________________________________
{Player} overall score for this turn is {Players_score}
------------------------------------------------------
""".format(Player = Player1.name, Players_score = Player1.score))
    


#The game script
print("""_______________________
TERMINAL FARKLE — KINGDOM COME GAME
© Strogonov V. a.k.a. Rattlehead90
2022
--------------------------------------------------""")
time.sleep(2)

print("""_-_-_-_-RULES-_-_-_-_


Six dice are thrown and the players alternate turns. Points are gained for every 1 or 5 thrown, and for three or more of a kind of any other number. Scoring is as follows:

a single 1 is worth 100 points;
a single 5 is worth 50 points;
three of a kind is worth 100 points multiplied by the given number, e.g. three 4s are worth 400 points;
three 1's are worth 1,000 points;
four or more of a kind is worth double the points of three of a kind, so four 4s are worth 800 points, five 4s are worth 1,600 points etc.
full straight 1-6 is worth 1500 points.
partial straight 1-5 is worth 500 points.
partial straight 2-6 is worth 750 points.
""")

input("Type in anything to start")

name1 = input("Hello, welcome to the game of farkle. First player, introduce yourself.")
print("Nice to meet you, {name}.".format(name = name1))
time.sleep(3)
name2 = input("And the second player goes by the name of..?")
print("It's a pleasure, {name}.".format(name = name2))
time.sleep(3)
print("Let's throw the dice! It's {name}'s turn.".format(name = name1))
time.sleep(3)
Ja = Player(name1, 0)
Ty = Player(name2, 0)

while Ja.score < 4000 and Ty.score < 4000:
    time.sleep(2)

    Throw_of_the_dice(Ja)

    Ja.clear_the_hand() 

    if Ja.score >= 4000:
        break

    print("Now, let's see, how {name} will do!".format(name = name2))

    time.sleep(2)

    Throw_of_the_dice(Ty)

    Ty.clear_the_hand()

    time.sleep(2)

    if Ty.score >= 4000:
        break

    print("Now, let's see, how {name} will do!".format(name = name1))

    

if Ja.score >= Ty.score: 
    print("Congratulations, {name}, you win the game. The scores are {scorewin} - {scorelose}".format(name = name1, scorewin = Ja.score, scorelose = Ty.score))
else:
    print("Congratulations, {name}, you win the game. The scores are {scorewin} - {scorelose}".format(name = name2, scorewin = Ty.score, scorelose = Ja.score))

input("Type in anything to exit.")
