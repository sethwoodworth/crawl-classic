"""Crit tables are used when rolling the max value during an attack with a character's action dice.
For instance, if your action dice is a d20, and you roll 20, you get to roll on the appropriate crit table with your crit die.
Crit tables start at `0 or lower` and the last value is applied for rolls above the number of entries in the table.
"""
#: Crit Table I is used for lvl 0 characters and all wizards.
CRIT_TABLE_I = [
    "Force of blow shivers your weapon free of your grasp. Inflict +1d6 damage with this strike and you are disarmed.",
    "Opportunistic strike. Inflict +1d3 damage with this strike.",
    "Foe jabbed in the eye! Ugly bruising and inflict +1d4 damage with this strike.",
    "Stunning crack to forehead. Inflict +1d3 damage with this strike, and the foe falls to the bottom of the initiative count next round.",
    "Strike to foe’s kneecap. Inflict +1d4 damage with this strike and the foe suffers a -10’ penalty to speed until healed.",
    "Solid strike to torso. Inflict +1d6 damage with this strike.",
    "Lucky strike disarms foe. You gain a free attack if the enemy stoops to retrieve his weapon.",
    "Smash foe’s hand. Inflict +2d3 damage with this strike. You break two of the enemy’s fingers.",
    "Numbing strike! Cursing in agony, the foe is unable to attack next round.",
    "Smash foe’s nose. Inflict +2d4 damage with this strike and blood streams down the enemy’s face.",
    "Foe trips on his own feet and falls prone for the remainder of the round.",
    "Piercing strike. Inflict +2d4 damage with this strike.",
    "Strike to groin. The foe must make a DC 15 Fort save or spend the next two rounds retching.",
    "Blow smashes foe’s ankle; his movement speed is reduced by half.",
    "Strike grazes temple; blood blinds the foe for 1d3 rounds.",
    "Stab enemy’s weapon hand. The weapon is lost and knocked 1d10+5 feet away.",
    "Narrowly avoid foe’s counterstrike! Inflict normal damage and make another attack roll. If the second attack hits, you inflict an additional +1d6 damage.",
    "Blow to throat. Foe staggers around for 2 rounds and is unable to speak, cast spells, or attack.",
    "Foe falls into your attack. He takes +2d6 damage from the strike and curses your luck.",
    "Miracle strike. The foe must make a DC 20 Fort save or fall unconscious.",
    "Lucky blow dents foe’s skull! Inflict +2d6 damage with this strike. If the foe has no helm, he suffers a permanent loss of 1d4 Int.",
]
