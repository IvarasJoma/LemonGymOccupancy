from fetcher import fetch_html
from parser import parse_clubs
from saver import save_club_data
from concurrent.futures import ThreadPoolExecutor, TimeoutError

def run_logger():
    html_content = fetch_html()
    clubs = parse_clubs(html_content)
    save_club_data(clubs)
    print("✅ Data saved successfully")

def main():
    TIMEOUT_SECONDS = 30
    with ThreadPoolExecutor(max_workers=1) as executor:
        future = executor.submit(run_logger)
        try:
            future.result(timeout=TIMEOUT_SECONDS)
        except TimeoutError:
            print(f"❌ Script aborted: exceeded {TIMEOUT_SECONDS} seconds")

if __name__ == "__main__":
    main()