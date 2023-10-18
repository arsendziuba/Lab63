import sys
sys.path.append('C:/Users/user/PycharmProjects/pythonProject1/Defs')  # Добавьте путь к папке с модулем definitions.py

import definitions as defs

main_var = "Some data"
if hasattr(defs, "functionTwo"):
    defs.functionTwo(main_var)
else:
    print(f"Execution module {__file__}")
