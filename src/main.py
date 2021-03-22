from my_lunch import Lunch

def main():

	options = {
		0:{'bk':{'votes': 0}},
		1:{'mc':{'votes': 0}},
		2:{'bocattino':{'votes': 0}},
		3:{'mb':{'votes': 0}},
		4:{'padaria':{'votes': 0}}
	}

	lunch = Lunch(options)
	day = lunch.get_day_number()
	week = lunch.get_week_number()
	options_past_voted = lunch.load_past_week_choices(week)
	response, store_choice = lunch.choice_lunch_today(options_past_voted)

	if response is True:
		print(store_choice)
		status = lunch.save_choice(store_choice, week, day)
		print(status)


main()