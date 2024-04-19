from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from openpyxl import load_workbook
from .functions.generateExcel import FillWorkBook
from .models import Parameter

# Create your views here.
def index(request):
    return render(request, "index.html")


def parameter_list(request):
    parameters = Parameter.objects.all()  # Fetch all data from the database
    return render(request, 'parameter_list.html', {'parameters': parameters})


def report(request):
    # Your Python function logic here
    FillWorkBook()
    print('Report function triggered')
    return JsonResponse({'message': 'Report function triggered'})

