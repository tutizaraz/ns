import csv
from datetime import datetime, timezone

def read_data(csv_file):
    with open(csv_file, mode='r') as file:
        reader = csv.reader(file)
        next(reader) 
        last_smoked_date, days_without_smoking = next(reader)
        return datetime.strptime(last_smoked_date, '%d-%m-%Y').replace(tzinfo=timezone.utc), int(days_without_smoking)

def write_data(csv_file, last_smoked_date, days_without_smoking):
    with open(csv_file, mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(['Last Smoked Date', 'Days Without Smoking'])
        writer.writerow([last_smoked_date.strftime('%d-%m-%Y'), days_without_smoking])

def update_smoking_status(csv_file):
    last_smoked_date, days_without_smoking = read_data(csv_file)
    current_date = datetime.now(timezone.utc)
    updated_days_without_smoking = (current_date - last_smoked_date).days

    if updated_days_without_smoking != days_without_smoking:
        write_data(csv_file, last_smoked_date, updated_days_without_smoking)
        print(f"Updated: {updated_days_without_smoking} days without smoking.")
    else:
        print(f"{days_without_smoking} days without smoking.")

csv_file = 'data.csv'
update_smoking_status(csv_file)
