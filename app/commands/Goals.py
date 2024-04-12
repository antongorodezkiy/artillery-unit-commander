import logging as l
import datetime
from sqlalchemy.orm import Session
from sqlalchemy import select
from gettext import gettext as __

from app.models.Goal import Goal
from app.models.Correction import Correction
from app.models.Shot import Shot
import app.database as database

class Goals:
	current_goal = None
	current_correction = None
	corrections = []

	# Vegas, take new goal
	def new(self, name = None):
		if name is None:
			try:
				# TODO: sanitize string
				name = input(__("Name (optional)") + ": ")
			except (KeyboardInterrupt, EOFError):
				# handle ctrl+d
				return

		with Session(database.engine) as session:
			goal = Goal()
			goal.created_at = datetime.datetime.now()
			if name is not None:
				goal.name = name
			session.add(goal)
			session.commit()

			self.current_goal = goal

		return self.current_goal

	# Vegas, select the goal
	def select(self):
		name = None
		try:
			# TODO: sanitize string
			name = input(__("Name") + ": ")
		except (KeyboardInterrupt, EOFError):
			# handle ctrl+d
			return

		if not name:
			print(__("No goal name specified"))
			return

		# TODO: find by name
		self.current_goal = Goal(name)

		if not self.current_goal:
			print(__("No current goal found"))
			return

	# Vegas, take new correction
	def correction(self):
		sight = None
		angle = None

		# TODO: testing
		sight = 6
		angle = 6

		try:
			while not sight:
				sight = input(__("Sight") + ": ").astype(int)
				l.warning(f"Sight: {sight}")

			while not angle:
				angle = input(__("Angle") + ": ").astype(float)
				l.error(f"Angle: {angle}")

		except (KeyboardInterrupt, EOFError):
			# handle ctrl+d
			return
		# TODO: handle ValueError
		# except ValueError:
		#   print("Looks like value error")

		with Session(database.engine) as session:
			if self.current_goal is None:
				self.new(name = '')

			correction = Correction()
			correction.goal = self.current_goal
			correction.sight = sight
			correction.angle = angle
			correction.created_at = datetime.datetime.now()
			session.add(correction)

			result = session.commit()
			print(repr(result))
			self.current_correction = correction

	# Fire!
	def shot(self):
		if self.current_correction is None:
			print("We do not have current correction")
			return

		with Session(database.engine) as session:
			shot = Shot()
			shot.correction = self.current_correction
			shot.created_at = datetime.datetime.now()
			session.add(shot)

			result = session.commit()
			print(repr(result))

	# Vegas, stop, write down the goal
	def stop(self):
		try:
			# TODO: sanitize string
			name = input(__("Name") + ": ")
		except (KeyboardInterrupt, EOFError):
			# handle ctrl+d
			return

		with Session(database.engine) as session:
			self.current_goal = session.query(Goal).filter(Goal.name == name).first()

			if not self.current_goal:
				print(__("No current goal found"))
				return

			self.current_goal.name = name

			session.add(self.current_goal)
			result = session.commit()
