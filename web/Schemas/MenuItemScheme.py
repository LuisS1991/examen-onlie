from typing import List
from dataclasses import dataclass

@dataclass
class LinkWeb:
    name:str
    icon:str
    link:str


@dataclass
class MenuItemScheme(LinkWeb):
    subMenu: List[LinkWeb]
