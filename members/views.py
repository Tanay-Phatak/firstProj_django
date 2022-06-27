'''from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

def index(request):
    template = loader.get_template('first.html')
    return HttpResponse(template.render())
'''
'''
from django.http import HttpResponse
from django.template import loader
from .models import Members

def index(request):
  mymembers = Members.objects.all().values()
  output = ""
  for x in mymembers:
    output += x["firstname"]
  return HttpResponse(output)
'''




from asyncio.windows_events import NULL
from datetime import datetime, timedelta
from urllib import request
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from django.shortcuts import render
from django.template import loader
from django.urls import reverse
from .models import Members, Person
import json
from .tables import PersonTable
from django_tables2 import SingleTableView


def index(request):
    mymembers = Members.objects.all()
    template = loader.get_template('index.html')
    context = {
        'mymembers': mymembers,
    }
    return HttpResponse(template.render(context, request))
    # return render(request, "template name",{'key':mymembers})


def add(request):
    template = loader.get_template('add.html')
    return HttpResponse(template.render({}, request))


def addrecord(request):
    x = request.POST['first']
    y = request.POST['last']
    member = Members(firstname=x, lastname=y)
    member.save()
    return HttpResponseRedirect(reverse('index'))


def delete(request, id):
    member = Members.objects.get(id=id)
    member.delete()
    return HttpResponseRedirect(reverse('index'))


def update(request, id):
    id = request.POST['id']
    mymember = Members.objects.get(id=id)
    template = loader.get_template('update.html')
    context = {
        'mymember': mymember,
    }
    return HttpResponse(template.render(context, request))


def updaterecord(request):
    first = request.POST['fname']
    last = request.POST['lname']
    hobbies = request.POST['hobbies']
    dob = request.POST['dob']
    member = Members.objects.filter(id=id)
    member.firstname = first
    member.lastname = last
    member.hobbies = hobbies
    member.dob = dob
    member.save()
    return AllData(request)


def testing(request):
    mydata = Members.objects.all()
    template = loader.get_template('template.html')
    context = {
        'mymembers': mydata,
    }
    return render(request, 'template.html', {'mymembers':mydata})
    # return HttpResponse(template.render(context, request))


def abc():
    fnames = ['Karan', 'Rahul', 'Shyam', 'Rohan', 'Jayesh', 'Utsav', 'Pranav', 'Sachet', 'Aadya', 'Kaamoad']
    lnames = ['AAAA', 'BBBB', 'CCCC', 'DDDD', 'EEEE', 'FFFF', 'GGGG', 'HHHH', 'IIII', 'JJJJ']
    hob = ['football', 'badminton', 'cricket', 'swimming', 'cooking', 'drawing', 'painting', 'cycling', 'squash', 'hiking']

    i = 0 
    j = 0
    for x in range(100):
        print(x)
        Person.objects.create(firstname = fnames[i] + lnames[j], 
                                lastname = fnames[i] + '_' + lnames[j], 
                                hobbies = hob[i] + "_" + hob[j],
                                dob = datetime.now().date() - timedelta(days=x))
        j += 1
        if i == len(fnames):
            i = 0
           
        if j == len(lnames): 
            j = 0
            i += 1

def disp(request):
    #abc()
    data = Person.objects.all()
    return render(request, 'display.html', {"data": data})
    

def search(request):
    try:
        if request.method == "POST":
            w = request.POST['fname']
            # x = request.POST['lname']
            # y = request.POST['hobbies']
            # z_start = request.POST['dob_start']
            # z_end = request.POST['dob_end']
            person = Person.objects

            if w != "":
                person = Person.objects.filter(firstname__contains=w)
            # if x != "":
            #     person = person.filter(lastname__contains=x)
            # if y != "":
            #     person = person.filter(hobbies__contains=y)
            # if z_start != "":
            #     person = person.filter(dob__gte=z_start)
            # if z_end != "":
            #     person = person.filter(dob__lte=z_end)

            # if (w == x == y == z_start == z_end == "") :
            #     person = person.all()

            if (w == "") :
                person = person.all()

            get_all_data = [[each.id, each.firstname, each.lastname, each.hobbies, each.dob] for each in person]
            return JsonResponse({'data': get_all_data}, safe=False)
            
    except Exception as ep:
        return JsonResponse({'data': ep})


def search_result(request) :
    person = request.POST.get("str")
    print(person)
    return JsonResponse({'data': person})


def AllData(request):
    data = Person.objects.values()
    get_all_data = [[each['id'], each['firstname'], each['lastname'], each['hobbies'], each['dob']] for each in data]
    # above stmt used to serialize querySet as JsonResponse cannot handle complex python objects, so 
    #      querySet is not serializable...........
    return JsonResponse({'data': get_all_data}, safe=False)


def delete(request):
    rowId = request.POST.get('delRow')
    Person.objects.filter(id=rowId).delete()
    return AllData(request)


def update(request):
    rowId = request.POST['id']
    print("-----------", request.POST['fname'])
    person = Person.objects.get(id=rowId)
    person.firstname = request.POST['fname']
    person.lastname = request.POST['lname']
    person.hobbies = request.POST['hobbies']
    person.save()
    return AllData(request)




