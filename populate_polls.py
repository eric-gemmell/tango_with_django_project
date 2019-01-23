import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "tango_with_django_project.settings")

import django
from django.utils import timezone
django.setup()
from polls.models import Choice, Question

def populate():
	dictionary = [
	{"question":"What's Up?",
	"choice":["Not Much","The Sky","I want to go to bed if I'm honest... Why do I leave things to the last minute?"]},
	{"question":"Are you Ready?",
        "choice":["For What?","No Not Really","I'm never ready... :'("]},
	{"question":"Favorite Beverage?",
        "choice":["Coke","Nestea","Is there really something better than Nestea?"]},
	]

	for question in dictionary:
		q = add_question(question["question"],timezone.now())
		for choice in question["choice"]:
			add_choice(choice, q)

	for q in Question.objects.all():
		for c in Choice.objects.filter(question = q):
			print("- {0} - {1}".format(str(q),str(c)))

def add_question(title, time):
	q = Question.objects.get_or_create(question_text = title)[0]
	q.pub_date = time
	q.save()
	return q

def add_choice(text,q): 
	c = Choice.objects.get_or_create(question=q,choice_text=text)[0]
	c.save()
	return c

if __name__ == "__main__":
	print("Starting Polls population script...")
	populate()

