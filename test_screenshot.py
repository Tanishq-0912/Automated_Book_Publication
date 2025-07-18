
from scraping.fetch_chapter import fetch_and_screenshot, fetch_chapter_text

# Screenshot
fetch_and_screenshot("https://en.wikipedia.org/wiki/Machine_learning", "ml_chapter")

# Text Extraction
fetch_chapter_text("https://en.wikipedia.org/wiki/Machine_learning", "ml_chapter")
