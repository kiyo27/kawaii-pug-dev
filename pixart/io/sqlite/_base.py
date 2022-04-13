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
                _extract_filename(character.ctype),
                _extract_filename(character.attributes.head),
                _extract_filename(character.attributes.neck),
                _extract_filename(character.attributes.mouth),
                _extract_filename(character.attributes.eyes),
                _extract_filename(character.attributes.glasses),
                _extract_filename(character.attributes.nose),
                _extract_filename(character.attributes.ears),
                _extract_filename(character.attributes.skin),
            )
        ]
        con.executemany("insert into attributes values (?,?,?,?,?,?,?,?,?,?)", l)


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
