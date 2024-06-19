import csv

# Membaca file CSV
def read_csv(file_path):
    with open(file_path, mode='r', newline='') as file:
        csv_reader = csv.reader(file)
        header = next(csv_reader)  # Membaca header
        print(f"Header: {header}")
        
        for row in csv_reader:
            print(row)

# Contoh penggunaan
read_csv('Python/Semester2/Percobaan/Data.csv')
