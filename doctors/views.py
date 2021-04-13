from bs4 import BeautifulSoup
from urllib.request import urlopen
from .forms import inpform
from django.shortcuts import render



def display(request):
    if request.method== 'POST':
        input=inpform(request.POST)
        if input.is_valid():
            cd=input.cleaned_data

        
            url='https://www.practo.com/search?results_type=doctor&q=%5B%7B%22word%22%3A%22'+cd['specialization']+'%22%2C%22autocompleted%22%3Atrue%2C%22category%22%3A%22subspeciality%22%7D%5D&city='+cd['city']

            client=urlopen(url)
            page_html=client.read()
            soup=BeautifulSoup(page_html,'html.parser')

            client.close()

            liz=soup.find_all('div',{"class":"listing-doctor-card"})
            d={}
            for i in range(len(liz)):
                name=liz[i].find('h2',{"class":"doctor-name"}).getText()
                address=liz[i].find('span',{"data-qa-id":"practice_locality"}).getText()
                address+=" "+ cd['city']
                print(name, end=' , ')
                print(address)
                d[i]={'name':name ,'address': address}
            print(d)
            k={'a': d}
            print(k)
            length=len(k['a'])
            if length>0:
                return render( request, 'display.html',k)
            else:
                return render( request, 'display2.html')

    else:
        input=inpform()
    return render(request,'form.html' ,{'form' : input})
            

