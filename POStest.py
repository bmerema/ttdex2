import pytest
from POSexcercise import *

#product found, product not found, empty barcode, null barcode

def test_output_test():
    assert Sale('12345') == '11,50'

def test_valid_input():
    sale('12345')
    assert last_text_displayed() == "$11.50"

def test_invalid_input_blank_string():
    sale("")
    assert last_text_displayed() == "Scanning error: empty barcode"

def test_input_non_number_characters():
    sale("junk")
    assert last_text_displayed() == "invalid"

def test_string_with_trailing_space_invalid_input():
    sale("54321")
    assert last_text_displayed() == "Product not found for:54321"

def test_string_with_trailing_tab_invalid_input():
    sale("34235\t")
    assert last_text_displayed() == "invalid"

def test_valid_input():
    sale('56789')
    assert last_text_displayed() == "$22.50"

def test_lookup_table():
    sale('56789')
    assert last_text_displayed() == "$22.50"

