import string
import unittest
import requests


class UniTest(unittest.TestCase):
    def test_signals(self):
        URL = "https://hacker-news.firebaseio.com/v0/topstories.json"
        r = requests.get(URL)
        file_json = r.json()
        for j in range(1, 6):
            url = f"https://hacker-news.firebaseio.com/v0/item/{file_json[j]}.json"
            req = requests.get(url)
            f = req.json()
            self.assertEqual(req.status_code, 200)

    def test_name(self):
        URL = "https://hacker-news.firebaseio.com/v0/topstories.json"
        r = requests.get(URL)
        file_json = r.json()
        for j in range(1, 7):
            url = f"https://hacker-news.firebaseio.com/v0/item/{file_json[j]}.json"
            req = requests.get(url)
            f = req.json()
            self.assertEqual(type(f['by']), str)


if __name__ == "__main__":
    UniTest.main()
