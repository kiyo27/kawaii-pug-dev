import sqlite3

con = sqlite3.connect("characters.db")
cur = con.cursor()

cur.execute(
    """create table attributes
  (id number, type string, mask string, head string, headband string, neck string, mouth string, eyes string, glasses string, nose string, ears string, skin string)
    """
)

con.close()
