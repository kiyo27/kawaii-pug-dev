import sqlite3
import csv
import os


def _extract_filename(path):
    if path is not None:
        return os.path.splitext(os.path.basename(path))[0]


def write_sqlite(character):
    con = sqlite3.connect("characters.db")

    with con:
        l = [
            (
                character.num,
                character.ctype,
                character.attributes.mask["name"],
                character.attributes.head["name"],
                character.attributes.headband["name"],
                character.attributes.neck["name"],
                character.attributes.mouth["name"],
                character.attributes.eyes["name"],
                character.attributes.glasses["name"],
                character.attributes.nose["name"],
                character.attributes.ears["name"],
                _extract_filename(character.color.skin)
            )
        ]
        con.executemany("insert into attributes values (?,?,?,?,?,?,?,?,?,?,?,?)", l)


def export_csv():
    con = sqlite3.connect("characters.db")
    cur = con.cursor()
    cur.execute("SELECT * FROM attributes")
    with open('result.csv', 'w') as f:
        writer = csv.writer(f)
        h = [t[0] for t in cur.description] 
        writer.writerow(h)
        for row in cur.fetchall():
            writer.writerow(row)

    con.close()

def select():
    con = sqlite3.connect("characters.db")
    con.row_factory = sqlite3.Row
    with con:
        cur = con.cursor()
        cur.execute("SELECT * FROM attributes")
        l = list()
        for row in cur.fetchall():
            l.append(_format(row))
        
    con.close()  
    return l

def delete_table():
    con = sqlite3.connect("characters.db")
    with con:
        con.execute("delete from attributes")

def _format(row):
    data = {
        'id': row['id'],
        'type': row['type'],
        'skin': _convert_none_to_false(row['skin']),
        'attributes': {
            'mask': _convert_none_to_false(row['mask']),
            'head': _convert_none_to_false(row['head']),
            'headband': _convert_none_to_false(row['headband']),
            'neck': _convert_none_to_false(row['neck']),
            'mouth': _convert_none_to_false(row['mouth']),
            'eyes': _convert_none_to_false(row['eyes']),
            'glasses': _convert_none_to_false(row['glasses']),
            'nose': _convert_none_to_false(row['nose']),
            'ears': _convert_none_to_false(row['ears']),
        }
    }

    return data

def _convert_none_to_false(value):
    if value is None:
        return False
    return value
