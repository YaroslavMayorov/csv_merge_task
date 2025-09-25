# CSV Merge Assignment

This repository contains all the necessary files for the **CSV Merge** programming assignment.  
The goal of the assignment is to teach learners how to merge two CSV files by a common key column.

---

## Repository structure

```text 
.
├── src/                               # Source files for the assignment
│   ├── assignment.md                  # Assignment description and hints for learners
│   ├── solution.py                    # Reference correct solution
│   ├── wrong_solution.py              # Intentionally incorrect solution
│   ├── data/                          # Example input data
│   │   ├── file1.csv                  # Example input file 1
│   │   ├── file2.csv                  # Example input file 2
|
├── tests/                             # Unit tests for validating solutions
│   ├── test.py                        # Unittest test suite
│
├── README.md                          # Instructions for instructors and learners
```
---

## Running the tests

1. **Clone the repository**
   ```bash
   git clone https://github.com/YaroslavMayorov/csv_merge_task.git
   cd csv_merge_task
   ```
   
2. **Run tests against the reference solution**

    ```bash
   python tests/test.py src/solution.py -v
   ```

3. **Run tests against the wrong solution**

    ```bash
    python tests/test.py src/wrong_solution.py -v
    ```

---

## FAQ

### How does the reference solution work?
The reference solution reads both CSV files using `csv.DictReader` and builds a dictionary from the second file where  
the **key column** is used as an index.  
Then it iterates over the rows of the first file in order, finds the matching row from the second file (by the same key),  
and combines their fields into a new row.  
This guarantees:
- all headers from both files are present in the result,
- rows are merged only if they share the same key,
- the original order of rows from the first file is preserved.

### Why does the wrong solution fail?
The wrong solution demonstrates common mistakes that learners may encounter:
- It uses a `set` of keys instead of iterating over `file1` rows, which **loses the original row order**.
- It performs a union of keys (`|`) instead of an inner join (`&`), which may **include keys that don’t exist in both files**.
- As a result, the merged CSV may contain rows that should not exist or appear in the wrong order.