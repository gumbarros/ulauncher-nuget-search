from dataclasses import dataclass

@dataclass
class NuGetPackage:
    id: str
    title: str
    description: str