""" test the hello module"""
import toware.hello


def test_hello():
    assert "hello" == toware.hello.hello()
