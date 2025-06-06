import logging
import sys

import pytest
from click.testing import CliRunner

from pymorphy3 import cli


def run_pymorphy3(args=()):
    if sys.version_info >= (3, 10):
        runner = CliRunner()
    else:
        runner = CliRunner(mix_stderr = False)
    results = runner.invoke(cli.main, args)

    return results.stdout, results.stderr

def test_show_usage():
    out = ' '.join(run_pymorphy3([]))
    assert 'Usage:' in out


def test_show_memory_usage():
    pytest.importorskip("psutil")
    out = ' '.join(run_pymorphy3(['dict', 'mem_usage']))
    assert 'Memory usage:' in out


def test_show_dict_meta(morph):
    meta = morph.dictionary.meta
    out = ' '.join(run_pymorphy3(['dict', 'meta']))
    assert meta['compiled_at'] in out


def test_parse_basic(tmpdir):
    logging.raiseExceptions = False
    try:
        p = tmpdir.join('words.txt')
        p.write_text("""
        крот пришел
        """, encoding='utf8')
        out, err = run_pymorphy3(["parse", str(p)])
        print(out)
        print(err)
        assert out.strip() == """
крот{крот:1.000=NOUN,anim,masc sing,nomn}
пришел{прийти:1.000=VERB,perf,intr masc,sing,past,indc}
        """.strip()
    finally:
        logging.raiseExceptions = True
