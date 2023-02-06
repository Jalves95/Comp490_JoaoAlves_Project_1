import pytest
import database_functions

""" This file contains all unit tests """


def test_create_wufoo_db():

    assert database_functions.create_wufoo_db() is None


