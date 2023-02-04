import requests
from nuget_package import NuGetPackage

SEARCH_URL = "https://azuresearch-ussc.nuget.org/query"
PACKAGE_URL = "https://www.nuget.org/packages/"

def get_nuget_packages(query: str, take: int) -> list[NuGetPackage]:
    request = requests.get(SEARCH_URL, params={"q": query, "take": take}, verify=False)
    json: dict = request.json()

    for package in json["data"]:
        yield NuGetPackage(package["id"],package["title"],package["description"])
        