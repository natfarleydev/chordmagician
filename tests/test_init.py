import random

import pytest

from hypothesis import given, settings
from hypothesis import strategies as st

from chordmagician import (
    pick_random_chord,
    generate_abc_score,
    generate_bars,
    generate_random_title,
    generate_full_exercise,
)


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
    random.seed(seed)
    assert pick_random_chord()


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


@given(st.integers(), st.integers(min_value=1, max_value=30), st.integers(min_value=1, max_value=30))
@settings(max_examples=10)
def test_generate_full_exercise(seed, lines, bars):
    random.seed(seed)
    assert generate_full_exercise(lines, bars)

@given(st.integers(), st.integers(max_value=0), st.integers(max_value=0))
@settings(max_examples=10)
def test_generate_full_exercise__raises_valueerror(seed, lines, bars):
    random.seed(seed)
    with pytest.raises(ValueError):
        generate_full_exercise(lines, bars)


@given(st.integers())
def test_generate_random_title(seed):
    random.seed(seed)
    assert generate_random_title()
