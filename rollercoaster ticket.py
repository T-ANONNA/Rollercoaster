print("Welcome to the rollercoaster! ")
height=int(input("What is your height in cm? "))
if height>=120:
    print("You can ride the rollercoaster ")
    age=int(input("What is your age? "))
    if age < 12:
        bill=5
        print("child tickets are $5. ")
    if age >=12 and age <=18:
        bill=7
        print("Youth tickets are $7")
    elif  45<=age<=55:
        print("Everything is going to be ok.have a free ride on us!")

    else:
        bill=12
        print("Adult tickets are $12.")   
    wants_photo=input("do you want to have a photo take? type y for yes and n for No.")
    if wants_photo =="y":
       bill+=3  
    print(f"your final bill is {bill}")     
   
else:
    print("sorry you have to grow taller before you can ride")