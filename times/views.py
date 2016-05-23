from django.shortcuts import render
import datetime

# Create your views here.
def index(request):
    print( 'index' )
    current_time = datetime.datetime.now()
    date = current_time.strftime('%b %d, %Y')
    time = current_time.strftime('%I:%M %p')
    print(date,'--',time)
    context = {
        'title': 'the current time and date.',
        'current_time': {
            'date': date,
            'time': time
        }
    }
    return render(request, 'times/index.html', context)
