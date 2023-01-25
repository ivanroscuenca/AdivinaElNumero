
import random 
from art import logo

EASY_LEVEL=10
HARD_LEVEL=5


# Creamos la funcion para comprobar respuesta y suposición
def check_answer(guess,answer,turns):
  if guess>answer:
    print("Demasiado alto")
    return turns-1
  elif guess<answer:
    print("Demasiado bajo")
    return turns-1
  else:
    print(f"Lo adivinaste, el número es {answer}")

# Creamos la funcion para numero de intentos segun dificultad
def set_difficulty():
  level=input("Elige nivel dificultad. Escribe 'f' para fácil, 'd' para difícil: ")
  if level=='f':
    return EASY_LEVEL
  else:
    return HARD_LEVEL


#Creamos la funcion principal
def game():
  print(logo)
  print("Bienvenido al juego adivina el número")
  turns=set_difficulty()
  print("Piensa un número del 1 al 100.")
  answer = random.randint(1, 100)
  guess=0
  while guess !=answer:
    print(f"Te quedan {turns} intentos")
    guess = int(input("Di un número del 1 al 100: "))
    turns =check_answer(guess,answer,turns)
    if turns==0:
      print("Has acabado con el numero de intentos")
      print("GAME OVER")
      return
    elif guess !=answer:
      print("Prueba otra vez")

#llamamos a la funcion principal
game()

#volver a jugar
regame = input("Quieres volver a jugar. Aprieta 's' para jugar de nuevo:")
while regame=="s" or "S":
  game()

print("GAME OVER")







