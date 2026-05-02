from urllib.parse import urlparse

class Canonicalizer:

    @staticmethod
    def get_domain(url, include_scheme=True):
        parsed = urlparse(url)

        scheme = parsed.scheme if parsed.scheme else "http"
        domain = parsed.netloc.lower()

        domain = Canonicalizer.clean_domain(domain, scheme)

        if include_scheme:
            return scheme + "://" + domain
        else:
            return domain

    @staticmethod
    def is_relative_url(url):
        parsed = urlparse(url)
        return parsed.netloc == ""

    @staticmethod
    def canonicalize(url, domain=None):

        if domain is not None:
            url = domain.rstrip("/") + "/" + url.lstrip("/")

        parsed = urlparse(url)

        scheme = parsed.scheme if parsed.scheme else "http"
        domain = Canonicalizer.clean_domain(parsed.netloc.lower(), scheme)

        path = Canonicalizer.clean_path(parsed.path)

        return scheme + "://" + domain + path

    @staticmethod
    def clean_domain(domain, scheme):
        if scheme == "http":
            return domain.replace(":80", "")
        elif scheme == "https":
            return domain.replace(":443", "")
        return domain

    @staticmethod
    def clean_path(path):
        parts = path.split("/")
        cleaned = ""

        for p in parts:
            if p:
                cleaned += "/" + p

        return cleaned


print(Canonicalizer.get_domain("https://www.en.wikipedia.org/wiki/World_War_II"))