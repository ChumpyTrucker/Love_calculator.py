print("Welcome to the love calculator\n")
name1 = input("What is your name?\n")
name2 = input( "What is their name?\n")

pair_name = name1 + name2
lower_pair_name = pair_name.lower()

t = lower_pair_name.count("t")
r = lower_pair_name.count("r")
u = lower_pair_name.count("u")
e = lower_pair_name.count ("e")

t1 = t + r + u + e

l = lower_pair_name.count("l")
o = lower_pair_name.count("o")
v = lower_pair_name.count("v")
e = lower_pair_name.count("e")

t2 = l + o + v + e

love_formula = str(t1) + str(t2)

score = int(love_formula)

if score < 10 or score > 90:
    print(f"Your score is {love_formula},  you go together like coke and mentos. ")
elif score >= 40 and score <= 50:
    print(f"Your score is {score}, you are alright together. ")
else:
    print(f"Your score is {score}. ")
