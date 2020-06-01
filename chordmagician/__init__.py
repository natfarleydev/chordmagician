import logging
import random
import os 
dir_path = os.path.dirname(os.path.realpath(__file__))

import yaml

logger = logging.getLogger(__name__)

from .animal_names import animals

# TODO possibly replace this with a yaml file that is configurable
CHORDS = yaml.safe_load(open(os.path.join(dir_path, "config.yaml")))['chords']

WORDS = [
    "courage",
    "bravery",
    "foolishness",
    "mockery",
    "interest",
    "fantastic tale",
    "rupture",
    "adventure",
    "heartbreak",
    "pomplamoose",
    "betrayal",
]


def generate_random_title():
    title = random.choice(animals)
    if title[-1] == "s":
        title = title + "' "
    else:
        title = title + "'s "
    title += random.choice(WORDS)
    return title


def pick_random_chord(chords=CHORDS, prev_chord=""):
    """Picks a random chord given input (above)."""

    ret_chord = prev_chord
    try_number = 0
    while ret_chord == prev_chord:
        pitch = random.choice(list(chords.keys()))
        allowed_type = random.choice(chords[pitch])
        ret_chord = pitch + allowed_type

        try_number += 1
        if try_number > 100:
            raise RuntimeError(f"Unable to find a different chord to {prev_chord}")

    return ret_chord


def generate_bars(no_of_bars=32, *args, **kwargs) -> list:
    """Generates a list of bars with random chord symbols.

    *args, **kwargs are passed to pick_random_chord(...).

    """
    bars = []
    prev_chord = ""
    for _ in range(no_of_bars):
        chord = pick_random_chord(*args, **kwargs, prev_chord=prev_chord)
        bar = generate_bar(chord)
        bars.append(bar)
        prev_chord = chord

    return bars


def generate_rest_bars(no_of_bars=32, *args, **kwargs) -> list:
    """Generates no_of_bars with semibreve rest in.
    
    *args, **kwargs are ignored; they are kept for compatibility with generate_bars.
    
    """
    return ["z1"] * no_of_bars


def generate_abc_score(
    content,
    bass_content=None,
    title=None,
    author="Chord Magician",
    reference_number=1,
    meter="C",
    key="C",
    base_note_length="1/1",
):
    """ Generates an ABC score from input. """

    if bass_content is None:
        bass_content = content

    if title is None:
        title = generate_random_title()

    return f"""
X:{reference_number}
T:{title}
M:{meter}
L:{base_note_length}
K:{key}
%%staves {{1 2}}
V:1
[K:{key} clef=treble]{content}
V:2
[K:{key} clef=bass]{bass_content}
"""


def generate_bar(chord):
    """Given a chord, generates a bar with a semibreve in and the chord symbol."""
    return f'"{chord}"  z1'


def generate_full_exercise(no_of_lines: int = 2, bars_per_line: int = 8) -> str:
    """Generates the content of a full exercise in ABC notation and returns it as a string.

    no_of_lines: Number of lines for the exercise
    bars_per_line: Number of bars per line
    
    """
    if no_of_lines < 1:
        raise ValueError("no_of_lines should be greater than 0")

    if bars_per_line < 1:
        raise ValueError("bars_per_line should be greater than 0")

    return generate_abc_score(
        "\n".join(
            [
                "|" + "|".join(generate_bars(bars_per_line)) + "|"
                for _ in range(no_of_lines)
            ]
        ),
        "\n".join(
            [
                "|" + "|".join(generate_rest_bars(bars_per_line)) + "|"
                for _ in range(no_of_lines)
            ]
        ),
    )


def main():
    print(generate_full_exercise())
