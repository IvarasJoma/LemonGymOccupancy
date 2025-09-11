import os
import csv
from datetime import datetime
from zoneinfo import ZoneInfo
from config import DATA_FOLDER, FILENAME_REPLACE_CHAR

def save_club_data(club_data):
    repo_root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    folder_path = os.path.join(repo_root, DATA_FOLDER)
    os.makedirs(folder_path, exist_ok=True)
    timestamp = datetime.now(ZoneInfo("Europe/Vilnius")).strftime("%Y-%m-%d %H:%M:%S")
    for club in club_data:
        safe_name = "".join(c if c.isalnum() else FILENAME_REPLACE_CHAR for c in club["club_name"])
        filepath = os.path.join(folder_path, f"{safe_name}.csv")
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