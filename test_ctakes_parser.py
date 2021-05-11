import os
import pytest

from ctakes_parser import ctakes_parser as parser

def test_parse_directory():
    in_dir = 'notes_in/'
    out_dir = 'notes_out/'

    parser.parse_dir(in_dir, out_dir)

    assert os.path.exists(os.path.join(out_dir, '11995.csv'))
    assert os.path.exists(os.path.join(out_dir, '18563.csv'))
    assert os.path.exists(os.path.join(out_dir, '133875.csv'))
    assert os.path.exists(os.path.join(out_dir, '150406.csv'))
    assert os.path.exists(os.path.join(out_dir, '180195.csv'))
    assert os.path.exists(os.path.join(out_dir, '182909.csv'))
    assert os.path.exists(os.path.join(out_dir, '189350.csv'))
    assert os.path.exists(os.path.join(out_dir, '210958.csv'))
    assert os.path.exists(os.path.join(out_dir, '241468.csv'))
    assert os.path.exists(os.path.join(out_dir, '379569.csv'))

if __name__ == '__main__':
    pytest.main(__file__)
