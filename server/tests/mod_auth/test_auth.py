# from doubles import allow
from mod_auth.auth import load_user  # , register, login
from run_tests import fixtures, app


class TestAuth:

    @fixtures('single_user.yml')
    def test_load_user(self):
        with app.test_request_context():
            user = load_user(1)
            assert user is not None
            assert user.username == 'ganemone'
