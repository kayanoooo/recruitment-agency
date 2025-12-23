import sqlite3

def report1(vakansii):
    conn = sqlite3.connect('kadri.db')
    cursor = conn.cursor()

    with open('report1.txt', 'w', encoding='utf-8') as f:
        f.write('Список актуальных вакансий:\n')
        f.write('Название вакансии, актуальность\n')

        cursor.execute('''            
        select vak_name, aktual
        from vakansii
        where aktual = 'актуально'
        ''')
        
        for row in cursor.fetchall():
            vak_name, aktual = row
            f.write(f'{vak_name}, {aktual}\n')

        print("Первый отчёт создался\n")

    conn.close()

def report2(vakansii, level):
    conn = sqlite3.connect('kadri.db')
    cursor = conn.cursor()

    with open('report2.txt', 'w', encoding='utf-8') as f:
        f.write('Сравнительная таблица окладов по уровням:\n')
        f.write('Уровень, Количество вакансий, Средний оклад, Минимальный оклад, Максимальный оклад\n')

        cursor.execute('''            
        select 
            l.level_name AS 'Уровень',
            count(v.vak_id) AS 'Количество вакансий',
            round(avg(v.oklad), 2) AS 'Средний оклад',
            min(v.oklad) AS 'Минимальный оклад',
            max(v.oklad) AS 'Максимальный оклад'
        from vakansii v
        join level l ON v.level_id = l.level_id
        group by l.level_id, l.level_name
        order by l.level_id;
        ''')

        for row in cursor.fetchall():
            level_name, count, avg_oklad, min_oklad, max_oklad = row
            f.write(f"{level_name}, {count}, {avg_oklad}, {min_oklad}, {max_oklad}\n")

        print("Второй отчёт создался\n")

    conn.close()
    
