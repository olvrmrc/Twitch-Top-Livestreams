from os import getenv
from typing import Any

from dotenv import load_dotenv
from requests import get

load_dotenv()

URL = 'https://api.twitch.tv/helix/streams'
CLIENT_ID = getenv('CLIENT_ID')
AUTH_TOKEN = getenv('AUTH_TOKEN')
MIN = 0
MAX = 1000000
PAGES = 3
LANGUAGES = ['en']
GAMES = [
    {'ID': 515024, 'Name': 'Diablo IV'},
    {'ID': 509658, 'Name': 'Just Chatting'},
    {'ID': 516575, 'Name': 'VALORANT'},
    {'ID': 55453844, 'Name': 'Street Fighter 6'},
    {'ID': 21779, 'Name': 'League of Legends'},
    {'ID': 29595, 'Name': 'Dota 2'},
    {'ID': 597712627, 'Name': 'Kingdom Hearts Final Mix'},
    {'ID': 32982, 'Name': 'Grand Theft Auto V'},
    {'ID': 513143, 'Name': 'Teamfight Tactics'},
    {'ID': 511224, 'Name': 'Apex Legends'},
    {'ID': 32399, 'Name': 'Counter-Strike: Global Offensive'},
    {'ID': 1767487238, 'Name': 'Casino Slot Machine'},
    {'ID': 33214, 'Name': 'Fortnite'},
    {'ID': 18122, 'Name': 'World of Warcraft'},
    {'ID': 512710, 'Name': 'Call of Duty: Warzone'},
    {'ID': 491487, 'Name': 'Dead by Daylight'},
    {'ID': 26936, 'Name': 'Music'},
    {'ID': 1745202732, 'Name': 'FIFA 23'},
    {'ID': 138585, 'Name': 'Hearthstone'},
    {'ID': 27471, 'Name': 'Minecraft'},
    {'ID': 518144, 'Name': 'The Outlast Trials'},
    {'ID': 509659, 'Name': 'ASMR'},
    {'ID': 515025, 'Name': 'Overwatch 2'},
    {'ID': 512998, 'Name': 'The Legend of Zelda: Tears of the Kingdom'},
    {'ID': 513181, 'Name': 'Genshin Impact'},
    {'ID': 490100, 'Name': 'Lost Ark'},
    {'ID': 263490, 'Name': 'Rust'},
    {'ID': 27546, 'Name': 'World of Tanks'},
    {'ID': 1678052513, 'Name': 'Call of Duty: Modern Warfare II'},
    {'ID': 509660, 'Name': 'Art'},
    {'ID': 491931, 'Name': 'Escape from Tarkov'},
    {'ID': 498566, 'Name': 'Slots'},
    {'ID': 417528, 'Name': 'Albion Online'},
    {'ID': 493597, 'Name': 'New World'},
    {'ID': 29452, 'Name': 'Virtual Casino'},
    {'ID': 518203, 'Name': 'Sports'},
    {'ID': 386821, 'Name': 'Black Desert'},
    {'ID': 19731, 'Name': 'Portal 2'},
    {'ID': 30921, 'Name': 'Rocket League'},
    {'ID': 16582, 'Name': 'Metal Gear Solid 3: Snake Eater'},
    {'ID': 670867987, 'Name': 'Pokémon Scarlet/Violet'},
    {'ID': 509672, 'Name': 'Travel & Outdoors'},
    {'ID': 461067, 'Name': 'Tekken 7'},
    {'ID': 497057, 'Name': 'Destiny 2'},
    {'ID': 27284, 'Name': 'Retro'},
    {'ID': 24241, 'Name': 'FINAL FANTASY XIV ONLINE'},
    {'ID': 19976, 'Name': 'MapleStory'},
    {'ID': 459931, 'Name': 'Old School RuneScape'},
    {'ID': 772421245, 'Name': 'NBA 2K23'},
    {'ID': 493057, 'Name': 'PUBG: BATTLEGROUNDS'},
    {'ID': 32507, 'Name': 'SMITE'},
    {'ID': 65632, 'Name': 'DayZ'},
    {'ID': 499003, 'Name': 'VRChat'},
    {'ID': 213930085, 'Name': 'Honkai: Star Rail'},
    {'ID': 515386, 'Name': 'Skul: The Hero Slayer'},
    {'ID': 743, 'Name': 'Chess'},
    {'ID': 19619, 'Name': 'Tibia'},
    {'ID': 941530474, 'Name': 'Mario Kart 8 Deluxe'},
    {'ID': 272263131, 'Name': 'Animals, Aquariums, and Zoos'},
    {'ID': 1910324696, 'Name': 'High on Life'},
    {'ID': 1047410718, 'Name': 'Football Manager 2023'},
    {'ID': 515214, 'Name': 'Politics'},
    {'ID': 32502, 'Name': 'World of Warships'},
    {'ID': 2146039317, 'Name': 'Farlight 84'},
    {'ID': 2748, 'Name': 'Magic: The Gathering'},
    {'ID': 23857, 'Name': 'Pokémon HeartGold/SoulSilver'},
    {'ID': 1016442748, 'Name': 'MLB The Show 23'},
    {'ID': 499973, 'Name': 'Always On'},
    {'ID': 512980, 'Name': 'Fall Guys'},
    {'ID': 508402, 'Name': 'Live'},
    {'ID': 23020, 'Name': 'ROBLOX'},
    {'ID': 490377, 'Name': 'Sea of Thieves'},
    {'ID': 25367, 'Name': 'Dungeon Fighter Online'},
    {'ID': 512953, 'Name': 'ELDEN RING'},
    {'ID': 488190, 'Name': 'Poker'},
    {'ID': 8105, 'Name': 'South Park'},
    {'ID': 509663, 'Name': 'Special Events'},
    {'ID': 499379, 'Name': 'Stick Fight: The Game'},
    {'ID': 500188, 'Name': 'Hunt: Showdown'},
    {'ID': 499634, 'Name': 'Crypto'},
    {'ID': 498638, 'Name': 'Anno 1800'},
    {'ID': 245018539, 'Name': 'Only Up!'},
    {'ID': 515349, 'Name': 'Lineage II'},
    {'ID': 506416, 'Name': 'Halo Infinite'},
    {'ID': 294724507, 'Name': 'The Last of Us Part I'},
    {'ID': 71375, 'Name': 'Star Citizen'},
    {'ID': 637756067, 'Name': 'ANIME WORLD'},
    {'ID': 116747788, 'Name': 'Pools, Hot Tubs, and Beaches'},
    {'ID': 489635, 'Name': 'ARK: Survival Evolved'},
    {'ID': 515160, 'Name': 'KartRider: Drift'},
    {'ID': 31339, 'Name': 'Project Zomboid'},
    {'ID': 458224, 'Name': 'SOMA'},
    {'ID': 505705, 'Name': 'Noita'},
    {'ID': 514974, 'Name': 'Battlefield 2042'},
    {'ID': 518184, 'Name': 'Phasmophobia'},
    {'ID': 29056, 'Name': 'Knight Online'},
    {'ID': 493959, 'Name': 'Red Dead Redemption 2'}
]


