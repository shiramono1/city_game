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

class MenuStack:

    def __init__(self, default_menu):
        self.elements = list()
        self.default_menu = default_menu

    def push(self, element):
        self.elements.append(element)

    def pop(self):
        if len(self.elements) == 0:
            return self.default_menu

        popped_element = self.elements[-1]
        del self.elements[-1]
        return popped_element

    def top(self):
        if len(self.elements) == 0:
            return self.default_menu
        return self.elements[-1]

    def __str__(self):
        return str(self.elements)


