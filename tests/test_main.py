import unittest
from main import merge_layers

class MergeTests(unittest.TestCase):
    def test_recursive_merge_and_trace(self):
        merged, trace = merge_layers([
            ("base", {"server": {"port": 8000, "host": "localhost"}}),
            ("local", {"server": {"port": 8080}})
        ])
        self.assertEqual(merged["server"], {"port": 8080, "host": "localhost"})
        self.assertEqual(trace[0]["key"], "server.port")
    def test_later_arrays_replace_earlier(self):
        merged, trace = merge_layers([("a", {"items": [1, 2]}), ("b", {"items": [3]})])
        self.assertEqual(merged["items"], [3])
        self.assertEqual(len(trace), 1)
