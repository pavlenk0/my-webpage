from django.shortcuts import render

def project(request):
	return render(request, 'webpage/project.html')

def pclass(request):
	return render(request, 'webpage/pclass.html')

def sex(request):
	return render(request, 'webpage/sex.html')

def tfare(request):
	return render(request, 'webpage/tfare.html')