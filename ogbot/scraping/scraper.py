import util
import logging
import mechanize

class Scraper(object):
    """Base class for scraper classes"""

    def __init__(self, browser, universe):
        self.url_provider = util.UrlProvider(universe)
        self.logger = logging.getLogger('OGBot')
        self.browser = browser

    def open_url(self, url, data = None):
        """Open url, make up to 3 retrys"""
        for attempt in (0, 3):
            try:
                res = self.browser.open(url, data = data)
                return res
            except mechanize.URLError:
                self.logger.warning("URLError opening url, trying again for the %dth time" % (attempt + 1))

    def submit_request(self):
        """Submit browser, make up to 3 retrys"""
        for attempt in (0, 3):
            try:
                res = self.browser.submit()
                return res
            except mechanize.URLError:
                self.logger.warning("URLError submitting form, trying again for the %dth time" % (attempt + 1))

    def sanitize(self, t):
        for i in t:
            try:
                yield int(i)
            except ValueError:
                yield i
