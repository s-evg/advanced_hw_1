from applications import salary, people
from datetime import datetime

def main():
    p = people.get_employees()
    s = salary.calculate_salary()
    return p, s


if __name__ == '__main__':
    man, money = main()
    print(man, money, sep="\n")
    current_time = datetime.now()
    print(f"Текущая дата и время ===>>> {current_time}")
