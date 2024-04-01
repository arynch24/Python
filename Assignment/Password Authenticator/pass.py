def password_validation(pass_,user_,last_pass):
    global count_cap
    global count_small
    global count_digit
    global count_spe_cha
    global repetition_flag
    global hist_pass
    global seq_flag
    
    count_cap=0
    count_small=0
    count_digit=0
    count_spe_cha=0
    repetition_flag=0
    hist_pass=0
    seq_flag=0

    for i in range (0, len(pass_)):
        if(pass_[i].isupper()):
            count_cap+=1
        if(pass_[i].islower()):
            count_small+=1
        if(pass_[i].isdigit()):
            count_digit+=1
        if(pass_[i].isalpha() or pass_[i].isdigit()):
             count_spe_cha
        else:
            count_spe_cha+=1
        if(pass_[i]==pass_[i-1]==pass_[i-2] ==pass_[i-3]==pass_[i-4] ):
            repetition_flag=1
        if(pass_[i:i+3] in user_):
            seq_flag=1

    for i in range(3):
        if(last_pass[i]==pass_):
            hist_pass=1
    
    if (len(pass_) > 10 and
    count_cap >= 2 and
    count_digit >= 2 and
    count_small >= 2 and
    count_spe_cha >= 2 and
    repetition_flag == 0 and
    hist_pass == 0 and
    seq_flag == 0):
        return True
    else:
        return False



ans=False
last_pass=[0,0,0]
while(ans==False):
    pass_=input("Enter your Password:")
    user_=input("Enter your username:")
   
    for i in range(3):
        last_pass[i]=input("Enter your last 3 passwords:")
    
    ans=password_validation(pass_,user_,last_pass)
    
    if(ans==True):
        print("Congratulations! Your Password is Valid.")
    else:
        print("Correct the following errors and retry.")
        if(count_cap<2):
            print("Please Enter at least 2 capital letters.")
        if(count_small<2):
            print("Please Enter at least 2 small letters.")
        if(count_digit<2):
            print("Please Enter at least 2 digits.")
        if(count_spe_cha<2):
            print("Please Enter at least 2 special characters.")
        if(repetition_flag==1):
            print("Your password contains more than 3 same characters in a sequence.")
        if(hist_pass==1):
            print("Your password is same as your last password.")
        if(seq_flag==1):
            print("Your username characters are matched with password.")
        
            

        


