import requests
import sys
import traceback
import urllib


class UrlShortenTinyurl:
    URL = "http://tinyurl.com/api-create.php"

    def shorten(self, url_long):
        try:
            url = self.URL + "?" \
                + urllib.parse.urlencode({"url": url_long})
            res = requests.get(url)
            print("  SHORT URL:", res.text)
        except Exception as e:
            raise


if __name__ == '__main__':
    url_long = input("	Enter long URL: ")
    try:
        obj = UrlShortenTinyurl()
        obj.shorten(url_long)
    except Exception as e:
        traceback.print_exc()
