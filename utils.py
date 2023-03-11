import sqlite3

from constants import fetch_name_of_cities


def get_name_of_cities():
    sql = fetch_name_of_cities()
    conn = sqlite3.connect("cities.db")
    cursor = conn.cursor()
    cursor.execute(sql)
    conn.commit()

    data = cursor.fetchall()
    names = []
    for city in data:
        names.append(city[0])
    return names

if __name__ == '__main__':
    cities = get_name_of_cities()
    print(cities)