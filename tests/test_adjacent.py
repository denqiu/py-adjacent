import numpy

import py_adjacent


def test_adjacent():
    """
    Generate a random array to test adjacent algorithm.

    1: Generate a random number or text.

    2: Generate a random size.

    3: Add repeated elements. Repeat until loop randomly becomes False.

    4: Shuffle elements a random number of times.

    5: Run adjacent algorithm.

    6: Put back the original array from the output and compare if equal or not.
    """
    generator = numpy.random.default_rng()
    random_array = numpy.array([])
    p_true, p_false = (1.0, 0.0)
    while generator.choice([True, False], p=[p_true, p_false], size=1)[0]:
        random_element = generator.integers(1, 10000)
        if generator.choice([True, False], 1)[0]:
            random_element = numpy.char.mod("text-%s", random_element)
        random_size = generator.integers(1, 1000)
        random_array = numpy.concatenate([random_array, numpy.repeat(random_element, random_size)])
        p_decimal = generator.uniform(high=p_true)
        p_true -= p_decimal
        p_false += p_decimal
    p_true, p_false = (1.0, 0.0)
    while generator.choice([True, False], p=[p_true, p_false], size=1)[0]:
        generator.shuffle(random_array)
        p_decimal = generator.uniform(high=p_true)
        p_true -= p_decimal
        p_false += p_decimal
    elements, counts = py_adjacent.count_adjacent_elements(random_array)
    print(elements)
    print(counts)
    original_array = numpy.repeat(elements, counts)
    assert (original_array == random_array).all()
