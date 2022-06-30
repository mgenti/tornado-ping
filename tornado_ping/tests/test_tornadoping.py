from tornado.testing import AsyncTestCase, gen_test

import tornado_ping


class TestTornadoPing(AsyncTestCase):
    @gen_test
    def test_verbose_ping(self):
        responses = yield tornado_ping.verbose_ping("127.0.0.1", count=5)
        self.assertEquals(len(responses), 5)

    @gen_test
    def test_unable_to_resolve(self):
        response = yield tornado_ping.ping("a-test-url-taht-is-not-available.com")
        self.assertIsNone(response)

    @gen_test
    def test_resolvable(self):
        response = yield tornado_ping.ping("github.com")
        self.assertIsNotNone(response)
        self.assertGreater(response, 0)
