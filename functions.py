import requests
import config

base_url = "https://www.dnd5eapi.co"
headers = {"Accept": "application/json"}


def send_to_coda(url, list_of_payloads):
    for payload in list_of_payloads:
        requests.post(
            url=url,
            headers={
                "Authorization": config.config["CODA_API_TOKEN"],
                "Accept": "application/json",
            },
            json=payload,
        )


def dnd_itereable(list_of_urls):
    payloads = []
    for url in list_of_urls:
        res = requests.get(url=f"{base_url}{url}")
        payloads.append(res.json())
    return payloads


def get_armor():
    res = requests.get(
        url=f"{base_url}/api/equipment-categories/armor", headers=headers
    )
    armor_list = []
    for item in res.json()["equipment"]:
        # Ignore generic armor items and magic items
        if not "Armor" in item["name"].split()[0] and not "magic" in item["url"].strip(
            "/api/"
        ).split("-"):
            armor_list.append(item["url"])
    return armor_list


def get_weapons():
    res = requests.get(
        url=f"{base_url}/api/equipment-categories/weapon", headers=headers
    )
    weapons_list = []
    # Ignore magic items
    for item in res.json()["equipment"]:
        if not "magic" in item["url"].strip("/api/").split("-"):
            weapons_list.append(item["url"])
    return weapons_list


def get_skills():
    res = requests.get(url=f"{base_url}/api/skills", headers=headers)
    skills_list = []
    for item in res.json()["results"]:
        skills_list.append(item["url"])
    return skills_list


def get_monsters():
    res = requests.get(url=f"{base_url}/api/monsters", headers=headers)
    monsters_list = []
    for item in res.json()["results"]:
        monsters_list.append(item["url"])
    return monsters_list


def get_classes():
    res = requests.get(url=f"{base_url}/api/classes", headers=headers)
    classes_list = []
    for item in res.json()["results"]:
        classes_list.append(item["url"])
    return classes_list


def get_races():
    res = requests.get(url=f"{base_url}/api/races", headers=headers)
    races_list = []
    for item in res.json()["results"]:
        races_list.append(item["url"])
    return races_list


def get_traits():
    res = requests.get(url=f"{base_url}/api/traits", headers=headers)
    traits_list = []
    for item in res.json()["results"]:
        traits_list.append(item["url"])
    return traits_list
