import random
from typing import Optional
from models import Player, World


class AntagonistAI: 
    """ 
    Minimal reactive antagonist AI:
    -Mood affects frequency/intensity
    -Reacts to 'talk', 'use', entering specific rooms,
    and health/sanity checks"""

    def __init__(self, name="Mock"):
        self.name = name
        self.mood = 0 # -10 (placid)...0...+10 (agitated)
        self._taunts_neutral = [
            "Why do you persist, {player}? Entropy is patient and so am I."
        ]