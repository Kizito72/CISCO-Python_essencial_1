# LET US CHECK HOW FAR WE HAVE GONE

# learner State
learner = "I believe deep down you, you are better today than you were 3 months ago."

# Self assess your learneing progress from 5 to 100 percent
learner = int(input("Input your self assessment result in percentage, Type only the figure. E.g. 20 for 20 percent: "))

#declaring variables for diferent learning progress levels in percentage 
beginner = 30   # 5% to 30%
intermediate = 60 # 31% to 60%
advance = 80 # 61% and above

# checking  progress level

if learner <= beginner and learner >= 5:
    print("\nYour learning Progrees So Far is", learner, "Percent \nTherefore your Level is BEGINNER")
    print("\nO'Yes!, You are Progressing... \nIndeed learner is a gradual process")

elif learner <= intermediate and learner > beginner:
    print("\nYour learning Progrees So Far is", learner, "Percent \nTherefore your Level is INTERMEDIATE")
    print("\nGreat!, Your Progress is impressive \nKeep the the fire burning")

elif learner > intermediate or learner >= advance:
    print("\nYour learning Progrees So Far is", learner, "Percent \nTherefore your Level is ADVANCE")
    print("\nWell Done!, Your Progress top notch \nYou are unstopable")

else:
    print("\nYour learning Progrees So Far is", learner, "Percent \nTherefore you have no level.")
    print("\nO'No!, This is not impressive \nYou need to go back to drawing board")
exit()
