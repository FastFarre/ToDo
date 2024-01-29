import pandas as pd

print("todo app")

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
    delete_task()
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

def main():
  df = pd.read_pickle("./todo.pkl")
  df = df.reset_index(drop=True)
  print("\n1 = nieuwe taak, 2 = verwijder taak, 3 = markeer taak als klaar, 4 = toon alle taken, 5 = sluit programma")
  selection = int(input("selecteer 1, 2, 3 of 4: "))
  if selection == 1:
    new_task = input("give your task a name: ")
    df.loc[len(df.index)] = [new_task, False]
    print(df)
    df.to_pickle("./todo.pkl")
    main()
  elif selection == 2:
    delete_task()
    main()
  elif selection == 3:
    mark_done()
    main()
  elif selection == 4:
    print(df)
    main()
  elif selection == 5:
    exit()
  else:
    print("not a valid option. Try again")
main()