import sqlite3
from create import create
from data import load_all
from test_debug import test, debug
from reports import report1, report2

def show_menu():
    print('1. Загрузка данных')
    print('2. Создать бд')
    print('3. Сделать тест')
    print('4. Показать отладку')
    print('5. Создать первый отчёт')
    print('6. Создать второй отчёт')
    print('7. Показать сложность')
    print('8. Выйти')

def big_o():
    print("Анализ временной сложности:")
    print("1. Подключение к БД — O(1), константное время.")
    print("2. Выполнение 5 SQL-запросов — каждый запрос SELECT * FROM ... имеет сложность:")
    print("- В худшем случае O(N), где N — количество записей в таблице.")
    print("- Но если таблицы проиндексированы (по dol_id, level_id и т.д.), то выборка с сортировкой - O(N log N).")
    print("3. Итерация по результатам запросов — для каждой таблицы проходим по всем строкам:")
    print("- O(N_d) + O(N_l) + O(N_o) + O(N_p) + O(N_v), где N_* — количество записей в соответствующей таблице.")
    print("- В сумме это O(N_total), где N_total — общее количество записей во всех таблицах.")
    print("4. Создание объектов — для каждой строки создается объект класса, что также O(1) на запись.")
    print("5. Закрытие соединения — O(1)\n")
    print("Итоговая сложность (индексы присутствуют, сортировка быстрая): O(N_total), где N_total — общее число записей.")

def main():
    dolshnosti, level, obrazovanie, professii, vakansii = [], [], [], [], []

    while True:
        show_menu()
        choice = input("Выберите: \n")
        if choice == '1':
            dolshnosti, level, obrazovanie, professii, vakansii = load_all()
        elif choice == '2':
            create()
        elif choice == '3':
            test()
        elif choice == '4':
            debug()
        elif choice == '5':
            report1(vakansii)
        elif choice == '6':
            report2(vakansii, level)
        elif choice == '7':
            big_o()
        elif choice == '8':
            break
        else:
            print('выберите другое число\n')
