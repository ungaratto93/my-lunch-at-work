
from datetime import datetime
import pprint
import logging
import os


class Lunch(object):
	"""docstring for Lunch"""
	def __init__(self, options):
		super(Lunch, self).__init__()
		self.options = options
	
	def get_options(self):
		"""get options to be voted"""
		return self.options

	def load_past_week_choices(self, week_number):
		"""Return options choiced on this week, load files pasted voted on weeknumber"""
		was_voted = ''
		try:
			basepath = os.getcwd() + str('\\')
			for filename in os.listdir(basepath):
			    if filename.endswith(".txt") and str(week_number) in filename: 
			        print(os.path.join("\\", filename))

			        with open(basepath + filename) as openfile:    
			            for line in openfile:
			            	print(line)
			            	was_voted = was_voted + line + ',' 

		except Exception as e:
			raise e
		return was_voted

	def get_day_number(self):
		try:
			week_day = datetime.today().weekday()+1
		except NameError as e:
			logging.error(e)
			logging.warn('You need import datetime lib')
		return week_day

	def get_week_number(self):
		try:
			# two // divide and return int
			week_number = (datetime.now().day - 1) // 7 + 1
		except NameError as e:
			logging.error(e)
			logging.warn('You need import datetime lib')
		return week_number

	def get_keyname(self, options, choice):
		key_name = ''
		try:
			for key in options[choice].keys():
				key_name = key
		except Exception as e:
			logging.error(e)
		return key_name

	def save_choice(self, choice, week_number, week_day):
		try:
			with open(''+datetime.now().strftime("%y_"+str(week_number)+"_"+str(week_day)) + '.txt', 'w', encoding='utf-8') as logfile:
				logfile.write(str(choice))
			response = "choice was saved ? " + str(True)
		except Exception as e:
			logging.error(e)
			response = "choice was saved ? " + str(False)
		return response

	def choice_lunch_today(self, options_past_voted):
		"""Make a votation based on options and quantity coworkers participants"""
		try:
			print('Enter quantity of participants:')
			players = int(input())
			index = 0
			key_choice = ''
			response = None
			while index < players:
				print(str(index) + ' Make your choice:')
				choice = int(input())
				key = self.get_keyname(self.options, choice)
				print('Your choice is: ' + str(key))
				print('Before your vote: ' + str(self.options[choice][key]['votes']))
				votes = self.options[choice][key]['votes']
				votes = votes + 1
				self.options[choice][key]['votes'] = votes
				print('Now with your vote: ' + str(self.options[choice][key]['votes']))

				index = index + 1
				pprint.pprint(self.options)

			zindex =0
			compute_votes = 0
			key = ''
			while zindex < len(self.options):
				key_list = list(self.options[zindex].keys())
				access_key = str(key_list[0])
				if compute_votes < self.options[zindex][access_key]['votes']:
					compute_votes = self.options[zindex][access_key]['votes']
					key = access_key
				zindex = zindex + 1

			print('key selected ' + str(key) + ' with ' + str(compute_votes) + ' votes ')
			print('Options past voted was: ' + str(options_past_voted))

			if key in options_past_voted:
				response = False
				logging.warning('Cannot be repeated! Run again!')
			else:
				response = True

		except TypeError as e:
			logging.error(e)
			logging.warn('input a integer number')
		except ValueError as e:
			logging.error(e)
			logging.warning('input a integer number')		
		return response, key
