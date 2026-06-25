import requests
from bs4 import BeautifulSoup
import pandas as pd
import time


def scrape_all_squads(nation_map):
    url = "https://en.wikipedia.org/wiki/2026_FIFA_World_Cup_squads"
    http_headers = {
        "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
    }
    response = requests.get(url, headers=http_headers)
    print(f"Status: {response.status_code}")
    soup = BeautifulSoup(response.text, "html.parser")

    all_players = []
    current_nation = None
    current_nation_id = None

    for tag in soup.find_all(["h3", "table"]):
        if tag.name == "h3":
            heading = tag.get_text(strip=True).replace("[edit]", "").strip()
            if heading in nation_map:
                current_nation = heading
                current_nation_id = nation_map[heading]
                print(f"Found: {current_nation}")
            else:
                current_nation = None
                current_nation_id = None

        elif tag.name == "table" and current_nation:
            headers = [th.get_text(strip=True) for th in tag.find_all("th")]
            if "Pos." not in headers and "Player" not in headers:
                continue

            rows = tag.find_all("tr")[1:]
            for row in rows:
                cols = row.find_all(["td", "th"])
                if len(cols) < 4:
                    continue

                kit_number = cols[0].get_text(strip=True)

                # Strip leading number from position e.g. "1GK" -> "GK"
                position_raw = cols[1].get_text(strip=True)
                position = ''.join([c for c in position_raw if not c.isdigit()])

                full_name = cols[2].get_text(strip=True).replace("(captain)", "").strip()

                # Date is inside first set of brackets e.g. "(1992-10-02)October 2, 1992"
                dob_raw = cols[3].get_text(strip=True)
                dob = dob_raw.split(")")[0].replace("(", "").strip()

                # Split name
                name_parts = full_name.split(" ", 1)
                first_name = name_parts[0]
                last_name = name_parts[1] if len(name_parts) > 1 else ""

                all_players.append({
                    "nation_id": current_nation_id,
                    "first_name": first_name,
                    "last_name": last_name,
                    "position": position,
                    "kit_number": kit_number,
                    "date_of_birth": dob
                })

            current_nation = None

    return all_players


# Map Wikipedia nation names to your nation_id values
nation_map = {
    "Mexico": 1,
    "South Korea": 2,
    "Czech Republic": 3,
    "South Africa": 4,
    "Canada": 5,
    "Switzerland": 6,
    "Bosnia and Herzegovina": 7,
    "Qatar": 8,
    "Brazil": 9,
    "Morocco": 10,
    "Scotland": 11,
    "Haiti": 12,
    "United States": 13,
    "Australia": 14,
    "Paraguay": 15,
    "Turkey": 16,
    "Germany": 17,
    "Ivory Coast": 18,
    "Ecuador": 19,
    "Curaçao": 20,
    "Netherlands": 21,
    "Sweden": 22,
    "Japan": 23,
    "Tunisia": 24,
    "New Zealand": 25,
    "Iran": 26,
    "Belgium": 27,
    "Egypt": 28,
    "Uruguay": 29,
    "Saudi Arabia": 30,
    "Spain": 31,
    "Cape Verde": 32,
    "Norway": 33,
    "France": 34,
    "Senegal": 35,
    "Iraq": 36,
    "Argentina": 37,
    "Austria": 38,
    "Jordan": 39,
    "Algeria": 40,
    "Colombia": 41,
    "DR Congo": 42,
    "Portugal": 43,
    "Uzbekistan": 44,
    "England": 45,
    "Ghana": 46,
    "Panama": 47,
    "Croatia": 48,
}

all_players = scrape_all_squads(nation_map)

df = pd.DataFrame(all_players)
print(df.head(10))
print(f"\nTotal players: {len(all_players)}")

df.to_csv("data/cleaned/players.csv", index=False)
print("Saved to data/cleaned/players.csv")