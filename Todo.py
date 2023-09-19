import pandas as pd
from simple_term_menu import TerminalMenu

def menu():
    
    #main menu settings
    main_menu_items = ['Add Task', 'Mark as done', 'Remove task', 'Show tasks', 'Exit']
    main_menu = TerminalMenu(main_menu_items)
    main_menu_exit = False
    
    while not main_menu_exit:
      main_sel = main_menu.show()      
      todo_file = pd.read_csv('Todo.csv', usecols=['Status', ' Task'])
      todo_df = pd.DataFrame(todo_file)

      if main_sel == 0:
        task_input = input('Please type a task: ')
        task_row = [False, task_input]
        todo_df.loc[len(todo_df)] = task_row
        todo_df.to_csv('Todo.csv', index=True, header=True)

      elif main_sel == 1:
        print(todo_df)
        sel = int(input('Please select a task by typing its index: '))
        todo_df.at[sel, 'Status'] = True
        todo_df.to_csv('Todo.csv', index=True, header=True)
      
      elif main_sel == 2:
        print(todo_df)
        sel = int(input('Please select a task by typing its index: '))
        df2 = todo_df.drop(todo_df.index[sel])
        df2.to_csv('Todo.csv', index=True, header=True)
      
      elif main_sel == 3:
        print(todo_df)
      
      elif main_sel == 4:
        main_menu_exit = True

menu()