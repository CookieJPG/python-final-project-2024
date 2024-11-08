from gui import cre_main_window
from  database import init_excel_db

def main():
    init_excel_db()
    cre_main_window()

if __name__ == "__main__":
    main()