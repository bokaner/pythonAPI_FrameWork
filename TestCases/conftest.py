import html
import json

import allure
import pytest
import os

import requests
from allure_commons.types import AttachmentType


# Add command line options to pytest





# Log on failure fixture
@pytest.fixture()
def log_on_failure(request):
    yield
    item = request.node
    if hasattr(item, 'rep_call') and item.rep_call.failed:
        if hasattr(item, 'response'):
            allure.attach(item.response.request.body or '', name="Request Body", attachment_type=AttachmentType.JSON)
            allure.attach(item.response.text or '', name="Response Body", attachment_type=AttachmentType.JSON)
            allure.attach(str(item.response.status_code), name="Response Status Code",
                          attachment_type=AttachmentType.TEXT)


def allureLogs(text):
    with allure.step(text):
        pass



