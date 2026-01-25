import requests
import CharacterData as char
import os


class House:
    def __init__(self, name, words, region, coat_of_arms, lord_name):
        self.name = name
        self.words = words
        self.region = region
        self.coat_of_arms = coat_of_arms
        self.lord_name = lord_name


# Then in your loop:
for houseID in range(1, 21):
    url = f"https://www.anapioficeandfire.com/api/houses/{houseID}"
    response = requests.get(url)
    data = response.json()

    HLID = data["currentLord"].split("/")[-1]

    # Create a House object
        #Now corrects for commas in data
    house = House(
        name=(data.get("name") or "No name found").replace(",", ";"),
        words = (data.get("words") or "No words found").replace(",", ";"),
        region = (data.get("region") or "No region found").replace(",", ";"),
        coat_of_arms = (data.get("coatOfArms") or "No coat of arms found").replace(",", ";"),
        lord_name=char.get_char_name(HLID)
    )

    print(f"Processing: {house.name}")

    # Write to CSV
    file_exists = os.path.exists("HouseData.csv")
    with open("HouseData.csv", "a", encoding="utf-8", newline="") as f:
        if not file_exists:
            f.write("House Name,House Words,House Region,House Coat Of Arms,House Lord Name\n")
        f.write(f'{house.name},{house.words},{house.region},{house.coat_of_arms},{house.lord_name}\n')