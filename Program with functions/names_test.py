from names import make_full_name, extract_family_name, extract_given_name
import pytest

def test_make_full_name():
    assert make_full_name('Sally', 'Brown') == 'Brown; Sally'
    full_name = make_full_name('Lin-manuel', 'Miranda')
    assert full_name == 'Miranda; Lin-manuel'

def test_extract_family_name():
    family_name = extract_family_name('Brown; Sally')
    assert family_name == 'Brown'

def test_extract_given_name():
    given_name = extract_given_name('Brown; Sally')
    assert given_name == 'Sally'

pytest.main(['-v', '--tb=line', '-rN', 'names_test.py'])     
