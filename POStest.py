import pytest
from POSexcercise import *

#product found, product not found, empty barcode, null barcode

def test_output_test():
    assert on_barcode('12345') == '11,50'

def test_valid_input():
    on_barcode('12345')
    assert last_text_displayed() == "$11.50"

def test_invalid_input_blank_string():
    on_barcode("")
    assert last_text_displayed() == "Scanning error: empty barcode"

def test_input_non_number_characters():
    on_barcode("junk")
    assert last_text_displayed() == "invalid"

def test_string_with_trailing_space_invalid_input():
    on_barcode("54321 ")
    assert last_text_displayed() == "$12.50"

def test_string_with_trailing_tab_invalid_input():
    on_barcode("34235\t")
    assert last_text_displayed() == "invalid"

def test_valid_input():
    on_barcode('56789')
    assert last_text_displayed() == "$22.50"

