import unittest

from app.commands.Goals import Goals

class GoalsTest(unittest.TestCase):
	
	def test_new(self):
		goals = Goals()
		goal = goals.new()
		print(goal)
		self.assertEqual(1, 1)
