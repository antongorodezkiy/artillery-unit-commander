from sqlalchemy.orm import Session
import logging as l
from gettext import gettext as __

import app.database as database
from app.models.Correction import Correction
from app.helpers.Cli import CLIHelper

cli = CLIHelper()

class Reports:
	
	def report(self):
		
		with Session(database.engine) as session:
			
			corrections = session.query(Correction) \
				.limit(100) \
				.all()
				
			column_names = [
				 "#",
				 __("Goal"),
				 __("Sight"),
				 __("Angle"),
				 __("Date")
				]
			
			data = []
			for correction in corrections:
				# TODO: need to optimize this db query
				goal = correction.goal
				
				goal_column = ""
				if correction.goal:
					goal_column = f"{goal.name if goal.name else ''}, {goal.id}"
				
				data.append([
						correction.id,
						goal_column,
						correction.sight,
						correction.angle,
						"TODO"
					])
			  
			cli.table(column_names, data)
