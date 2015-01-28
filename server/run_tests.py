import pytest
import wtforms_json

wtforms_json.init()

pytest.main('-x tests/')
