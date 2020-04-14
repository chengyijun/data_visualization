from django.conf.urls import url
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render, reverse, redirect
import json
import re
import numpy as np
import redis
import pandas as pd


# Create your views here.

def revtest(request):
    # return redirect(reverse('myapp:test3', kwargs={'a': 'abel', 'b': 999}))
    return redirect(reverse('myapp:test2', args=('abel', 889)))


def showtest(request):
    return render(request, 'showtest.html')


def test5(request, a, b):
    # a = request.GET.get('a', '')
    # b = request.GET.get('b', '')
    res = 'a={}, b={}'.format(a, b)
    return HttpResponse(res)


def test4(request, a, b):
    # a = request.GET.get('a', '')
    # b = request.GET.get('b', '')
    res = 'a={}, b={}'.format(a, b)
    return HttpResponse(res)


def test3(request, a, b):
    # a = request.GET.get('a', '')
    # b = request.GET.get('b', '')
    res = 'a={}, b={}'.format(a, b)
    return HttpResponse(res)


def test2(request, a, b):
    # a = request.GET.get('a', '')
    # b = request.GET.get('b', '')
    res = 'a={}, b={}'.format(a, b)
    return HttpResponse(res)


def test1(request):
    a = request.GET.get('a', '')
    b = request.GET.get('b', '')
    res = 'a={}, b={}'.format(a, b)
    return HttpResponse(res)


def index(request):
    return render(request, 'index.html')


def calc(request):
    ds = make_data()
    # print(ds)
    # data = {
    #     'city': ['a', 'b'],
    #     'price': [30000.0005, 50000.1235]
    # }
    data = {
        'city': ds[0],
        'price': ds[1]
    }
    # print(data)
    return JsonResponse(data=data)
    # return HttpResponse(json.dumps(data, ensure_ascii=False), content_type="application/json,charset=utf-8")


def make_data():
    pool = redis.ConnectionPool(host='localhost', port=6379, db=0)
    red = redis.Redis(connection_pool=pool)

    items = red.lrange("sf:items", 0, -1)

    items = list(map(lambda x: json.loads(x), items))

    df = pd.DataFrame(items)
    ps = []
    for price in df['price']:
        res = re.search(r'.*?(\d+).*?', price)
        if not res:
            p = np.nan
        else:
            p = res.group(1)
            if int(p) > 60000:
                p = np.nan
        ps.append(p)
    df['price_without_unit'] = ps
    df['price_without_unit'] = df['price_without_unit'].astype('float')

    # 按城市分组
    city_groups = df['price_without_unit'].groupby(by=[df['province'], df['city']]).mean()
    # print(city_groups)

    _x = city_groups.index
    _y = city_groups.values

    return [list(map(lambda x: x[0] + ' - ' + x[1], _x))[::6], list(_y)[::6]]
