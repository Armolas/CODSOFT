import random
rock = """
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
"""
paper = """
     _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)
"""
scissors = """
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
"""

score = 0
comp_score = 0
print("Rock Paper Scissors!\nCan you beat me?")
while True:
    play = (input("type '0' for rock, '1' for paper and '2' for scissors or any other key to exit: "))
    if play == '0':
        print(rock)
    elif play == '1':
        print(paper)
    elif play == '2':
        print(scissors)
    else:
        break
    computer = random.randint(0, 2)
    print(f"Computer chose {computer}")
    if computer == 0:
        print(rock)
    elif computer == 1:
        print(paper)
    elif computer == 2:
        print(scissors)
    if play == computer:
        print("It's a draw! :|")
    elif play == '0' and computer == 2:
        print("You Win! :)")
        score += 1
    elif play == '1' and computer == 0:
        print("You Win! :)")
        score += 1
    elif play == '2' and computer == 1:
        print("You Win! :)")
        score += 1
    else:
        print("You Lose! :(")
        comp_score += 1
    print("\n---------------SCORE------------------")
    print(f"\tplayer {score} : computer {comp_score}")
    print("--------------------------------------")