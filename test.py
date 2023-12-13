import unittest
from post import PostMachine

class TestPostMachine(unittest.TestCase):
    def test_run_case1(self):
        pm = PostMachine()
        pm.add_command(">")
        pm.add_command("0")
        pm.add_command("? 3 5")
        pm.add_command("1")
        pm.run()
        self.assertEqual(pm.get_tape(), "001")

    def test_run_case2(self):
        pm = PostMachine()
        pm.add_command(">")
        pm.add_command("1")
        pm.add_command("? 3 5")
        pm.add_command("0")
        pm.run()
        self.assertEqual(pm.get_tape(), "010")

    def test_run_case3(self):
        pm = PostMachine()
        pm.add_command(">")
        pm.add_command("? 3 5")
        pm.add_command("0")
        pm.add_command("1")
        pm.run()
        self.assertEqual(pm.get_tape(), "010")

   

if __name__ == '__main__':
    unittest.main()