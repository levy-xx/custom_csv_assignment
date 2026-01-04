import csv
import shutil
import os

class CustomCSV:
    def __init__(self, file_name):
        self.file_name = file_name
        self.headers = []
        self.rows = []
        self.read_file()

    # --- Read CSV file ---
    def read_file(self):
        # Check if file exists, if not create an empty one
        if not os.path.exists(self.file_name):
            open(self.file_name, "w").close()
            self.headers = []
            self.rows = []
            return

        with open(self.file_name, "r", encoding="utf-8") as file:
            reader = csv.reader(file)
            all_data = list(reader)
            if all_data:
                self.headers = all_data[0]  # first row is headers
                self.rows = all_data[1:]    # rest are rows
            else:
                self.headers = []
                self.rows = []

    # --- Save changes to the file ---
    def save_file(self):
        with open(self.file_name, "w", newline="", encoding="utf-8") as file:
            writer = csv.writer(file)
            if self.headers:
                writer.writerow(self.headers)
            for row in self.rows:
                writer.writerow(row)

    # --- Get headers ---
    def get_headers(self):
        return self.headers

    # --- Get all rows ---
    def get_rows(self):
        return self.rows

    # --- Delete a row by its number (1 = first data row) ---
    def delete_row(self, number):
        if number < 1 or number > len(self.rows):
            print("Row number does not exist!")
            return
        self.rows.pop(number - 1)
        self.save_file()
        print(f"Row {number} deleted!")

    # --- Replace a row by its number ---
    def replace_row(self, number, new_row):
        if number < 1 or number > len(self.rows):
            print("Row number does not exist!")
            return
        self.rows[number - 1] = new_row
        self.save_file()
        print(f"Row {number} replaced!")

    # --- Copy the file ---
    def copy_file(self, new_file_name):
        shutil.copy(self.file_name, new_file_name)
        print(f"File copied to {new_file_name}!")

    # --- Clear all rows (keep headers if keep_headers=True) ---
    def clear_file(self, keep_headers=True):
        if keep_headers:
            self.rows = []
        else:
            self.rows = []
            self.headers = []
        self.save_file()
        print("File cleared!")
