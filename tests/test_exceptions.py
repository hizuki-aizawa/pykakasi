# -*- coding: utf-8 -*-

import pykakasi.kakasi
import pytest
from pykakasi.kakasi.exceptions import (InvalidFlagValueException,
                                        InvalidModeValueException,
                                        UnsupportedRomanRulesException)


def test_kakasi_unknown_rule():
    with pytest.raises(UnsupportedRomanRulesException):
        kakasi = pykakasi.kakasi.Kakasi()
        kakasi.setMode("H", "a")
        kakasi.setMode("K", "a")
        kakasi.setMode("J", "a")
        kakasi.setMode("r", "hogefuga")


def test_kakasi_unknown_mode():
    with pytest.raises(InvalidModeValueException):
        kakasi = pykakasi.kakasi.Kakasi()
        kakasi.setMode("H", "a")
        kakasi.setMode("K", "a")
        kakasi.setMode("J", "X")


def test_kakasi_invalid_flag_value():
    with pytest.raises(InvalidFlagValueException):
        kakasi = pykakasi.kakasi.Kakasi()
        kakasi.setMode("H", "a")
        kakasi.setMode("K", "a")
        kakasi.setMode("s", "yes")
