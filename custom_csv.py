class CustomCSV:
    def __init__(self, file_path):
        self.file_path = file_path

    def get_headers(self):
        with open(self.file_path, "r") as file:
            first_line = file.readline().strip()
            return first_line.split(",")

    def get_rows(self):
        with open(self.file_path, "r") as file:
            lines = file.readlines()[1:]
            rows = []
            for line in lines:
                rows.append(line.strip().split(","))
            return rows

    def delete_row(self, row_number):
        with open(self.file_path, "r") as file:
            lines = file.readlines()

        if row_number < len(lines):
            lines.pop(row_number)

        with open(self.file_path, "w") as file:
            file.writelines(lines)

    def replace_row(self, row_number, new_data):
        with open(self.file_path, "r") as file:
            lines = file.readlines()

        if row_number < len(lines):
            lines[row_number] = ",".join(new_data) + "\n"

        with open(self.file_path, "w") as file:
            file.writelines(lines)

    def copy_file(self, new_file_name):
        with open(self.file_path, "r") as original:
            content = original.read()

        with open(new_file_name, "w") as copy:
            copy.write(content)

    def clear_file(self):
        headers = self.get_headers()
        with open(self.file_path, "w") as file:
            file.write(",".join(headers) + "\n")
