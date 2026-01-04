# Custom CSV Class

This project is about working with CSV files using basic Python file handling.
A custom class is created so that all CSV operations are handled in one place.

---

## Reading Data

The first line of the CSV file is treated as the header.
All remaining lines are treated as data rows.
This separation makes it easier to work with CSV content.

---

## Deleting a Row

To delete a row, the file is read completely.
The selected row is removed based on its line number.
After that, the file is saved again with updated content.

---

## Replacing a Row

Replacing a row works by reading all lines from the file.
The selected row is replaced with new data.
The file is then written again so the change is permanent.

---

## Copying the File

A copy of the CSV file can be created by reading the original file
and writing its content into a new file.
The copied file has the same data and structure.

---

## Clearing the File

While clearing the file, all data rows are removed.
The header row is preserved so the CSV structure remains intact.

---

## Sample Usage

```text
csv = CustomCSV("students.csv")

headers = csv.get_headers()
rows = csv.get_rows()

csv.delete_row(2)
csv.replace_row(1, ["2", "Robert", "robert@example.com"])
csv.copy_file("students_backup.csv")
csv.clear_file()
