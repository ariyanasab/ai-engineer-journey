#print("Hello Ai Engineer 🚀 ")
#name=input("what's your name ?").strip().title()
#remove whitespace frome str and capitalize user's name
#name=name.strip().title()
#capitalize user's name
#name=name.capitalize()
#capitalize title user's name
#name=name.title()
#say hello to user
#print(f"hello, {name}")

#print("Name:", "Ahmadreza", "City:", "Esfahan", sep=" | ", end=" <END>\n")

def main():
    name=input("what's your name ?")
    city=input("which city do you live in ?")
    age=input("how old are you ?")
    occupation=input("what do you do ?")
    hello(name,city,age,occupation)

def hello(name,city,age,occupatin):
    output=f"Hello , {name} , {age} years old {occupatin} from {city} city .".title()
    print(output)

main()