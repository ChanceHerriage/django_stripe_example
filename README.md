# django_stripe_example

This project is to show how easy it is to get stripe running with a simple payment form. This is often the base of what is needed to start building a project that processes payments so this is a great place to start.

For this you will want to follow along [here](https://stripe.com/docs/api).

### Usage

Assuming you already have created a virtual environment and are working inside it...

	pip install -r requirements.txt
	./manage.py migrate
	./manage.py runserver
	

### Beyond this

Understanding the basics is key here, but once you do understand them; There are a few things you could/should do.

- You should clean up the card validation a little bit.
- You could turn the expiration month and year into a single field with validation
- You could check the length of the ccv based on the card type because debit cards have 3 char ccv while credit cards often have 4
- You could do live authentication of card information with AJAX
- You could display the errors after POST submits below the inputs
- You could offer preset prices
- You could tie the token to an account and automatically fill the payment information


### It's ready for you

The possibilities are endless, but now you have the base form and you can run with it.
