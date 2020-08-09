from django.shortcuts import render
from django.contrib import messages
from .forms import PersonCreateForm

def home_page(request):

    if request.method == 'POST':
        person_form = PersonCreateForm(request.POST or None)

        if person_form.is_valid():
            new_person = person_form.save()
            messages.success(request, f'Sign up Succesful!')

        else:
            messages.warning(request, f'Sign up Failed, try again')

    else:
        person_form = PersonCreateForm()

    return render(request, 'home/home.html', {'form':person_form})

def media_page(request):
    return render(request, 'home/media_page.html')

def about_page(request):
    return render(request, 'home/about.html')

def our_story(request):
    return render(request, 'home/our_story.html')

def events(request):
    return render(request, 'home/events.html')


def missions_page(request):
    return render(request, 'home/missions.html')

def tailoring_center(request):
    return render(request, 'missions/tailoring_center.html')

def discipleship_centre(request):
    return render(request, 'missions/discipleship_centre.html')

def tuition_center(request):
    return render(request, 'missions/tutition_center.html')



def ministries_page(request):
    return render(request, 'home/ministries_page.html')

def vbs(request):
    return render(request, 'ministries/vbs.html')

def literature_ministry(request):
    return render(request, 'ministries/literature_ministry.html')

def sunday_school(request):
    return render(request, 'ministries/sunday_school.html')

def youth(request):
    return render(request, 'ministries/youth.html')

def evangalism(request):
    return render(request, 'ministries/evangalism.html')

def family_seminar(request):
    return render(request, 'ministries/family_seminar.html')

def relief_work(request):
    return render(request, 'ministries/relief_work.html')

def seekers_meeting(request):
    return render(request, 'ministries/seekers_meeting.html')

def christmas(request):
    return render(request, 'ministries/christmas.html')
