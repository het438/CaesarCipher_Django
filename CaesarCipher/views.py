from django.shortcuts import render
from django.http import HttpResponse


def home(request):
    return render(request, 'index.html')


def caesar(request):
    if request.POST.get("ebutton"):
        plain_text = request.POST["plain"]
        plain_text = plain_text.replace(" ", "")
        key = int(request.POST["key"])
        cipher_text = ""

        for i in range(len(plain_text)):
            letter = plain_text[i]
            if letter.isupper():
                cipher_text += chr((ord(letter) + key - 65) % 26 + 65)
            else:
                cipher_text += chr((ord(letter) + key - 97) % 26 + 97)
        return render(request, 'index.html', {"result1": cipher_text})
    if request.POST.get("dbutton"):
        cipher_text = request.POST["decrypt"]
        cipher_text = cipher_text.replace(" ","")
        key1 = int(request.POST["key"])
        plain_text = ""
        for i in range(len(cipher_text)):
            letter = cipher_text[i]
            if letter.isupper():
                plain_text += chr((ord(letter) - key1 - 65) % 26 + 65)
            else:
                plain_text += chr((ord(letter) - key1 - 97) % 26 + 97)
        return render(request, 'index.html', {"result": plain_text})
