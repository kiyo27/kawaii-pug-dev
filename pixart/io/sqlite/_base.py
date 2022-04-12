import sqlite3
import os


def _extract_filename(path):
    if path is not None:
        return os.path.splitext(os.path.basename(path))[0] 

def write_sqlite(num, character):
    con = sqlite3.connect("characters.db")

    with con:
        l = [
            (
                num,
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
