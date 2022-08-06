from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect
from django.urls import reverse
from . import zodiac_info

from django.template.loader import render_to_string


def index(request):
    zodiacs = list(zodiac_info.zodiac_dict)
    context = {
        'zodiacs': zodiacs,
        }
    return render(request, 'horoscope/index.html', context=context)


def types(request):
    types = zodiac_info.types_list
    zodiacs = list(zodiac_info.zodiac_dict)
    context = {
        'types': types,
        'zodiacs': zodiacs,
        }
    return render(request, 'horoscope/types.html', context=context)

def get_info_about_types(request, sign_type):
    zodiacs = list(zodiac_info.zodiac_dict)
    types = zodiac_info.types_list
    description_title = zodiac_info.dict_ru.get(sign_type, None)
    description_img = zodiac_info.zodiac_img_dict.get(sign_type, None)
    sign_type = list(zodiac_info.types_dict.get(sign_type, None))
    data = {
        'description_title': description_title,
        'description_img': description_img,
        'zodiacs': zodiacs,
        'types': types,
        'sign_type': sign_type
    }
    return render(request, 'horoscope/info_types.html', context=data)


    #li_elements = ''
    #count = 0
    #counter = zodiac_info.types_list.index(sign_type)
    #for i in zodiac_info.zodiac_dict.keys():
     #   if count % 4 == counter:
      #      redirect_path = reverse("horoscope-name", args=[i])
       #     li_elements += f"<h3><a href='{redirect_path}'>{i.title()}({zodiac_info.dict_ru[i].title()})</a></h3>"
       # count += 1
    #li_elements += f"""<img
     #       src={zodiac_info.types_img_list[counter]}
      #      title="Стихия"
       #     alt="Стихия"
        #    width="400"
         #   height="300">
          #  <br><br><br><button><h3><a href='/horoscope/types'>Стихии</a></h3></button>"""
    #li_elements += f"<br><button><h3><a href='/horoscope/'>Знаки зодиака</a></h3></button>"
    #response = f"""
    #<ul>
    #{li_elements}
    #</ul>
    #"""
    #return HttpResponse(
    #    f"""<head><title>{zodiac_info.dict_ru[sign_type].title()}</title></head>
    #    <h2>Знаки задиака стихии {zodiac_info.dict_ru[sign_type].title()}</h2>{response}""")


def get_info_about_sign_zodiac(request, sign_zodiac):
    zodiacs = list(zodiac_info.zodiac_dict)
    description = zodiac_info.zodiac_dict.get(sign_zodiac, None)
    description_title = zodiac_info.dict_ru.get(sign_zodiac, None)
    description_img = zodiac_info.zodiac_img_dict.get(sign_zodiac, None)
    data = {
        'description_zodiac': description,
        'description_title': description_title.title(),
        'description_img': description_img,
        'zodiacs': zodiacs
    }
    if description:
        return render(request, 'horoscope/info_zodiac.html', context=data)
    else:
        return render(request, 'horoscope/info_error.html')


def get_info_about_sign_zodiac_number(request, sign_zodiac: int):
    zodiacs = list(zodiac_info.zodiac_dict)
    if sign_zodiac > len(zodiacs):
        return HttpResponseNotFound(
            f"<head><title>Ошибка</title></head>Неправильный порядковый номер знака задиака - {sign_zodiac}!")
    name_zodiac = zodiacs[sign_zodiac - 1]
    redirect_url = reverse("horoscope-name", args=(name_zodiac,))
    return HttpResponseRedirect(redirect_url)
