s = input("enter a string to start ")
course = input("enter a course name ")
service = input("enter a service name ")
if s == "pwskills":
    if course == "DSA":
        print("yes its available under pwskills and in multiple mode for job prepratoin and core concept ")
    elif course == "Blockchain":
        print("this is not aviable as of now , kindly raise your demand and we will fulfil in 60 days ")
    elif course == "FSDS":
        print("yes its availble , you can start learning ")
    else :
        print("this course is not availble kindly raise your demand ")
elif s  == "pwskillsservice":
    if service == "courserequest":
        print("*NOTE: Dear Learner, you can raise demand related to any new course, and we will fulfil your need in the next 60 days.")
    elif service == "module" :
        print("*NOTE: Dear Learner, you can raise demand related to any new course module, and we will fulfil your need in the next 30 days.")
    elif service == "doubt":
        print("*NOTE: Dear Learner, you can raise demand related to any doubt clearing, and we will fulfil your need in the next 24 hours.")
    elif service == "workwithus":
        print("*NOTE: Dear Learner, you can raise the demand to work with our team; our HR will evaluate and get back to you in 24 hours.")
    else :
        print("kindly provide us your feedback and we will fulfil")
else :
    print("kindly connect with our team ")