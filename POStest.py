import pytest
from POSexcercise import *

#product found, product not found, empty barcode, null barcode

def test_output_test():
    assert Sale('12345') == '11,50'

def test_valid_input():
    Sale('12345')
    assert last_text_displayed() == "$11.50"

def test_invalid_input_blank_string():
    Sale("")
    assert last_text_displayed() == "Scanning error: empty barcode"


def test_string_with_trailing_space_invalid_input():
    Sale("54321")
    assert last_text_displayed() == "Product not found for:54321"

def test_string_with_trailing_tab_invalid_input():
    Sale("34235")
    assert last_text_displayed() == "Product not found for:34235"

def test_valid_input():
    Sale('56789')
    assert last_text_displayed() == "$22.50"

def test_lookup_table():
    Sale('56789')
    assert last_text_displayed() == "$22.50"

