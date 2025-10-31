print("Welcome to Come On and Reveal Your Daily Horoscope! Want to know about your Horoscope? Well come and explore about different horoscopes!")
user_name = input("Please enter your name here and we will get started! ^_^")
print("Hello",user_name,"please review all of the zodiac signs")
proceed = True
while proceed == True:
    print("""
(1) - Aries
(2) - Taurus
(3) - Gemini
(4) - Cancer
(5) - Leo
(6) - Vigro
(7) - Libra
(8) - Scorpio
(9) - Saggitarius
(10) - Capricon
(11) - Aquarius
(12) - Pisces
""")
# I have to make sure that I put every daily horoscope with their corresponding zodiac signs 
    zodiac_sign = int(input("\nPlease enter the number that associates to your Zodiac-Sign! "))

    if zodiac_sign == 1:       # This is the daily horoscope of aries
        #I did this change because I needed to know what this part of the code is
        
        print(user_name,"""Your daily horoscope is......
Friends or a group could bring new and exciting information your way,
perhaps involving career or educational opportunities. 
You might explore combining artistic talents with modern technology.
Invitations to related social events could follow. Accept as many as you can, Aries. 
They could make a difference in your personal, professional, and creative lives.""")


    elif zodiac_sign == 2:      # for taurus
        print(user_name,"""Your daily horoscope is......
Today you could decide to host a virtual party or small meeting in your home. 
You miss having a lot of visitors. 
This should be an exciting occasion, Taurus, and you could go out of your way to make this the best small event possible. 
It will probably be worth it. 
This event could bring people and information your way that make a big difference to you!""")


    elif zodiac_sign == 3:     # for gemini
        print(user_name,"""Your daily horoscope is......
Vast amounts of information could come to you through email or phone.
Expect to hear from groups. You could make new friends, Gemini, possibly in your neighborhood, as changes could be taking place in your community. 
You could hear of online classes you want to take. Books or magazines may bring valuable information. 
This could be a very stimulating and significant day.""")


    elif zodiac_sign == 4:     # for cancer
        print(user_name,"""Your daily horoscope is......
Have you been thinking about expanding your computer skills? If so, this is the day to do it. You're likely to discover a lot of valuable information, as well as shortcuts for accomplishing your goals. Happiness reigns in the home as family members exchange a lot of new and interesting ideas. This could be a very gratifying day in a lot of ways, Cancer!""")


    elif zodiac_sign == 5:     # for leo
        print(user_name,"""Your daily horoscope is......
!""")


    elif zodiac_sign == 6:     # for vigro
        print(user_name,"""Your daily horoscope is......
!""")


    elif zodiac_sign == 7:    # for libra
        print(user_name,"""Your daily horoscope is......
.""")


    elif zodiac_sign == 8:     # for scorpio
        print(user_name,"""Your daily horoscope is......
.""")


    elif zodiac_sign == 9:     # for sagittarius
        print(user_name,"""Your daily horoscope is......
!""")


    elif zodiac_sign == 10:      # for capricon
        print(user_name,"""Your daily horoscope is......
!""")


    elif zodiac_sign == 11:    # for aquarius
        print(user_name,"""Your daily horoscope is......
.""")


    else:
        print(user_name,"""Your daily horoscope is......
.""")

    temp = input("Would you like to continue again yes / no ? ")
    if temp == "yes":
        proceed = True
    else:
        proceed = False

else:
    print("\nI hope you were very excited to know about your Horoscope.",user_name,"!!")
    print("\nI hope you'll come back again to read about another amazing horoscope !!")
