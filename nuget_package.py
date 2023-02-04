from dataclasses import dataclass
import dataclasses
from typing import Optional


@dataclass
class NuGetPackage:
    id: str
    title: str
    description: str

    @classmethod
    def from_dict(self, dict):
        keys = [f.name for f in dataclasses.fields(self)]

        data = {key: dict[key] for key in dict if key in keys}

        instance = self(**data)

        return instance
