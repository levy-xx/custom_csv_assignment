import csv
import os

class CustomCSV:
    def __init__(self, file_name):
        self.file_name = file_name
        self.headers = []
        self.rows = []
        print(f"Opening file: {self.file_name}...")
        self.read_file()

    # Read CSV file
    def read_file(self):
        if not os.path.exists(self.file_name):
            print("File not found, creating new one...")
            open(self.file_name, "w").close()
            self.headers = []
            self.rows = []
            return

        with open(self.file_name, "r", encoding="utf-8") as f:
            reader = csv.reader(f)
            data = list(reader)
            if len(data) > 0:
                self.headers = data[0]
                self.rows = data[1:]
                print("File loaded successfully!")
            else:
                self.headers = []
                self.rows = []
                print("File is empty!")

    # Save changes
    def save_file(self):
        with open(self.file_name, "w", newline="", encoding="utf-8") as f:
            writer = csv.writer(f)
            if self.headers != []:
                writer.writerow(self.headers)
            for r in self.rows:
                writer.writerow(r)
        print("File saved!")

    # Get headers
    def get_headers(self):
        return self.headers

    # Get all rows
    def get_rows(self):
        return self.rows

    # Delete a row
    def delete_row(self, num):
        if num < 1 or num > len(self.rows):
            print("Oops! Row number is wrong.")
            return
        self.rows.pop(num - 1)
        self.save_file()
        print(f"Row {num} deleted!")

    # Replace a row
    def replace_row(self, num, new_row):
        if num < 1 or num > len(self.rows):
            print("Oops! Row number is wrong.")
            return
        self.rows[num - 1] = new_row
        self.save_file()
        print(f"Row {num} replaced!")

    # Copy file without shutil
    def copy_file(self, new_file_name):
        try:
            with open(self.file_name, "r", encoding="utf-8") as f1:
                content = f1.read()
            with open(new_file_name, "w", encoding="utf-8") as f2:
                f2.write(content)
            print(f"File copied to {new_file_name}!")
        except:
            print("Error copying file!")

    # Clear file
    def clear_file(self, keep_headers=True):
        if keep_headers:
            self.rows = []
        else:
            self.rows = []
            self.headers = []
        self.save_file()
        print("File cleared!")

# Example usage
if __name__ == "__main__":
    mycsv = CustomCSV("test.csv")
    print("Headers:", mycsv.get_headers())
    print("Rows:", mycsv.get_rows())
