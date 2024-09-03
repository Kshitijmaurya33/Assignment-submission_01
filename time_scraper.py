import requests
from html.parser import HTMLParser

class TimeParser(HTMLParser):
    def __init__(self):
        super().__init__()
        self.stories = []

    def handle_starttag(self, tag, attrs):
        if tag == "h3":
            for name, value in attrs:
                if name == "class" and value == "headline":
                    self.stories.append({"title": "", "link": ""})

    def handle_data(self, data):
        if self.stories and self.stories[-1]["title"] == "":
            self.stories[-1]["title"] = data.strip()

    def handle_endtag(self, tag):
        if tag == "a":
            if self.stories and self.stories[-1]["link"] == "":
                self.stories[-1]["link"] = self.get_attribute("href")

    def get_attribute(self, attr):
        for name, value in self.lasttag.find("a").attrs:
            if name == attr:
                return value

def get_latest_stories(stories, num_stories):
    return stories[:num_stories]

def main():
    url = "https://time.com"
    response = requests.get(url)
    html = response.text
    parser = TimeParser()
    parser.feed(html)
    latest_stories = get_latest_stories(parser.stories, 6)
    return latest_stories

if __name__ == "__main__":
    latest_stories = main()
    print(latest_stories)