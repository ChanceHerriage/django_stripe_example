from django.shortcuts import render


from .forms import PaymentForm

def payment(request):
	template_name = "payment/form.html"
	form = PaymentForm(request.POST or None)

	if request.method == "POST":
		if form.is_valid():
			print('the charge was successful')			
		else:
			print('not valid.')
			
	else:
		form = PaymentForm()

	context = {

		'form': form,
	}

	return render(request, template_name, context)
