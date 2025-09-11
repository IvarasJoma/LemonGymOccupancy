import os
import csv
from datetime import datetime
from config import DATA_FOLDER, FILENAME_REPLACE_CHAR

def save_club_data(club_data):
    os.makedirs(DATA_FOLDER, exist_ok=True)
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    for club in club_data:
        safe_name = "".join(c if c.isalnum() else FILENAME_REPLACE_CHAR for c in club["club_name"])
        filepath = os.path.join(DATA_FOLDER, f"{safe_name}.csv")
        file_exists = os.path.isfile(filepath)
        with open(filepath, "a", newline="", encoding="utf-8") as f:
            writer = csv.DictWriter(f, fieldnames=["timestamp", "club", "address", "occupancy"])
            if not file_exists:
                writer.writeheader()
            writer.writerow({
                "timestamp": timestamp,
                "club": club["club_name"],
                "address": club["address"],
                "occupancy": club["occupancy"]
            })
