import random


secret_number = random.randint(1, 100)

print("Bienvenue au jeu des nombre!")
print("Devinez le nombre entre 1 et 100")

attempts = 0

while True:
   
    guess = int(input("Entrez votre nombre: "))
    attempts += 1

    if guess == secret_number:
        print(f"Félicitations! Vous avez deviné le bon nombre en {attempts} tentatives.")
        break
    elif guess < secret_number:
        print("Trop bas! Essayez encore.")
    else:
        print("Trop haut! Essayez encore.")

        
