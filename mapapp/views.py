from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import render
from .models import Marker
from .forms import MarkerForm
from django.utils.dateparse import parse_date

def map_view(request):
    selected_date = request.GET.get('date')
    
    if selected_date:
        selected_date = parse_date(selected_date)
        markers = (Marker.objects.filter(is_permanent=True) | 
                   Marker.objects.filter(start_date__lte=selected_date, end_date__gte=selected_date))
    else:
        markers = Marker.objects.all()

    # Определение типа устройства
    user_agent = request.META.get('HTTP_USER_AGENT', '')
    if 'Mobile' in user_agent or 'Android' in user_agent or 'iPhone' in user_agent:
        template_name = 'mapapp/mobile.html'
    else:
        template_name = 'mapapp/desktop.html'

    return render(request, template_name, {'markers': markers, 'selected_date': selected_date})

@csrf_exempt
def add_marker(request):
    if request.method == 'POST' and request.META.get('HTTP_X_REQUESTED_WITH') == 'XMLHttpRequest':
        form = MarkerForm(request.POST, request.FILES)

        if form.is_valid():
            marker = form.save()

            return JsonResponse({
                'success': True,
                'id': marker.id,
                'title': marker.title,
                'description': marker.description,
                'latitude': marker.latitude,
                'longitude': marker.longitude,
                'event_type': marker.event_type if marker.event_type else '',
                'image': marker.image.url if marker.image else '',
                'video': marker.video.url if marker.video else '',
                'start_date': marker.start_date.isoformat() if marker.start_date else '',
                'end_date': marker.end_date.isoformat() if marker.end_date else '',
                'is_permanent': marker.is_permanent
            })
        else:
            return JsonResponse({'success': False, 'errors': form.errors})
    
    return JsonResponse({'success': False})

def get_markers(request):
    start_date = request.GET.get('start_date')
    end_date = request.GET.get('end_date')
    query = request.GET.get('query', '')

    markers = Marker.objects.all()

    if start_date:
        start_date = parse_date(start_date)
        markers = markers.filter(start_date__gte=start_date)
    if end_date:
        end_date = parse_date(end_date)
        markers = markers.filter(end_date__lte=end_date)
    
    if query:
        if query.startswith('ID:'):
            try:
                marker_id = int(query.split('ID:')[1].strip())
                markers = markers.filter(id=marker_id)
            except ValueError:
                markers = markers.none()
        else:
            markers = markers.filter(title__icontains=query) | markers.filter(description__icontains=query)
    
    markers = markers.values('id', 'title', 'description', 'latitude', 'longitude', 'image', 'video', 'event_type', 'start_date', 'end_date', 'is_permanent')
    markers_list = list(markers)
    return JsonResponse(markers_list, safe=False)
