from django.shortcuts import render, HttpResponse
from django.http import JsonResponse
import random
import requests
import json
from .models import Countries

# Create your views here.


def prepare_data(request):
    try:
        country_data = requests.get('https://countriesnow.space/api/v0.1/countries/capital')
        response_data = json.loads(country_data.content)
        print("DATA======>", response_data['data'])
        for each_item in response_data['data']:
            country_name = each_item['name']
            capital_city = each_item['capital']
            get_data_by_name = Countries.objects.filter(name=country_name)
            print("EXISTING_DATA=====>", get_data_by_name)
            if not get_data_by_name:
                country_obj = Countries(
                    name=country_name,
                    capital=capital_city
                )
                country_obj.save()
    except Exception as e:
        return HttpResponse(e.__str__())
    return HttpResponse("Data Prepared")


def load_queeze(request):
    rand_int = random.randint(0, 251)
    country_data = Countries.objects.all()
    context = {'country_data': country_data,'rand_int': rand_int}
    return render(request, 'my_queeze/load_queeze.html', context)


def validate_answer(request):
    selected_country_id = request.GET['selected_country']
    entered_value = request.GET['entered_value']
    response_data = dict()
    try:
        get_row_by_id = Countries.objects.get(id=selected_country_id)
        if get_row_by_id.capital == entered_value:
            response_data['status'] = 'TRUE'
        else:
            response_data['status'] = 'FALSE'
            response_data['capital_city'] = get_row_by_id.capital
    except Exception as e:
        response_data['status'] = None
        response_data['message'] = e.__str__()
    print(selected_country_id, " || ", entered_value)
    print(response_data)
    return JsonResponse(response_data)
