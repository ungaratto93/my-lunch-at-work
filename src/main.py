from lunch import Lunch

def main():

	options = {
		0:{'bk':{'votes': 0}},
		1:{'mc':{'votes': 0}},
		2:{'bocattino':{'votes': 0}},
		3:{'mb':{'votes': 0}},
		4:{'padaria':{'votes': 0}}
	}

	lunch = Lunch(options)
	options_past_voted = lunch.load_past_week_choices()
	lunch.choice_lunch_today(options_past_voted)

main()