from django.shortcuts import render
from django.contrib.auth.decorators import login_required, permission_required
# Create your views here.

@login_required()
def bmap_index(request):
    return render(request, 'bmap/index.html')


@login_required()
def bmap_data_map(request):
    return render(request, 'bmap/data_map.html')