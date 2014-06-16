from django.shortcuts import render, get_list_or_404
from django.http import HttpResponse
import pymorphy2

def api(request):
	inpunt_word = request.GET['s']
	case = request.GET['case']
	morph = pymorphy2.MorphAnalyzer()
	variations = morph.parse(inpunt_word)
	if len(variations) > 1:
		for item in variations:
			word = item
			if item.normal_form == inpunt_word:
				word = item
				break
	elif len(variations) == 1:
		word = variations[0]
	else:
		return HttpResponse(False)
	number = request.GET.get('number', word.tag.number)
	result = word.inflect({number, case})
	if result:
		return HttpResponse(result.word)
	else:
		return HttpResponse(False)

def home(request):
	return render(request, 'home.html')