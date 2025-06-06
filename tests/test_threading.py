import concurrent.futures
import random

import pymorphy3

from test_parsing import PARSES
from utils import assert_parse_is_correct
def _check_analyzer(morph, parses):
    for word, normal_form, tag in parses:
        parse = morph.parse(word)
        assert_parse_is_correct(parse, normal_form, tag)


def _check_new_analyzer(parses):
    morph = pymorphy3.MorphAnalyzer()
    for word, normal_form, tag in parses:
        parse = morph.parse(word)
        assert_parse_is_correct(parse, normal_form, tag)


def _create_morph_analyzer():
    morph = pymorphy3.MorphAnalyzer()
    word, normal_form, tag = random.choice(PARSES)
    parse = morph.parse(word)
    assert_parse_is_correct(parse, normal_form, tag)


def test_threading_single_morph_analyzer(morph):
    with concurrent.futures.ThreadPoolExecutor(3) as executor:
        list(executor.map(_check_analyzer, [morph]*10, [PARSES]*10))


def test_threading_multiple_morph_analyzers():
    with concurrent.futures.ThreadPoolExecutor(3) as executor:
        list(executor.map(_check_new_analyzer, [PARSES]*10))


def test_threading_create_analyzer():
    with concurrent.futures.ThreadPoolExecutor(3) as executor:
        for _ in range(10):
            executor.submit(_create_morph_analyzer)
