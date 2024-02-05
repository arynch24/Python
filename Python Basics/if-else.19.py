coursework1 = input("Input coursework1 name ")
score_theory1 = int(input("input score_theory1 "))
score_practical1 = int(input("input score_practical1 "))
coursework2 = input("Input coursework2 name ")
score_theory2 = int(input("input score_theory2 "))
score_practical2 = int(input("input score_practical2 "))
if(coursework1 == "English" or coursework1 == "english"):
    if(score_theory1 >70):
        print("Invalid input")
    elif(score_practical1>70):
        print("Invalid input")
    else:
        print("Sum of theory and practical in english ",score_theory1+score_practical1)
if(coursework2 == "Science" or coursework2 == "science"):
    if(score_theory2 >70):
        print("Invalid input")
    elif(score_practical2>70):
        print("Invalid input")
    else:
        print("Sum of theory and practical in Science",score_theory2+score_practical2)
else:
    print("coursework not recognized")
