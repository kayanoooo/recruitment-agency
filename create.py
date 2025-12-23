import sqlite3

def create():
    #подключение к базе данных
    conn = sqlite3.connect('kadri.db')
    cursor = conn.cursor()

    #запрос в бд: создание таблицы
    cursor.execute('''
    create table dolshnosti(
        dol_id integer primary key,
        dol_code text,
        dol_name text               
    )''')

    cursor.execute('''
    create table professii(
        prof_id integer primary key,
        prof_code text,
        prof_name text               
    )''')

    cursor.execute('''
    create table obrazovanie(
        obr_id integer primary key,
        obr_code text,
        obr_name text               
    )''')

    cursor.execute('''
    create table level(
        level_id integer primary key,
        level_code text,
        level_name text               
    )''')

    cursor.execute('''
    create table vakansii(
        vak_id integer primary key,
        vak_code text,
        date text,
        vak_name text,
        oklad integer,
        aktual text,
        prof_id integer,
        obr_id integer,
        level_id integer,                      
        foreign key (prof_id) references professii(prof_id),
        foreign key (obr_id) references obrazovanie(obr_id),
        foreign key (level_id) references level(level_id)
    )''')

    #создание массива с данными
    dolshnosti = [
        (1, '01.01', 'чёрный хлеб'),
        (2, '01.02', 'белый хлеб'),
        (3, '01.03', 'серый хлеб')
    ]

    professii = [
        (1, '02.01', 'программист'),
        (2, '02.02', 'веб-программист'),
        (3, '02.03', 'сис админ')
    ]

    obrazovanie = [
        (1, '03.01', 'ранхигс'),
        (2, '03.02', 'мфюа'),
        (3, '03.03', 'плеханова')
    ]

    level = [
        (1, '04.01', 'низкий'),
        (2, '04.02', 'средний'),
        (3, '04.03', 'высокий')
    ]

    vakansii = [
        (1, '05.01', '2024-01-01', 'back-end нужен', '40000', 'актуально', '1', '1', '1'),
        (2, '05.02', '2025-01-01', 'front-end нужен', '70000', 'актуально', '2', '2', '2'),
        (3, '05.03', '2024-08-01', 'сис админ нужен', '50000', 'неактуально', '3', '3', '3'),
        (4, '05.04', '2023-08-01', 'сис админ нужен', '30000', 'неактуально', '3', '3', '2')
    ]

    #добавление данных в таблицы из массивов
    cursor.executemany('insert into dolshnosti (dol_id, dol_code, dol_name) values (?, ?, ?)', dolshnosti)
    cursor.executemany('insert into professii (prof_id, prof_code, prof_name) values (?, ?, ?)', professii)
    cursor.executemany('insert into obrazovanie (obr_id, obr_code, obr_name) values (?, ?, ?)', obrazovanie)
    cursor.executemany('insert into level (level_id, level_code, level_name) values (?, ?, ?)', level)
    cursor.executemany('insert into vakansii (vak_id, vak_code, date, vak_name, oklad, aktual, prof_id, obr_id, level_id) values (?, ?, ?, ?, ?, ?, ?, ?, ?)', vakansii)

    #сохранение базы данных и её закрытие
    conn.commit()
    conn.close()

    print('БД создана')




