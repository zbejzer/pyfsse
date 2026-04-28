from typing import Any, Dict, List, Optional, TypedDict, Union

# ==========
# Sub-Models
# ==========


class HealthDict(TypedDict):
    healthValue: float
    radiationValue: float
    permaDeath: bool
    lastLevelUpdated: int
    maxHealth: float


class ExperienceDict(TypedDict):
    experienceValue: float
    currentLevel: int
    storage: int
    accum: int
    needLvUp: bool
    wastelandExperience: int


class StatEntry(TypedDict):
    value: int
    mod: int
    exp: float


class StatsDict(TypedDict):
    stats: List[StatEntry]


class EquipmentDict(TypedDict):
    id: str
    type: str
    hasBeenAssigned: bool
    hasRandonWeaponBeenAssigned: bool


# ========================
# Dweller and Actor Models
# ========================


class DwellerDict(TypedDict):
    serializeId: int
    name: str
    lastName: str
    health: HealthDict
    experience: ExperienceDict
    stats: StatsDict
    gender: int
    equipedOutfit: EquipmentDict
    equipedWeapon: EquipmentDict
    # Adding Any for fields not relevant to the HP-renaming logic
    # like happiness, relations, pregnant, etc.
    _extra: Any


class ActorDict(TypedDict):
    """Represents non-dweller entities like Mr. Handy."""

    characterType: int
    serializeId: int
    name: str
    health: float  # Actors use a simple float for health, unlike Dwellers
    savedRoom: int
    MrHandyVariantID: Optional[str]


# ===================
# Top-Level Container
# ===================


class DwellerManagerDict(TypedDict):
    """The 'dwellers' key in the root JSON contains this structure."""

    dwellers: List[DwellerDict]
    actors: List[ActorDict]
    id: int
    mrhId: int
    min_happiness: float


class SaveFileSchema(TypedDict):
    """The root of the Vault.sav JSON file."""

    dwellers: DwellerManagerDict
