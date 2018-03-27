# magneto
searches and pulls magnet links off a website via cli

v1.0 This is basically the end goal portion of this project. That goal being able to obtain the info hash for the torrent you are trying to download. This does a basic scrape of a website by parsing the html with BeautifulSoup and going through the tags to pull the magnet link. While the info hash is the only thing needed to be able to connect to any given torrent's swarm of seeders and leechers by just adding `magnet:?xt=urn:btih:` in front of it, this will pull the full magnet link available on the page.
