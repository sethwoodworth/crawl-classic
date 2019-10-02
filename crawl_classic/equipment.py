from __future__ import annotations
from dataclasses import dataclass
from typing import Optional
import re
import string


@dataclass
class Equipment:
    title: str
    value: str
    unit: Optional[str] = None
    quantity: Optional[int] = None


_equipment = [
    ("Backpack", "2gp"),
    ("Candle", "1cp"),
    ("Chain, 10'", "30gp"),
    ("Chalk, 1 piece", "1cp"),
    ("Chest, empty", "2gp"),
    ("Crowbar", "2gp"),
    ("Flask, empty", "3cp"),
    ("Flint & steel", "15cp"),
    ("Grappling hook", "1gp"),
    ("Hammer, small", "5sp"),
    ("Holy symbol", "25gp"),
    ("Holy water, 1 vial**", "25gp"),
    ("Ironspikes, each", "1sp"),
    ("Lantern", "10gp"),
    ("Mirror, hand-sized", "10gp"),
    ("Oil, 1 flask***", "2sp"),
    ("Pole, 10-foot", "15cp"),
    ("Rations, per day", "5cp"),
    ("Rope, 50'", "25cp"),
    ("Sack, large", "12cp"),
    ("Sack, small", "8cp"),
    ("Thieves' tools", "25gp"),
    ("Torch, each", "1cp"),
    ("Waterskin", "5sp"),
]


EQUIPMENT = {}
#: Process the initial list of equipment tuples into a dict of Equipment classes
for name, cost in _equipment:
    kwargs = {}
    title = name.split(", ")[0]
    kwargs["title"] = title
    kwargs["value"] = cost
    if len(name.split(", ")) > 1:
        quantity = name.split(", ")[1]
        try:
            digits = int("".join([c for c in quantity if c.isdigit()]))
        except IndexError:
            digits = None

        if digits:
            kwargs["quantity"] = digits
            kwargs["unit"] = re.sub(r"[\d+\s]", "", quantity)
    EQUIPMENT[title] = Equipment(**kwargs)
