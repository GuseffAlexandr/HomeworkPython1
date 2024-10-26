from datetime import datetime
from application.salary import calculate_salary
from application.db.people import get_employees

if __name__ == '__main__':
    print("Текущая дата:", datetime.now().date())
    calculate_salary()
    get_employees()