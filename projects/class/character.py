from dataclasses import dataclass
from battle_dice.charactertype import CharacterType

# Instantiating an Enum member

my_character_type = CharacterType.WARRIOR

# Accessing name and value
print(my_character_type)
print(my_character_type.name) #Constant Name
print(my_character_type.value) #Actual Stored Value

@dataclass
class Character:
    name: str
    character_type: CharacterType
    health: int
    attack_power: int