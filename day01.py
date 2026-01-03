import time 

def print_with_delay(text, delay=0.1):
    for char in text:
        print(char, end='', flush=True)
        time.sleep(delay)
    print()  
name = input("Enter your name:-")
if name.strip() == "":
    print("Error: Name cannot be empty.")
    exit()

try:
    age = int(input("enter your age:-"))
except ValueError:
    print ("Erorr,enter a number")
    exit()

carrier_stage=""
if age <= 18:
    carrier_stage += "student"
elif age > 18 and age<25:
    carrier_stage += "Early Professional"
else:
    carrier_stage += "professional"
city = input("Enter the city you live in:-").capitalize()

primary_skill = input("what are your primary skills:-")

print_with_delay("tell us how good you are at your skill",0.01)
try:
    skill_level = input("choose between beginner, intermediate or expert: ").lower()
    
    if skill_level not in ("beginner", "intermediate", "expert"):
        raise ValueError 
except ValueError:
    print("Error: Invalid option.")
    exit()
readiness_tag= ""
if skill_level=="beginner":
    readiness_tag += "foundation"
elif skill_level=="intermediate":
    readiness_tag += "Junior intern"
else:
    readiness_tag += "production ready"
learning_recommendation=""
if skill_level=="beginner":
    learning_recommendation += "Focus on core fundamentals and consistency"
elif skill_level=="intermediate":
    learning_recommendation += "Start building real-world projects"
else:
    learning_recommendation += "Contribute to production-grade systems"
print("=" * 45)
print("        CANDIDATE PROFILE CARD")
print("=" * 45)

print("Name          :",name)
print("Age           :",age)
print("City          :",city)
print("Primary Skill :",primary_skill)
print("Skill Level   :",skill_level)

print()
print("Career Stage  :",carrier_stage)
print("Readiness Tag :",readiness_tag)
print("Recommendation:",learning_recommendation)
print("=" * 45)

