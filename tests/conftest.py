import pytest


@pytest.fixture(scope='session')
def morph():
    import pymorphy3
    return pymorphy3.MorphAnalyzer()


@pytest.fixture(scope='session')
def Tag(morph):
    return morph.TagClass
