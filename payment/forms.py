from django import forms

import stripe

stripe.api_key = "sk_test_DdGFBfLWJjV7b1qL3Z9Vo8s600X4NJWrzF"

class PaymentForm(forms.Form):
	def is_valid(self):
		valid = super(PaymentForm, self).is_valid()

		if not valid:
			return valid

		if not (self.cleaned_data['amount'] and \
			self.cleaned_data['number'] and \
			self.cleaned_data['month'] and \
			self.cleaned_data['year'] and \
			self.cleaned_data['cvc']):
			print('didnt have all my shit')
			return False

		print(self.cleaned_data['amount'],
			self.cleaned_data['number'],
			self.cleaned_data['month'],
			self.cleaned_data['year'],
			self.cleaned_data['cvc'],)

		try:
			# Use Stripe's library to make requests...
		   
			card_token = None

			try:
				card_token = stripe.Token.create(
				  card={
				    'number': self.cleaned_data['number'],
				    'exp_month': self.cleaned_data['month'],
				    'exp_year': self.cleaned_data['year'],
				    'cvc': self.cleaned_data['cvc'],
				  },
				)
			except Exception as e:
				print('ERROR: Could not create token')
				pass
		  
			if card_token is not None:
				stripe.Charge.create(
					amount=str(self.cleaned_data['amount']).replace('.',''),
					currency="usd",
					source=card_token, # obtained with Stripe.js
					description="Test lacasabonita charge."
				)

				return True

			print('ERROR: card_token is None')
			return False
		  	
		except stripe.error.CardError as e:
			# Since it's a decline, stripe.error.CardError will be caught
			body = e.json_body
			err  = body.get('error', {})

			print("Status is: %s" % e.http_status)
			print("Type is: %s" % err.get('type'))
			print("Code is: %s" % err.get('code'))
			print("Param is: %s" % err.get('param'))
			print("Message is: %s" % err.get('message'))
		except stripe.error.RateLimitError as e:
		  # Too many requests made to the API too quickly
			print('RateLimitError')
		except stripe.error.InvalidRequestError as e:
		  # Invalid parameters were supplied to Stripe's API
	  		print('InvalidRequestError')
		except stripe.error.AuthenticationError as e:
		  # Authentication with Stripe's API failed
		  # (maybe you changed API keys recently)
		  	print('AuthenticationError')
		except stripe.error.APIConnectionError as e:
		  # Network communication with Stripe failed
		  	print('APIConnectionError')
		except stripe.error.StripeError as e:
		  # Display a very generic error to the user, and maybe send
		  # yourself an email
		  	print('StripeError')
		except Exception as e:
		  # Something else happened, completely unrelated to Stripe
		  	print('Exception')

		return False

	amount = forms.DecimalField(max_digits=8, decimal_places=2)
	number = forms.CharField(required=False, max_length=16)
	month = forms.CharField(min_length=2, max_length=2)
	year = forms.CharField(min_length=4, max_length=4)
	cvc = forms.CharField(max_length=4)

	class Meta:
		fields = ('number', 'month', 'year', 'cvc')