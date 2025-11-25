print("Welcome to MATCHBOX. Find your perfect personality partner! (please complete Meyers Briggs 16 Personality test prior)")
user = input("Enter your First Name:")
last = input("Enter your Last Name:")
user_info = []
proceed = ["INTJ", "INTP", "ENTJ", "ENTP","INFJ", "INFP", "ENFJ", "ENFP","ISTJ", "ISFJ", "ESTJ", "ESFJ","ISTP", "ISFP", "ESTP", "ESFP"]
def profile_match():
    print('-------- User profile creation: ------')
    age = input("enter your age:")
    meyers_profile = input("enter your personality type:")
    profile = []
    profile.append(user)
    profile.append(last)
    profile.append(age)
    profile.append(meyers_profile)
    user_info.append(profile)

    print("\nProfile created successfully!")
    print("Current user database:", user_info)   

profile_match()

intro= print("ATTENTION", user , last ,"STARTING MATCH MAKING")

def personality_test():
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
    mbti = input("Type your 4-letter personality: ").upper()
    if mbti == proceed[0]:
        print(user, "Your best personality match: ENFP\nWhy? ENFPs bring emotional warmth and flexibility to the INTJ’s structured, strategic mindset. They complement each others' weak spots and both value deep intellectual connection.")
    elif mbti == proceed[1]:
        print(user, "Your best personality match: ENTJ\nWhy? ENTJs provide structure and drive that help INTPs actualize ideas, while INTPs provide creativity and analysis. They stimulate each other intellectually.")
    elif mbti == proceed[2]:
        print(user, "Your best personality match: INTP\nWhy? INTPs balance the ENTJ’s intensity with curiosity and logic. ENTJs appreciate INTPs' depth of thought and novel ideas.")
    elif mbti == proceed[3]:
        print(user, "Your best personality match: INFJ\nWhy? INFJs stabilize ENTPs' chaotic energy while appreciating their creativity. Both are visionary and growth-focused.")
    elif mbti == proceed[4]:
        print(user, "Your best personality match: ENFP\nWhy? ENFPs bring warmth and spontaneity that INFJs need, while INFJs provide grounding and emotional insight. Both share intuition and deep values.")
    elif mbti == proceed[5]:
        print(user, "Your best personality match: ENFJ\nWhy? ENFJs help INFPs express their feelings and goals externally, while INFPs give ENFJs a gentle emotional refuge. Both value authenticity and connection.")
    elif mbti == proceed[6]:
        print(user, "Your best personality match: INFP\nWhy? INFPs offer emotional depth and individuality, balancing the ENFJ’s leadership and empathy. They communicate well and share values.")
    elif mbti == proceed[7]:
        print(user, "Your best personality match: INTJ\nWhy? INTJs offer stability and focus to ENFPs’ enthusiasm, while ENFPs help INTJs open up emotionally and explore possibilities.")
    elif mbti == proceed[8]:
        print(user, "Your best personality match: ESFP\nWhy? ESFPs bring spontaneity and warmth to the ISTJ’s structured, responsible nature. ISTJs provide stability and reliability in return.")
    elif mbti == proceed[9]:
        print(user, "Your best personality match: ESFP\nWhy? ESFPs help ISFJs loosen up and try new things, while ISFJs offer loyalty, harmony, and emotional support. Both focus on people and experiences.")
    elif mbti == proceed[10]:
        print(user, "Your best personality match: ISTP\nWhy? ISTPs bring calm problem-solving and flexibility that balance the ESTJ’s drive and structure. Both value efficiency and practicality.")
    elif mbti == proceed[11]:
        print(user, "Your best personality match: ISFP\nWhy? ISFPs offer creativity and emotional depth, balancing ESFJs’ social energy and caretaking tendencies. Both value harmony and connection.")
    elif mbti == proceed[12]:
        print(user, "Your best personality match: ESTJ\nWhy? ESTJs provide direction and decisiveness that complement ISTPs’ independence and adaptability. Both are logical and action-oriented.")
    elif mbti == proceed[13]:
        print(user, "Your best personality match: ESFJ\nWhy? ESFJs bring structure and warmth that help ISFPs feel supported, while ISFPs add creativity and emotional sensitivity to the relationship.")
    elif mbti == proceed[14]:
        print(user, "Your best personality match: ISFJ\nWhy? ISFJs provide grounding and emotional steadiness to ESTPs’ energetic lifestyle. ESTPs help ISFJs explore new experiences.")
    elif mbti == proceed[15]:
        print(user, "Your best personality match: ISTJ\nWhy? ISTJs offer reliability and structure, balancing ESFPs’ spontaneity and fun. Both value real-world experiences and practicality.")
    else:
        print("Sorry, that personality type is not recognized.")

personality_test()

print("Thank you for using MATCHBOX by Kirstyn Navarro. Goodbye!")