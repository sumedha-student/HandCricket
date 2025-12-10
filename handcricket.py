import random
syscore=0
score=0
symb={1:" 1️⃣",2:" 2️⃣",3:" 3️⃣",4:" 4️⃣",5:" 5️⃣",6:" 6️⃣",7:" 7️⃣",8:" 8️⃣",9: " 9️⃣",10:" 🔟"}
while True:
    user=int(input("Enter the number of runs you want to bat : "))
    system=random.randint(1,10)
    print("Current runs you scored",symb[user])
    print("Current System's bowling choice ",symb[system])
    score+=user
        
    if system==user:
        print("OUT!")
        print("System will bat")
        while True:
            system=random.randint(1,10)
            user=int(input("Enter the number of runs you want to bowl : "))
            syscore+=system
            print("Current System score ",symb[system])
            print("Current user's bowling choice",symb[user])
            if system==user:
                print("System OUT!")
                break
                
            else:
                syscore+=system
                continue
        break
    
if score > syscore:
    print(f"YOU WON by {score - syscore} runs")
else:
    print(f"SYSTEM WON by {score - syscore} runs")

print(f"Your score: {score}")
print(f"System's score: {syscore}")



