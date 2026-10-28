"""Check built navigation, assets, local links, and executable Python examples."""

from contextlib import redirect_stdout
from html.parser import HTMLParser
from io import StringIO
from pathlib import Path
import re
import sys
from urllib.parse import unquote, urlsplit


ROOT = Path(__file__).resolve().parents[1]
SITE = ROOT / "site"
sys.path.insert(0, str(ROOT))


class PageParser(HTMLParser):
    def __init__(self):
        super().__init__()
        self.links = []
        self.ids = set()
        self.images = []
        self.hero_count = 0
        self.pagination_count = 0
        self.directions = set()
        self.theme_switches = 0
        self.search_label = None

    def handle_starttag(self, tag, attrs):
        attrs = dict(attrs)
        if "id" in attrs:
            self.ids.add(attrs["id"])
        if tag == "a" and "href" in attrs:
            self.links.append(attrs["href"])
            if attrs.get("rel") in ("prev", "next"):
                self.directions.add(attrs["rel"])
        if tag == "img":
            self.images.append(attrs)
        if tag == "figure" and attrs.get("class") == "workshop-hero":
            self.hero_count += 1
        if tag == "nav" and attrs.get("aria-label") == "Workshop page navigation":
            self.pagination_count += 1
        if tag == "input" and attrs.get("data-md-color-scheme"):
            self.theme_switches += 1
        if attrs.get("data-md-component") == "search":
            self.search_label = attrs.get("aria-label")


def check() -> None:
    pages = {}
    for path in SITE.rglob("*.html"):
        parser = PageParser()
        parser.feed(path.read_text(encoding="utf-8"))
        pages[path.resolve()] = parser

    assert len(pages) >= 13, "Expected twelve workshop pages and a 404 page"
    for path, page in pages.items():
        if path.name == "404.html":
            continue
        assert page.hero_count == 1, f"Missing hero: {path}"
        assert page.pagination_count == 1, f"Missing page controls: {path}"
        assert page.directions == {"prev", "next"}, f"Missing direction: {path}"
        assert page.theme_switches == 2, f"Missing theme controls: {path}"
        assert page.search_label, f"Search dialog lacks a name: {path}"
        for image in page.images:
            assert "alt" in image, f"Image lacks alt attribute: {path}"
            target = (path.parent / unquote(urlsplit(image["src"]).path)).resolve()
            assert target.is_file(), f"Missing image: {target}"
        for link in page.links:
            parsed = urlsplit(link)
            if parsed.scheme or parsed.netloc:
                continue
            # Material uses a root-relative skip link only on its 404 page.
            target = (path.parent / unquote(parsed.path)).resolve() if parsed.path else path
            if target.is_dir():
                target /= "index.html"
            assert target.is_file(), f"Broken local link in {path}: {link}"
            if parsed.fragment and target in pages:
                assert unquote(parsed.fragment) in pages[target].ids, (
                    f"Missing anchor in {path}: {link}"
                )

    home = pages[(SITE / "index.html").resolve()]
    thumbnails = {image["src"] for image in home.images if image.get("loading") == "lazy"}
    assert len(thumbnails) == 11, "Home must show every original hero as a thumbnail"

    snippets = 0
    for path in (ROOT / "docs").glob("*.md"):
        source = path.read_text(encoding="utf-8")
        for snippet in re.findall(r"```python\n(.*?)```", source, re.DOTALL):
            with redirect_stdout(StringIO()):
                exec(compile(snippet, str(path), "exec"), {"__name__": "__workshop__"})
            snippets += 1
    assert snippets == 10, "Expected one executable Python example per chapter"
    print(f"Checked {len(pages)} HTML pages, 11 thumbnails, and {snippets} Python examples.")


if __name__ == "__main__":
    check()
