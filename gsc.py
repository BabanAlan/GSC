import requests
from bs4 import BeautifulSoup


def stats_collector(message, url):
    message_info = message.split()

    return parser(message_info[0], message_info[1], url)


def parser(game, nickname, url):
    URL = url + nickname
    HEADERS = {
        "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.116 Safari/537.36",
        "accept": "*/*"
    }
    html = requests.get(URL, headers=HEADERS, params=None)

    if html.status_code == 200:
        if game == "/fcsgo":
            return faceit_csgo(html)
        elif game == "/osu":
            return osu(html)
        else:
            return False


def faceit_csgo(html):
    soup = BeautifulSoup(html.text, "html.parser")
    soup_stats = soup.find_all("h5")
    stats = []

    for i in soup_stats:
        stats.append(i.text)

    return stats


def osu(html):
    soup = BeautifulSoup(html.text, "html.parser")
    soup_stats = soup.find(
        "div", class_="js-react--profile-page osu-layout osu-layout--full"
    )
    osu_data = str(soup_stats).split(";")
    stats = []

    categories = [
        "pp&quot",
        "hit_accuracy&quot",
        "maximum_combo&quot",
        "global_rank&quot",
        "country_rank&quot",
        "ss&quot",
        "ssh&quot",
        "s&quot",
        "sh&quot",
        "a&quot",
        "ranked_score&quot",
        "play_count&quot",
        "total_score&quot",
        "total_hits&quot",
        "current&quot",
    ]  # из-за конченной системы нахождения отличается по смыслу. лучше бы переписать то как работает "categories"

    for i in range(15):
        try:
            stats.append(
                osu_data[osu_data.index(categories[i]) + 1]
                .replace(",&quot", "")
                .replace(":", "")
                .replace("}", "")
            )
        except:
            stats.append('——')

    return stats