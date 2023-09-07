# pip install PyGithub
from github import Github

VERSION = "3.6.0"
STOP_VERSION = "3.5.0"
MODEL = "sm"
ending = MODEL + "-" + VERSION

REPO = "https://github.com/explosion/spacy-models"
g = Github()

repo = g.get_repo("explosion/spacy-models")

# Search for all releases that contain the string ending
releases = repo.get_releases()
for release in releases:
    print(release)
    if STOP_VERSION in release.title:
        break
    if ending in release.title:
        print("Downloading: " + release.title)
        assets = release.get_assets()
        # Download the asset ending in .whl
        for asset in assets:
            if asset.name.endswith(".whl"):
                url = asset.browser_download_url
                print("Downloading: " + url)
                # Download the file
                import urllib.request
                urllib.request.urlretrieve(url, asset.name)
                break
    # Wait for 0.5 seconds to avoid rate limiting
    import time
    time.sleep(0.5)

