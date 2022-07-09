
prerequisits

```
python -m venv .venv
. .venv/bin/activate
```

Install the kawaii-pugs in editable mode.

```
pip install -e .
```

Show useage

```
$ kawaii-pugs create --help
Usage: kawaii-pugs create [OPTIONS]

Options:
  --multiple INTEGER
  --no-preview
  --from-db
  --help              Show this message and exit.
```

---

ドット絵メーカーからcsvに変換
convert dotmaker format into csv.

```
./convert.py bandana.dt3 -d attributes/head
```
