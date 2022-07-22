from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect
from django.urls import reverse
from . import zodiac_info


def index(request):
    li_elements = ''
    for i in zodiac_info.zodiac_dict.keys():
        redirect_path = reverse("horoscope-name", args=[i])
        li_elements += f"<h3><a href='{redirect_path}'>{i.title()}({zodiac_info.dict_ru[i].title()})</a></h3>"
    li_elements += f"<br><button><h3><a href='types'>Стихии</a></h3></button>"
    response = f"""
    <ul>
    {li_elements}
    </ul>
    """
    return HttpResponse(f"<head><title>Гороскоп</title></head><h2>Знаки задиака</h2>{response}")


def types(request):
    li_types = ''
    for i in zodiac_info.types_list:
        redirect_types = reverse("type-name", args=[i])
        li_types += f"<h3><a href='{redirect_types}'>{i.title()}({zodiac_info.dict_ru[i].title()})</a></h3>"
    li_types += f"""<img
                src="https://img1.hochu.ua/uploads/98/15/05/98150588-caf0-40b9-8254-057343478be9_360x300_fit.jpg"
                title="4 Стихии"
                alt="Стихии"
                width="400"
                height="300"><br><br> <br>
                <button><h3><a href='/horoscope/'>Знаки зодиака</a></h3></button>"""
    response = f"""
    <ul>
    {li_types}
    </ul>
    """
    return HttpResponse(f"<head><title>Стихии</title></head><h2>Стихии</h2>{response}")


def get_info_about_types(request, sign_type):
    if sign_type not in zodiac_info.types_list:
        return HttpResponseNotFound(f"<head><title>Ошибка</title></head>Неизвестная стихия - {sign_type}!")
    else:
        li_elements = ''
        count = 0
        counter = zodiac_info.types_list.index(sign_type)
        for i in zodiac_info.zodiac_dict.keys():
            if count % 4 == counter:
                redirect_path = reverse("horoscope-name", args=[i])
                li_elements += f"<h3><a href='{redirect_path}'>{i.title()}({zodiac_info.dict_ru[i].title()})</a></h3>"
            count += 1
        li_elements += f"""<img
                src={zodiac_info.types_img_list[counter]}
                title="Стихия"
                alt="Стихия"
                width="400"
                height="300">
                <br><br><br><button><h3><a href='/horoscope/types'>Стихии</a></h3></button>"""
        li_elements += f"<br><button><h3><a href='/horoscope/'>Знаки зодиака</a></h3></button>"
        response = f"""
        <ul>
        {li_elements}
        </ul>
        """
        return HttpResponse(
            f"""<head><title>{zodiac_info.dict_ru[sign_type].title()}</title></head>
            <h2>Знаки задиака стихии {zodiac_info.dict_ru[sign_type].title()}</h2>{response}""")


def get_info_about_sign_zodiac(request, sign_zodiac):
    description = zodiac_info.zodiac_dict.get(sign_zodiac, None)
    if description:
        return HttpResponse(f"""
        {description}<head><title>{zodiac_info.dict_ru[sign_zodiac].title()}</title></head>
        <ul><br><br><button><h3><a href='/horoscope/types' target='_blank'>Стихии</a></h3></button>
        <br><button><h3><a href='/horoscope/' target='_blank'>Знаки зодиака</a></h3></ul></button>
        """)
    else:
        return HttpResponseNotFound(f"<head><title>Ошибка</title></head>Неизвестный знак задиака - {sign_zodiac}!")


def get_info_about_sign_zodiac_number(request, sign_zodiac: int):
    zodiacs = list(zodiac_info.zodiac_dict)
    if sign_zodiac > len(zodiacs):
        return HttpResponseNotFound(
            f"<head><title>Ошибка</title></head>Неправильный порядковый номер знака задиака - {sign_zodiac}!")
    name_zodiac = zodiacs[sign_zodiac - 1]
    redirect_url = reverse("horoscope-name", args=(name_zodiac,))
    return HttpResponseRedirect(redirect_url)
