import random

from hypothesis import given, settings
from hypothesis import strategies as st

from chordmagician import pick_random_chord, generate_abc_score, generate_bars


def test_pick_random_chord():
    assert pick_random_chord()


def test_generate_abc_score__sanity_check():
    assert generate_abc_score("")


@given(st.integers())
@settings(max_examples=100)
def test_generate_bars(seed):
    random.seed(seed)
    bars = generate_bars()
    for i in range(1, len(bars)):
        assert bars[i] != bars[i - 1]


@given(st.integers())
def test_pick_random_chord__with_seed(seed):
    assert pick_random_chord(seed=seed)


@given(st.integers())
@settings(max_examples=100)
def test_pick_random_chord__no_chord_twice_in_a_row(seed):
    random.seed(seed)
    chord1 = pick_random_chord()
    chord2 = pick_random_chord(prev_chord=chord1)
    chord3 = pick_random_chord(prev_chord=chord2)
    chord4 = pick_random_chord(prev_chord=chord3)

    assert chord1 != chord2
    assert chord2 != chord3
    assert chord3 != chord4
