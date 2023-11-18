import categories
import requests
from bs4 import BeautifulSoup


def faceit_csgo(nickname):
    URL = "https://faceitstats.com/player/" + nickname
    HEADERS = {
        "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.116 Safari/537.36",
        "accept": "*/*"
    }
    html = requests.get(URL, headers=HEADERS, params=None)

    if html.status_code == 200:
        soup = BeautifulSoup(html.text, "html.parser")
        soup_stats = soup.find_all("h5")
        soup_img = soup.find("img", class_="rounded")
        stats = []

        for i in soup_stats:
            stats.append(i.text)
        stats.append(soup_img["src"])
        print(stats)
        return stats

    else:
        return False


def osu(nickname):
    URL = "https://osu.ppy.sh/u/" + nickname
    HEADERS = {
        "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.116 Safari/537.36",
        "accept": "*/*"
    }
    html = requests.get(URL, headers=HEADERS, params=None)

    if html.status_code == 200:
        soup = BeautifulSoup(html.text, "html.parser")
        soup_stats = soup.find(
            "div", class_="js-react--profile-page osu-layout osu-layout--full"
        )
        osu_data = str(soup_stats).split(";")
        stats = []

        for i in range(15):
            try:
                stats.append(
                    osu_data[osu_data.index(categories.osu_stats_category[i]) + 1]
                    .replace(",&quot", "")
                    .replace(":", "")
                    .replace("}", "")
                )
            except:
                stats.append('——')
        return stats
    else:
        return False


def fort(nickname):
    URL = "https://fortnite.gg/stats?player=" + nickname
    HEADERS = {
        "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.116 Safari/537.36",
        "accept": "*/*"
    }
    html = requests.get(URL, headers=HEADERS, params=None)

    if html.status_code == 200:
        soup = BeautifulSoup(html.text, "html.parser")
        soup_stats = soup.find_all("script")
        all_stats = soup_stats[7].text.split(",")
        fort_stats = []
        stats = []

        for i in range(1, 6):
            fort_stats.append(int(all_stats[i].replace(categories.fort_stats_category[i - 1], '').replace('"', '')))

        fort_stats.append(fort_stats[1] * 100 / fort_stats[2])
        fort_stats.append(fort_stats[3] / fort_stats[4])
        fort_stats.append(fort_stats[3] / fort_stats[2])
        fort_stats.pop(4)

        return fort_stats
