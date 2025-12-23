from dolshnosti import Dolshnosti
from level import Level
from obrazovanie import Obrazovanie
from professii import Professii
from vakansii import Vakansii
import sqlite3

def load_all():
    conn = sqlite3.connect('kadri.db')
    cursor = conn.cursor()

    dolshnosti, level, obrazovanie, professii, vakansii = [], [], [], [], []

    cursor.execute('select dol_id, dol_code, dol_name from dolshnosti order by dol_id')
    for row in cursor.fetchall():
        dolshnosti.append(Dolshnosti(row[0], row[1], row[2]))

    cursor.execute('select level_id, level_code, level_name from level order by level_id')
    for row in cursor.fetchall():
        level.append(Level(row[0], row[1], row[2]))

    cursor.execute('select obr_id, obr_code, obr_name from obrazovanie order by obr_id')
    for row in cursor.fetchall():
        obrazovanie.append(Obrazovanie(row[0], row[1], row[2]))

    cursor.execute('select prof_id, prof_code, prof_name from professii order by prof_id')
    for row in cursor.fetchall():
        professii.append(Professii(row[0], row[1], row[2]))

    cursor.execute('select vak_id, vak_code, date, vak_name, oklad, aktual, prof_id, obr_id, level_id from vakansii order by vak_id')
    for row in cursor.fetchall():
        vakansii.append(Vakansii(row[0], row[1], row[2], row[3], row[4], row[5], row[6], row[7], row[8]))

    conn.close()

    print(f'загружены {len(dolshnosti)} строк из dolshnosi, загружены {len(level)} строк из level, загружены {len(obrazovanie)} строк из obrazovanie, загружены {len(professii)} строк из professii, загружены {len(vakansii)} строк из vakansii\n')

    return dolshnosti, level, obrazovanie, professii, vakansii

