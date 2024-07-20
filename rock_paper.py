import random 
print("======= (Rock, Paper, and Scissor game)")
b = ['Rock','Paper','Scissor']
a = input("Enter the choice (Rock, Paper, or Scissor): ")
print("You choose:", a)
c = random.choice(b)
print("Computer choose:", c)
if a == c:
    print("Result: It's a tie!")
elif a == "Paper" and c == "Rock":
    print("Result: You win!")
elif a == "Rock" and c == "Scissor":
     print("Result: You win!")
elif a == "Scissor" and c == "Paper":
     print("Result: You win!")
else:
    print("Result: Computer win!")