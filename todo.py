import pandas as pd
import pickle

df = pd.read_pickle("todo.pkl")

print("todo app")
print("\n")
print("1 = nieuwe taak, 2 = verwijder taak, 3 = markeer taak als klaar")
selection = input("selecteer 1, 2 of 3: ")

if selection == 1:
  new_task = input("give your task a name: ")
elif selection == 2:
  #alle taken printen met index en laten kiezen welke weg moet
  print("wip")
elif selection == 3:
  print("wip")