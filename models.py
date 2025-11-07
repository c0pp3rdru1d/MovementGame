from dataclasses import dataclass, field, asdict
from typing import Dict, List

@dataclass
class Player:
    name: str = "E"
    health: int = 100
    sanity: int = 75
    resolve: int = 50
    inventory: Dict[str, int] = field(default_factory=dict)
    location: str = "cell"

    def add_item(self, item: str, qty: int = 1):
        self.inventory[item] = self.inventory.get(item, 0)

    def remove_item(self, item: str, qty: int = 1) -> bool:
        if self.inventory.get(item, 0) >= qty:
            self.inventory[item] -= qty
            if self.inventory[item] <= 0:
                del self.inventory[item]
            return True
        return False
    
@dataclass
class Location:
    key: str
    title: str
    description: str
    exits: Dict[str, str] # direction -> location key
    items: List[str] = field(default_factory=list)

@dataclass
class World:
    locations: Dict[str, Location] = field(default_factory=dict)

    def here(self, key: str) -> Location:
        return self.locations[key]
    