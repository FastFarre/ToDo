import pandas as pd
from consolemenu import *
from consolemenu.items import *
import time
def delete_task():
  df = pd.read_pickle("./todo.pkl")
  print(df)
  delete_sel = int(input("\nselect task to delete: "))
  if delete_sel > len(df.index - 1):
    print("\nthis is not a valid option. Try again.")
    delete_task()
  else:
    df = df.drop(delete_sel)
    df.to_pickle("./todo.pkl")
    print(df)

def mark_done():
  df = pd.read_pickle("./todo.pkl")
  df = df.reset_index(drop=True)
  print(df)
  done_sel = int(input("\nselect task to mark as done: "))
  if done_sel > len(df.index - 1):
    print("\nthis is not a valid option. Try again.")
    mark_done()
  else:
    if df.at[done_sel, 'Status'] == True:
      print("taak is al af. Deze wordt nu gemarkeerd als niet klaar.")
      df.at[done_sel, 'Status'] = False
      df.to_pickle("./todo.pkl")
      print(df)
    else:
      df.at[done_sel, 'Status'] = True
      df.to_pickle("./todo.pkl")
      print(df)

def add_task():
  df = pd.read_pickle("./todo.pkl")
  df = df.reset_index(drop=True)
  new_task = input("Add New Task: ")
  df.loc[len(df.index)] = [new_task, False]
  print(df)
  df.to_pickle("./todo.pkl")
def show_task():
  df = pd.read_pickle("./todo.pkl")
  df = df.reset_index(drop=True)
  print(df)
  time.sleep(3)
  
def main():
  df = pd.read_pickle("./todo.pkl")
  df = df.reset_index(drop=True)
  menu = ConsoleMenu("ToDo App", "By FastFarre")
  delete_item = FunctionItem("Delete Task", delete_task)
  mark_item_done = FunctionItem("Mark Task As Done", mark_done)
  add_item = FunctionItem("Add Task", add_task)
  show_items = FunctionItem("Show All Tasks", show_task)
  menu.append_item(show_items)
  menu.append_item(mark_item_done)
  menu.append_item(add_item)
  menu.append_item(delete_item)
  menu.show()
main()