import pytest
from diff_cipher import dif_ciph  # Assuming the function is defined in 'task.py'

def test_dif_ciph_string_encoding():
    # Test encoding a string to a list of character codes and differences
    result = dif_ciph("Hello")
    assert result == [72, 29, 7, 0, 3]

def test_dif_ciph_list_decoding():
    # Test decoding a list of character codes and differences to a string
    result = dif_ciph([72, 33, -73, 84, -12, -3, 13, -13, -68])
    assert result == "Hi there!"

def test_dif_ciph_string_encoding_case_sensitive():
    # Test for a string with mixed case letters
    result = dif_ciph("Sunshine")
    assert result == [83, 34, -7, 5, -11, 1, 5, -9]

def test_dif_ciph_empty_string():
    # Test for an empty string (edge case)
    result = dif_ciph("")
    assert result == []

def test_dif_ciph_single_character():
    # Test for a single character string
    result = dif_ciph("A")
    assert result == [65]

def test_dif_ciph_special_characters():
    # Test for special characters in a string
    result = dif_ciph("!@#")
    assert result == [33, 12, -32]

def test_dif_ciph_list_decoding_special_characters():
    # Test for decoding a list with special characters
    result = dif_ciph([33, 12, -32])
    assert result == "!@#"

def test_dif_ciph_mixed_string():
    # Test a mixed string with both letters and numbers
    result = dif_ciph("a1b2c3")
    assert result == [97, 49, -48, 49, -48, 49]

def test_dif_ciph_mixed_list():
    # Test a mixed list of encoded values with letters and differences
    result = dif_ciph([97, 49, -48, 49, -48, 49])
    assert result == "a1b2c3"
