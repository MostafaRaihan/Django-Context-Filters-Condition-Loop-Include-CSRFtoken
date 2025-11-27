from django.shortcuts import render
from datetime import datetime, timedelta


def home(request):

    nam1 = 10
    nam2 = 20
    nam3 = 30
    nam4 = 40
    total_sum = nam1 + nam2 + nam3 + nam4

    name = "Mostafa Raihan"
    age = 18
    city = "Feni"
    country = "Bangladesh"

    skills = ["Python", "Django", "React JS", "Next JS"]

    date= datetime.now()-timedelta()

    button = "<button>This Button</button>"

    isBangladeshi = None

    myclass = [
        {"name" : "Ratul"},
        {"name" : "Mazed"},
        {"name" : "Raihan"},
        {"name" : "Nazmul"},
        {"name" : "Reven"},
    ]

    context = {
        "nam1": nam1,
        "nam2": nam2,
        "nam3": nam3,
        "nam4": nam4,
        'sum': total_sum,

        "name": name,
        "age": age,
        "city": city,
        "country": country,

        "skills": skills,

        "datetime": date,

        "button": button,

        "isBangladeshi": isBangladeshi,

        "myclass": myclass,
    }

    return render(request, 'home.html', context)
