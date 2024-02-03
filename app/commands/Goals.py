import sys
import logging as l
from sqlalchemy.orm import Session

from gettext import gettext as __
from app.models.Goal import Goal
from app.models.Correction import Correction 
import app.database as database

class Goals:
	current_goal = None
	corrections = []
	
	def new(self):
		sight = None
		angle = None
		
		# TODO: testing
		sight = 6
		angle = 6
		
		try:
			while not sight:
				sight = int(input(__("Sight") + ": "))
				l.warning(f"Sight: {sight}")
			
			while not angle:
				angle = float(input(__("Angle") + ": "))
				l.error(f"Angle: {angle}")
			
		except KeyboardInterrupt:
			# handle ctrl+d
			return
		# TODO: handle ValueError
		# except ValueError:
		#   print("Looks like value error")
			
		with Session(database.engine) as session:
			if self.current_goal == None:
				goal = Goal()
				session.add(goal)
				self.current_goal = goal
			
			correction = Correction()
			correction.goal = self.current_goal
			correction.sight = sight
			correction.angle = angle
			session.add(correction)
			
			result = session.commit()
			print(repr(result))
		
	def shot(self):
		pass
	def correction(self):
		pass
	def stop(self):
		try:
			# TODO: sanitize string
			name = input(__("Name") + ": ")
		except KeyboardInterrupt:
			# handle ctrl+d
			return
		
		goal_id = None
		if self.current_goal == None:
			try:
				while not goal_id:
					goal_id = input(__("Goal ID") + ": ").astype(int)
			except KeyboardInterrupt:
				# handle ctrl+d
				return
				
			print(goal_id)
			self.current_goal = Goal(goal_id)
			
		if not self.current_goal:
			print(__("No current goal found"))
			return
			
		self.current_goal.name = name
		
		with Session(database.engine) as session:
			session.add(self.current_goal)
			result = session.commit()
		
