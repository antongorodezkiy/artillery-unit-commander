from gettext import gettext as __
from os.path import exists as path_exists
import logging

import app.database as database

from app.commands.Goals import Goals
goals = Goals()

from app.commands.Reports import Reports
reports = Reports()

EXIT_TRIGGER = 0

def main(trigger = None):

	# actions
	actions = _get_actions()

	# choose action ui
	print("\n" + __("Select action") + ": ")
	for action in actions:
		print(f"  {action['trigger']}. {action['name']}")

	if trigger is None:
		try:
			trigger = int(input("> "))
		except ValueError:
			trigger = None
		except (KeyboardInterrupt, EOFError):
			# handle ctrl+d
			return

	filtered_actions = filter(lambda action: (action['trigger'] == trigger), actions)

	try:
		action = next(filtered_actions)
	except:
		action = None

	# execute
	if action == None:
		_unknown_action()
	else:
		action["callback"]()

		if action["trigger"] == EXIT_TRIGGER:
			# exit
			return

	# restart
	main()

def _get_actions():
	actions = []
	if path_exists(f"./{database.path}"):
		actions = [
		 {
		 	"trigger": 1,
		 	"name": __("New Goal"),
		 	"callback": goals.new
		 },
		 {
		 	"trigger": 2,
		 	"name": __("Correction"),
		 	"callback": goals.correction
		 },
		 {
		 	"trigger": 3,
		 	"name": __("Shot"),
		 	"callback": goals.shot
		 },
		 {
		 	"trigger": 4,
		 	"name": __("Stop, write down"),
		 	"callback": goals.stop
		 },
		 {
		 	"trigger": 5,
		 	"name": __("Show report"),
		 	"callback": reports.report
		 }
		]
	else:
		actions = [
			 {
			 	"trigger": 1,
			 	"name": __("Install"),
			 	"callback": _install
			 }
		 ]

	actions += [
			{
				"trigger": EXIT_TRIGGER,
				"name": __("Exit"),
				"callback": _close
			}
		]

	return actions

def _close():
	print(__("Bye-bye"))

def _install():
	# need to load these here to create schema
	import app.models.Goal
	import app.models.Correction
	import app.models.Shot
	database.declarative_base.metadata.create_all(database.engine)

def _unknown_action():
	print(__("Unknown action called"))

if __name__ == "__main__":
	# TODO: testing
	default_action = 1
	main(default_action)
