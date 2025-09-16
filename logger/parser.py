from bs4 import BeautifulSoup

def parse_clubs(html_content):
    soup = BeautifulSoup(html_content, "lxml")
    clubs = []
    for block in soup.select(".clubs-occupancy"):
        club_name = block.select_one("h6").get_text(strip=True)
        address = block.select_one("p").get_text(strip=True)
        occupancy = block.select_one(".clubs-occupancy__percentage").get_text(strip=True)
        clubs.append({
            "club_name": club_name,
            "address": address,
            "occupancy": occupancy
        })
    return clubs