import sqlite3

def test():
    try:
        conn = sqlite3.connect('kadri.db')
        cursor = conn.cursor()
        print("Коннект есть\n")
    except Exception as e:
        print("Коннекта нет\n")
        return 0
    
    cursor.execute("select name from sqlite_master where type='table'")
    tables = cursor.fetchall()
    table_names = [table[0] for table in tables]
    executed_tables = ['dolshnosti', 'professii', 'obrazovanie', 'level', 'vakansii']

    for table in executed_tables:
        if table in table_names:
            print(f'Таблица {table} есть\n')
        else:
            print(f'Таблицы {table} нет\n')
    conn.close()


def debug():
    conn = sqlite3.connect('kadri.db')
    cursor = conn.cursor()

    print("Первые два значения вакансии и профессии:")

    cursor.execute('''
    select v.vak_name, p.prof_name
    from vakansii v
    join professii p on v.prof_id = p.prof_id
    limit 2''')
    
    for row in cursor.fetchall():
        vak_name, prof_name = row
        print(f'{vak_name}, {prof_name}')
    
    conn.close()
        