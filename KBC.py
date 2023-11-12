# Kaun Banega Crorepati by Adnan Abdin 
# Date:- 11-11-2023

print("WELCOME TO :")
print('##############################')
print('### ||  // ||||||| ||||||| ###') 
print('### || //  ||   || ||      ###')
print('### ||//   ||||||| ||      ###')
print('### ||\\\\   ||   || ||      ###')
print('### || \\\\  ||   || ||      ###')
print('### ||  \\\\ ||||||| ||||||| ###')
print('##############################\n\n\n')


Q1 = ["Q1. What Is The National Art Of India ?\n\n**Your Options**:\n\n[01] Madhubani Painting\n[02] Tanjore Painting\n[03] Rajhasthani Painting\n[04] All Of The Above\n", 4]

Q2 = ["\n\nQ2. What Does The Traditional Indian Greeting \"Namaste\" Signify ?\n\n**Your Options**:\n\n[01] Goodbye\n[02] I bow to the divine in you\n[03] Congratulations\n[04] Have a nice day\n", 2]

Q3 = ["\n\nQ3. Which Of The Following Musical Instruments Is Commonly Associated With Hindustani Classical Music ?\n\n**Your Options**:\n\n[01] Sitar\n[02] Veena\n[03] Mridangam\n[04] Ghatam\n", 1]


while True:
    print(Q1[0])
    a = int(input("Enter The Option You Choose: "))
    if a==4:
        print("\nYou Won $1000.\n")
        print("Total Sum Of Money You Won : $1000")
        break
    else:
        print("##### You Lose ! #####")
        b = input("\nDo You Want To Replay (y or N)\n")
        if b=="y":
            continue
        else:
            print("Play The 2nd Question.")
            print("Total Money You Wiil Get $000")
            break


while True:
    print(Q2[0])
    a = int(input("Enter The Option You Choose: "))
    if a==2:
        print("\nYou Won $2000.")
        print("Total Sum Of Money You Won : $3000")
        break
    else:
        print("##### You Lose ! #####")
        b = input("\nDo You Want To Replay (y or N)\n")
        if b=="y":
            continue
        else:
            print("You Are A Faliure! Dont Play This Game Again.")
            print("Total Money You Wiil Get $000")
            break

while True:
    print(Q3[0])
    a = int(input("Enter The Option You Choose: "))
    if a==1:
        print("\nYou Won $5000.")
        print("Total Sum Of Money You Won : $8000")
        break
    else:
        print("##### You Lose ! #####")
        b = input("\nDo You Want To Replay (y or N)\n")
        if b=="y":
            continue
        else:
            print("You Are A Faliure! Dont Play This Game Again.")
            print("Total Money You Wiil Get $000")
            break







    
