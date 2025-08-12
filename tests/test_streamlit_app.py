import pytest
from streamlit.testing.v1 import AppTest

def test_streamlit_app():
    at = AppTest.from_file("streamlit/app.py")
    at.run()
    assert not at.exception
    assert at.title[0].value == "EndpointSync - Unified Endpoint Management"
