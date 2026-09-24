import os
import sys
import unittest


if __package__ is None or __package__ == "":
	sys.path.insert(0, os.path.dirname(os.path.dirname(__file__)))


from core.checker import check_step, is_final_answer


class CheckerTests(unittest.TestCase):
	def test_accepts_equivalent_linear_steps(self):
		self.assertTrue(check_step("2x + 5 = 15", "2x = 15 - 5"))
		self.assertTrue(check_step("2x = 15 - 5", "2x / 2 = 10 / 2"))
		self.assertTrue(check_step("2x / 2 = 10 / 2", "x = 5"))

	def test_rejects_invalid_step(self):
		self.assertFalse(check_step("2x + 5 = 15", "2x = 15"))

	def test_detects_final_answer(self):
		self.assertTrue(is_final_answer("x = 5"))
		self.assertFalse(is_final_answer("2x = 10"))


if __name__ == "__main__":
	unittest.main()
