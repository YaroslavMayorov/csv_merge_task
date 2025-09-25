## CSV files

**CSV (Comma-Separated Values)** is a very common text format for storing tabular data.  
- Each line in the file represents a row of the table.
- The **first line** usually contains the column headers (names of fields).
- The **following lines** contain values for these fields.
- All columns, including headers and values, are separated by a delimiter (by default – a comma `,`).

Example of a simple CSV file:

```text
key,field1,field2  
1,f11,f12  
2,f21,f22  
3,f31,f32
```

To work with CSV in Python you need the built-in csv module. There are some basic tools with common used arguments:

- `csv.reader(file, delimiter=',')` creates a reader object that reads the file row by row.

```python
import csv

with open("data/file1.csv", newline='') as f:
  reader = csv.reader(f, delimiter=",")
  rows = list(reader)
  ```

- `csv.writer(file, delimiter=',')` creates a writer object that writes rows into a file.
```python
import csv
with open("out.csv", "w", newline='') as f:
    writer = csv.writer(f)
    writer.writerow(["a", "b", "c"])
  ```

- `csv.DictReader(file, delimiter=',')` reads rows into dictionaries; keys for the dictionary are taken from the first row (header) of the file.

```python
import csv

with open("data/file1.csv", newline='') as f:
  reader = csv.DictReader(f, delimiter=";")
  for row in reader:
    print(row["field1"])
```

- `csv.DictWriter(file, fieldnames, delimiter=',')` writes dictionaries into a CSV file, matching keys to column names.
  
  `fieldnames` – a list of column names (must be specified).
  
```python
import csv
with open("out.csv", "w", newline='') as f:
    writer = csv.DictWriter(f, fieldnames=["col1", "col2"], delimiter="\t")
    writer.writeheader()
    writer.writerow({"col1": "x", "col2": "y"})
```

You can read more about working with CSV <a href="https://docs.python.org/3/library/csv.html">here</a>.


### Task

You are given two CSV files, both sharing **only** a column named `key`.

**file1.csv**  
```text
key,field1,field2  
1,f11,f12
3,f31,f32  
2,f21,f22  
4,f41,f42
```

**file2.csv** 
```text
key,field3  
1,f13  
2,f23  
3,f33
5,f53
```

Your goal is to write a function `merge_csv(file1_path, file2_path, result_path, key)` that creates a new CSV file by merging the two tables: the result must contain all columns from both files in the header, and rows must be combined where they share the same `key`.

**result.csv**  
```text
key,field1,field2,field3  
1,f11,f12,f13
3,f31,f32,f33  
2,f21,f22,f23  
```

**Rules:**
- The delimiter is always a comma (`,`).
- The `key` column is first column and used to match rows from both files.
- Each row in both files has a unique, non-empty value in the key column.
- The order of rows in the result must follow the order of `file1.csv`.
- The final header should contain `key`, then all additional columns from `file1.csv`, followed by all additional columns from `file2.csv`.
- Only rows that appear in both files (by `key`) should be written to the result (this is called an *inner join*).

<details><summary> Hint 1</summary> Use <code>csv.DictReader</code> to read rows as dictionaries. </details>
<details><summary> Hint 2</summary> You can store each row in a dictionary using its key to find matching rows. </details>
<details><summary> Hint 3</summary> Use <code>csv.DictWriter</code> to save merged dictionary. </details>



