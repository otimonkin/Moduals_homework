from datetime import datetime

from application.salary import calculate_salary
from db.people import get_employees
from datetime import datetime, date, time


print(datetime.now())

if __name__ == '__main__':
    calculate_salary()

if __name__ == '__main__':
    get_employees()