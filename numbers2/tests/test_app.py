import pytest
import app

def test_app_get0():
    assert len(app.get())==4

def test_app_get1():
    assert type(app.get())==str