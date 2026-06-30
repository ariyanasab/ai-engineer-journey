"""
========== PROFILE ==========

Name : Ahmad

Age : 29

City : Esfahan

Favorite Language : Python

Dream Job : AI Engineer

=============================

"""


def main():
    Name = input("what's your name?")
    Age = int(input("how old are you ?"))
    City = input("which city do you live in ?")
    Favorite_Language = input("what your favorit programming language ?")
    Dream_Job = input("what is your dream occupation ?")
    Profile_Generator(Name, Age, City, Favorite_Language, Dream_Job)


def Profile_Generator(name, age, city, favorite_language, dream_job):
    print("========== PROFILE ==========")
    print(
        f" Name : {name} \n Age : {age} \n City : {city} \n Favorite Language : {favorite_language} \n Dream Job : {dream_job}".title()
    )
    print("=============================")
    print("Good luck on your AI Engineer Journey 🚀")
    print(f"Next year you will be {age+1} years old.")


main()
