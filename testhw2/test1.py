import pytest
from task1 import get_longest_diverse_words, get_rarest_char, count_punctuation_chars, count_non_ascii_chars, \
    get_most_common_non_ascii_char


@pytest.mark.parametrize(
    "file,list",
    [
        ('../TASK/data.txt', ['3-608-93071-X\n\nSchutzumschlag:\nAutograph', '3-608-95022-2\n\nMaxima-Minima\nAdnoten',
                              'Heilungen.\n\nSelbstverständlich', 'her-\nauf.\n\n\nÜBERSICHT\n\n1.',
                              'außenpolitisch\nbemerkbar', 'Waldgänger.\nHistorisch', 'Maskenwelt\nhinausgeführt.',
                              'Souveränitätsan-\nsprüche', 'Mensch\nauftrete.\n\nSoviel', 'mythische\nZeugungskraft.'])
    ],
)
def test_get_longest_diverse_words(file: str, list):
    result = get_longest_diverse_words(file)
    assert result == list


@pytest.mark.parametrize(
    "file,rare_letter",
    [
        ('../TASK/data.txt', '›')
    ],
)
def test_get_rarest_char(file: str, rare_letter):
    result = get_rarest_char(file)
    assert result == rare_letter


@pytest.mark.parametrize(
    "file,quantity",
    [
        ('../TASK/data.txt', 5302)
    ],
)
def test_count_punctuation_chars(file: str, quantity):
    result = count_punctuation_chars(file)
    assert result == quantity


@pytest.mark.parametrize(
    "file,c",
    [
        ('../TASK/data.txt', 189738)
    ],
)
def test_count_non_ascii_chars(file: str, c):
    result = count_non_ascii_chars(file)
    assert result == c


@pytest.mark.parametrize(
    "file,most_common_letter",
    [
        ('../TASK/data.txt', 'ä')
    ],
)
def test_get_most_common_non_ascii_char(file: str, most_common_letter):
    result = get_most_common_non_ascii_char(file)
    assert result == most_common_letter