def set_params(cursor: Any = None) -> dict[str, Any]:
    game_ids = []

    for game in GAMES:
        game_ids.append(game['ID'])

    params = {
        'game_id': game_ids,
        'first': 100,
        'language': LANGUAGES
    }

    if cursor:
        params['after'] = cursor

    return params


def fetch_api(params: dict[str, Any]) -> Any:
    headers = {
        'Client-Id': CLIENT_ID,
        'Authorization': f'Bearer {AUTH_TOKEN}'
    }

    data = get(url=URL, headers=headers, params=params).json()

    return data


def save_names(names: list, viewer_counts: list) -> None:
    final_accounts = []

    for i, viewer_count in enumerate(viewer_counts):
        if (viewer_count <= MAX) and (viewer_count >= MIN):
            final_accounts.append(names[i])

    with open('output.txt', 'a') as txt_file:
        for account in final_accounts:
            txt_file.write(str(account) + '\n')


if __name__ == '__main__':
    params = set_params()
    streams = []

    for i in range(PAGES):
        data = fetch_api(params)
        streams.extend(data['data'])

        cursor = data.get('pagination', {}).get('cursor')
        params = set_params(cursor)

    names = []
    viewer_counts = []

    for i, stream in enumerate(streams):
        if not stream['user_login'] in names:
            names.append(stream['user_login'])
            viewer_counts.append(stream['viewer_count'])

    save_names(names, viewer_counts)
