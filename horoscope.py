print("Welcome to Come On and Reveal Your Daily Horoscope! Want to know about your Horoscope? Well come and explore about different horoscopes!")
user_name = input("Please enter your Personality type here and we will get started! ^_^")
print("Hello",user_name,"please review all of the zodiac signs")

def personality_test():
    proceed = ["INTJ", "INTP", "ENTJ", "ENTP","INFJ", "INFP", "ENFJ", "ENFP","ISTJ", "ISFJ", "ESTJ", "ESFJ","ISTP", "ISFP", "ESTP", "ESFP"]
    while proceed == True:
        print("""
    (1) - INTJ
    (2) - INTP
    (3) - ENTJ
    (4) - ENTP
    (5) - INFJ
    (6) - INFP
    (7) - ENFJ
    (8) - ENFP
    (9) - ISTJ
    (10) - ISFJ
    (11) - ESTJ
    (12) - ESFJ
    (13) - ISTP
    (14) - ISFP
    (15) - ESTP
    (16) - ESFP
    """)
    if user_name.upper() == proceed[0]:
        print("Best Match: ENFP\nWhy? ENFPs bring emotional warmth and flexibility to the INTJ’s structured, strategic mindset. They complement each others' weak spots and both value deep intellectual connection.")
    elif user_name.upper() == proceed[1]:
        print("Best Match: ENTJ\nWhy? ENTJs provide structure and drive that help INTPs actualize ideas, while INTPs provide creativity and analysis. They stimulate each other intellectually.")
    elif user_name.upper() == proceed[2]:
        print("Best Match: INTP\nWhy? INTPs balance the ENTJ’s intensity with curiosity and logic. ENTJs appreciate INTPs' depth of thought and novel ideas.")
    elif user_name.upper() == proceed[3]:
        print("Best Match: INFJ\nWhy? INFJs stabilize ENTPs' chaotic energy while appreciating their creativity. Both are visionary and growth-focused.")
    elif user_name.upper() == proceed[4]:
        print("Best Match: ENFP\nWhy? ENFPs bring warmth and spontaneity that INFJs need, while INFJs provide grounding and emotional insight. Both share intuition and deep values.")
    elif user_name.upper() == proceed[5]:
        print("Best Match: ENFJ\nWhy? ENFJs help INFPs express their feelings and goals externally, while INFPs give ENFJs a gentle emotional refuge. Both value authenticity and connection.")
    elif user_name.upper() == proceed[6]:
        print("Best Match: INFP\nWhy? INFPs offer emotional depth and individuality, balancing the ENFJ’s leadership and empathy. They communicate well and share values.")
    elif user_name.upper() == proceed[7]:
        print("Best Match: INTJ\nWhy? INTJs offer stability and focus to ENFPs’ enthusiasm, while ENFPs help INTJs open up emotionally and explore possibilities.")
    elif user_name.upper() == proceed[8]:
        print("Best Match: ESFP\nWhy? ESFPs bring spontaneity and warmth to the ISTJ’s structured, responsible nature. ISTJs provide stability and reliability in return.")
    elif user_name.upper() == proceed[9]:
        print("Best Match: ESFP\nWhy? ESFPs help ISFJs loosen up and try new things, while ISFJs offer loyalty, harmony, and emotional support. Both focus on people and experiences.")
    elif user_name.upper() == proceed[10]:
        print("Best Match: ISTP\nWhy? ISTPs bring calm problem-solving and flexibility that balance the ESTJ’s drive and structure. Both value efficiency and practicality.")
    elif user_name.upper() == proceed[11]:
        print("Best Match: ISFP\nWhy? ISFPs offer creativity and emotional depth, balancing ESFJs’ social energy and caretaking tendencies. Both value harmony and connection.")
    elif user_name.upper() == proceed[12]:
        print("Best Match: ESTJ\nWhy? ESTJs provide direction and decisiveness that complement ISTPs’ independence and adaptability. Both are logical and action-oriented.")
    elif user_name.upper() == proceed[13]:
        print("Best Match: ESFJ\nWhy? ESFJs bring structure and warmth that help ISFPs feel supported, while ISFPs add creativity and emotional sensitivity to the relationship.")
    elif user_name.upper() == proceed[14]:
        print("Best Match: ISFJ\nWhy? ISFJs provide grounding and emotional steadiness to ESTPs’ energetic lifestyle. ESTPs help ISFJs explore new experiences.")
    elif user_name.upper() == proceed[15]:
        print("Best Match: ISTJ\nWhy? ISTJs offer reliability and structure, balancing ESFPs’ spontaneity and fun. Both value real-world experiences and practicality.")
    else:
        print("Sorry, that personality type is not recognized.")

personality_test()

