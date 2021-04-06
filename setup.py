from cx_Freeze import setup, Executable
# package *.py to exe 
setup(
    name="yandere phototaker",
    version="1.1",
    description="Request for the yandere websites photos. Just send tags and crawl all of it",
    author="kidneyweakx",
    executables=[Executable("scraper.py")]
)