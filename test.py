#!/usr/bin/env python3
from unittest.mock import patch

import nose2


class Test(object):
    @classmethod
    def setUp(cls):
        cls.patched_methods = [
        #     'f',
        # self.mocks['f'].return_value = make_hostname()
        ]
        cls.patchers = {
            method: patch(method) for method in cls.patched_methods
        }
        cls.mocks = {
            method: p.start() for method, p in cls.patchers.items()
        }

    @classmethod
    def tearDown(cls):
        for patcher in cls.patchers.values():
            patcher.stop()

    def test_index(self):
        response = None
        assert 'Welcome' in response


if __name__ == "__main__":
    nose2.main()
