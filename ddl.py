import sqlite3

con = sqlite3.connect("characters.db")
cur = con.cursor()

cur.execute(
    """create table characters
  (id number, types string, head string, neck string, mouth string, eyes string, goggle string, nose string, ears string)
  """
)

con.close()
