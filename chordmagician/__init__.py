import logging
import random

logger = logging.getLogger(__name__)

from .animal_names import animals

# TODO possibly replace this with a yaml file that is configurable
CHORDS = {
    "A": ["Δ"],
    "Bb": ["Δ"],
    "B": ["Δ"],
    "C": ["Δ"],
    "Db": ["Δ"],
    "D": ["Δ"],
    "Eb": ["Δ"],
    "E": ["Δ"],
    "F": ["Δ"],
    "Gb": ["Δ"],
    "G": ["Δ"],
    "Ab": ["Δ"],
}


def pick_random_chord(chords=CHORDS, seed=None, prev_chord=""):
    """Picks a random chord given input (above)."""

    if seed is not None:
        random.seed(seed)

    ret_chord = prev_chord
    try_number = 0
    while ret_chord == prev_chord:
        pitch = random.choice(list(chords.keys()))
        allowed_type = random.choice(chords[pitch])
        ret_chord = pitch + allowed_type

        try_number += 1
        if try_number > 100:
            raise RuntimeError(f"Unable to find a different chord to {prev_chord}")

    # if ret_chord == "":
    #     raise RuntimeError("Um... not sure how this happened! ret_chord has not been set!")
    return ret_chord


def generate_bars(no_of_bars=32, *args, **kwargs):
    bars = []
    prev_chord = ""
    for _ in range(no_of_bars):
        chord = pick_random_chord(*args, **kwargs, prev_chord=prev_chord)
        bar = generate_bar(chord)
        bars.append(bar)
        prev_chord = chord

    return bars

WORDS  = [
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

def generate_abc_score(
    content,
    title=None,
    author="Chord Magician",
    reference_number=1,
    meter="C",
    key="C",
    base_note_length="1/1",
):
    """ Generates an ABC score from input. """

    if title is None:
        title = random.choice(animals)
        if title[-1] == "s":
            title = title + "' "
        else:
            title = title + "'s "
        title += random.choice(WORDS)

    return f"""
X:{reference_number}
T:{title}
M:{meter}
L:{base_note_length}
K:{key}
{content}
"""


def generate_bar(chord):
    return f'"{chord}"  y z1 y'

def main():
    print(generate_abc_score("|" + "|".join(generate_bars(8)) + "\n" + "|".join(generate_bars(8)) + "||"))
