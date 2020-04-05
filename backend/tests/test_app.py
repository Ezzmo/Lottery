import pytest
import app

def test_app_get0():
    assert len(app.roll())==6

def test_app_get1():
    assert type(app.roll())==str