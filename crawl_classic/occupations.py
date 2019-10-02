from __future__ import annotations
from dataclasses import dataclass
from typing import Optional, Union


@dataclass
class Occupation:
    """Encapsulates a DCC Occupation, including what demi-races a lvl 0
    character can class into."""
    title: str
    # TODO: weapon, subclass of equipment
    weapon: str
    # TODO: make equipment obj
    goods: Union[str, Equipment]
    race: str = "Human"

    def __post_init__(self, *args, **kwargs):
        demi_races = ["Dwarven", "Elven", "Halfling"]
        demi_race = [r for r in demi_races if r in self.title]
        try:
            self.race = demi_race[0]
        except IndexError:
            pass


title = "title"
weapon = "weapon"
goods = "goods"

# fmt: off
OCCUPATIONS = [
    {title: "Alchemist", weapon: "Staff", goods: "Oil, 1 flask"},
    {title: "Animal trainer", weapon: "Club", goods: "Pony"},
    {title: "Armorer", weapon: "Hammer (as club)", goods: "Iron helmet"},
    {title: "Astrologer", weapon: "Dagger", goods: "Spyglass"},
    {title: "Barber", weapon: "Razor (as dagger)", goods: "Scissors"},
    {title: "Beadle", weapon: "Staff", goods: "Holy symbol"},
    {title: "Beekeeper", weapon: "Staff", goods: "Jar of honey"},
    {title: "Blacksmith", weapon: "Hammer (as club)", goods: "Steel tongs"},
    {title: "Butcher", weapon: "Cleaver (as axe)", goods: "Side of beef"},
    {title: "Caravan guard", weapon: "Short sword", goods: "Linen, 1 yard"},
    {title: "Cheesemaker", weapon: "Cudgel (as staff)", goods: "Stinky cheese"},
    {title: "Cobbler", weapon: "Awl (as dagger)", goods: "Shoehorn"},
    {title: "Confidence artist", weapon: "Dagger", goods: "Quality cloak"},
    {title: "Cooper", weapon: "Crowbar (as club)", goods: "Barrel"},
    {title: "Costermonger", weapon: "Knife (as dagger)", goods: "Fruit"},
    {title: "Cutpurse", weapon: "Dagger", goods: "Small chest"},
    {title: "Ditch digger", weapon: "Shovel (as staff)", goods: "Fine dirt, 1 lb."},
    {title: "Dwarven apothecarist", weapon: "Cudgel (as staff)", goods: "Steel vial"},
    {title: "Dwarven blacksmith", weapon: "Hammer (as club)", goods: "Mithril, 1 oz."},
    {title: "Dwarven blacksmith", weapon: "Hammer (as club)", goods: "Mithril, 1 oz."},
    {title: "Dwarven chest-maker", weapon: "Chisel (as dagger)", goods: "Wood, 10 lbs."},
    {title: "Dwarven herder", weapon: "Staff", goods: "Sow**"},
    {title: "Dwarven miner", weapon: "Pick (as club)", goods: "Lantern"},
    {title: "Dwarven miner", weapon: "Pick (as club)", goods: "Lantern"},
    {title: "Dwarven mushroom-farmer", weapon: "Shovel", goods: "Sack"},
    {title: "Dwarven rat-catcher", weapon: "Club", goods: "Net"},
    {title: "Dwarven stonemason", weapon: "Hammer", goods: "Fine stone, 10 lbs."},
    {title: "Dwarven stonemason", weapon: "Hammer", goods: "Fine stone, 10 lbs."},
    {title: "Elven artisan", weapon: "Staff", goods: "Clay, 1 lb."},
    {title: "Elven barrister", weapon: "Quill (as dart)", goods: "Book"},
    {title: "Elven chandler", weapon: "Scissors (as dagger)", goods: "Candles, 20"},
    {title: "Elven falconer", weapon: "Dagger", goods: "Falcon"},
    {title: "Elven forester", weapon: "Staff", goods: "Herbs, 1 lb."},
    {title: "Elven forester", weapon: "Staff", goods: "Herbs, 1 lb."},
    {title: "Elven glassblower", weapon: "Hammer", goods: "Glass beads"},
    {title: "Elven navigator", weapon: "Bow", goods: "Spyglass"},
    {title: "Elven sage", weapon: "Dagger", goods: "Parchment and quill pen"},
    {title: "Elven sage", weapon: "Dagger", goods: "Parchment and quill pen"},
    {title: "Farmer*", weapon: "Pitchfork (as spear)", goods: "Hen**"},
    {title: "Farmer*", weapon: "Pitchfork (as spear)", goods: "Hen**"},
    {title: "Farmer*", weapon: "Pitchfork (as spear)", goods: "Hen**"},
    {title: "Farmer*", weapon: "Pitchfork (as spear)", goods: "Hen**"},
    {title: "Farmer*", weapon: "Pitchfork (as spear)", goods: "Hen**"},
    {title: "Farmer*", weapon: "Pitchfork (as spear)", goods: "Hen**"},
    {title: "Farmer*", weapon: "Pitchfork (as spear)", goods: "Hen**"},
    {title: "Farmer*", weapon: "Pitchfork (as spear)", goods: "Hen**"},
    {title: "Farmer*", weapon: "Pitchfork (as spear)", goods: "Hen**"},
    {title: "Fortune-teller", weapon: "Dagger", goods: "Tarot deck"},
    {title: "Gambler", weapon: "Club", goods: "Dice"},
    {title: "Gongfarmer", weapon: "Trowel (as dagger)", goods: "Sack of night soil"},
    {title: "Grave digger", weapon: "Shovel (as staff)", goods: "Trowel"},
    {title: "Grave digger", weapon: "Shovel (as staff)", goods: "Trowel"},
    {title: "Guild beggar", weapon: "Sling", goods: "Crutches"},
    {title: "Guild beggar", weapon: "Sling", goods: "Crutches"},
    {title: "Halfling chicken butcher", weapon: "Hand axe", goods: "Chicken meat, 5 lbs."},
    {title: "Halfling dyer", weapon: "Staff", goods: "Fabric, 3 yards"},
    {title: "Halfling dyer", weapon: "Staff", goods: "Fabric, 3 yards"},
    {title: "Halfling glovemaker", weapon: "Awl (as dagger)", goods: "Gloves, 4 pairs"},
    {title: "Halfling gypsy", weapon: "Sling", goods: "Hex doll"},
    {title: "Halfling haberdasher", weapon: "Scissors (as dagger)", goods: "Fine suits, 3 sets"},
    {title: "Halfling mariner", weapon: "Knife (as dagger)", goods: "Sailcloth, 2 yards"},
    {title: "Halfling moneylender", weapon: "Short sword", goods: "5 gp, 10 sp, 200 cp"},
    {title: "Halfling trader", weapon: "Short sword", goods: "20 sp"},
    {title: "Halfling vagrant", weapon: "Club", goods: "Begging bowl"},
    {title: "Healer", weapon: "Club", goods: "Holy water, 1 vial"},
    {title: "Herbalist", weapon: "Club", goods: "Herbs, 1 lb."},
    {title: "Herder", weapon: "Staff", goods: "Herding dog**"},
    {title: "Hunter", weapon: "Shortbow", goods: "Deer pelt"},
    {title: "Hunter", weapon: "Shortbow", goods: "Deer pelt"},
    {title: "Indentured servant", weapon: "Staff", goods: "Locket"},
    {title: "Jester", weapon: "Dart", goods: "Silk clothes"},
    {title: "Jeweler", weapon: "Dagger", goods: "Gem worth 20 gp"},
    {title: "Locksmith", weapon: "Dagger", goods: "Fine tools"},
    {title: "Mendicant", weapon: "Club", goods: "Cheese dip"},
    {title: "Mercenary", weapon: "Longsword", goods: "Hide armor"},
    {title: "Merchant", weapon: "Dagger", goods: "4 gp, 14 sp, 27 cp"},
    {title: "Miller/baker", weapon: "Club", goods: "Flour, 1 lb."},
    {title: "Minstrel", weapon: "Dagger", goods: "Ukulele"},
    {title: "Noble", weapon: "Longsword", goods: "Gold ring worth 10 gp"},
    {title: "Orphan", weapon: "Club", goods: "Rag doll"},
    {title: "Ostler", weapon: "Staff", goods: "Bridle"},
    {title: "Outlaw", weapon: "Short sword", goods: "Leather armor"},
    {title: "Rope maker", weapon: "Knife (as dagger)", goods: "Rope, 100"},
    {title: "Scribe", weapon: "Dart", goods: "Parchment, 10 sheets"},
    {title: "Shaman", weapon: "Mace", goods: "Herbs, 1 lb."},
    {title: "Slave", weapon: "Club", goods: "Strange-looking rock"},
    {title: "Smuggler", weapon: "Sling", goods: "Waterproof sack"},
    {title: "Soldier", weapon: "Spear", goods: "Shield"},
    {title: "Squire", weapon: "Longsword", goods: "Steel helmet"},
    {title: "Squire", weapon: "Longsword", goods: "Steel helmet"},
    {title: "Tax collector", weapon: "Longsword", goods: "100 cp"},
    {title: "Trapper", weapon: "Sling", goods: "Badger pelt"},
    {title: "Trapper", weapon: "Sling", goods: "Badger pelt"},
    {title: "Urchin", weapon: "Stick (as club)", goods: "Begging bowl"},
    {title: "Wainwright", weapon: "Club", goods: "Pushcart***"},
    {title: "Weaver", weapon: "Dagger", goods: "Fine suit of clothes"},
    {title: "Wizard's apprentice", weapon: "Dagger", goods: "Black grimoire"},
    {title: "Woodcutter", weapon: "Handaxe", goods: "Bundle of wood"},
]
# fmt: on
