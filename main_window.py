import sys
sys.path.append(r'C:\Users\user\PycharmProjects\pythonProject1')  # Добавьте путь к папке с main.py

import main
import definitions as defs

main_var = "Hello from main_window.py!"

if __name__ == "__main__":
    if hasattr(main, "functionTwo"):
        main.functionTwo(main_var)
    else:
        print("Execution module %s" % __file__)
