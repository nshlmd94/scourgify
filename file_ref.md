# 📂 CSV & File Handling – Quick Reference Table

| 🧠 Concept                            | 💻 Command / Code                                                                 | 📘 Explanation                                                                 |
|--------------------------------------|----------------------------------------------------------------------------------|--------------------------------------------------------------------------------|
| Open file for reading                | `with open("file.csv", "r") as file:`                                            | Opens a file safely for reading                                               |
| Open file for writing                | `with open("file.csv", "w") as file:`                                            | Opens file for writing (overwrites if exists)                                |
| Check if file exists                 | `os.path.isfile("file.csv")`                                                     | Checks if the file exists                                                     |
| Check if file is readable            | `os.access("file.csv", os.R_OK)`                                                 | Checks if file has read permissions                                           |
| Check if file is writable            | `os.access("file.csv", os.W_OK)`                                                 | Checks if file has write permissions                                          |
| Exit if file can't be read           | `if not os.access(file, os.R_OK): sys.exit("Cannot read file")`                 | Exits the program with an error                                               |
| Read CSV with headers                | `reader = csv.DictReader(file)`                                                  | Returns each row as a dict (header as keys)                                  |
| Read CSV without headers             | `reader = csv.reader(file)`                                                      | Returns each row as a list                                                    |
| Write CSV with headers               | `writer = csv.DictWriter(file, fieldnames=[...])`                                | Prepares to write dict rows to file                                           |
| Write header row                     | `writer.writeheader()`                                                           | Writes the fieldnames to the first row                                        |
| Write one row                        | `writer.writerow({...})`                                                         | Writes one row of data as a dict                                              |
| Access values from DictReader row    | `row["name"]`, `row["house"]`                                                    | Access individual values by column name                                       |
| Split a string by comma              | `"Potter, Harry".split(",")`                                                     | Useful to separate last and first names                                       |
| Clean up whitespace                  | `"  Harry  ".strip()`                                                            | Removes leading/trailing spaces                                               |
| Remove double quotes                 | `string.replace('"', "")`                                                        | Removes unwanted quotes from CSV fields                                       |
| Exit on wrong command-line args      | `if len(sys.argv) != 3: sys.exit("Too few or too many args")`                   | Checks correct number of arguments                                            |
| Get file names from command-line     | `file_before = sys.argv[1]; file_after = sys.argv[2]`                            | Gets input/output filenames from terminal                                     |
| Check file extension                 | `filename.endswith(".csv")`                                                      | Ensures only `.csv` files are processed                                       |
| Handle file-not-found errors         | `except FileNotFoundError:`                                                      | Catches errors if the file is missing                                         |
| Write to file using DictWriter       | `writer.writerow({"first name": ..., "last name": ..., "house": ...})`          | Rewrites CSV row with cleaned and split data                                  |