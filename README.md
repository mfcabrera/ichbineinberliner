# Ichbineinberliner

This is a small scrappy project that I wrote for two purposes:

1. Learn Scrapy
2. Help my GF to find a place to live.

## Idea
My GF is looking for an apartment in specific areas of Berlin. She wants an apartment with specific characteristics (number of room, rent price, etc) and  to be able to get to her job using public transportation within an specific amount of time.
The goal of the project is to scrap information from places like ImmobilienScout24 to find a place, then based on the address calculate the time to her work location using Google directions API. So far only ImmobilienScout24 is supported but I plan to add more.

For now this is nothing more than a proof of concept.

## Run

    $ scrapy crawl immoscout24 -o items.json

Check the items.json file.
