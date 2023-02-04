import requests
from nuget_package import NuGetPackage

SEARCH_URL = "https://azuresearch-ussc.nuget.org/query"
PACKAGE_URL = "https://www.nuget.org/packages/"

def get_nuget_packages(query: str, take: int) -> list[NuGetPackage]:
    r = requests.get(SEARCH_URL, params={"q": query, "take": take})
    json: dict = r.json()

    for package in json["data"]:
        yield NuGetPackage.from_dict(package)