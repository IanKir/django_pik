from django.http import Http404
from django.shortcuts import render, redirect, get_object_or_404
from django.utils import timezone

from core.models import Building, Task


def get_stats(request):
    if request.method == 'GET':
        buildings = Building.objects.filter(
            establishment_date__lte=timezone.now()
        ).order_by('establishment_date')
        return render(
            request=request,
            template_name='mainpage/stats.html',
            context={'buildings': buildings}
        )
    else:
        return Http404('Not supported action 404')


def building_detail(request, pk):
    building = get_object_or_404(Building, id=pk)
    return render(
        request=request,
        template_name='mainpage/building_detail.html',
        context={'building': building}
    )


def building_edit(request, pk):
    building = get_object_or_404(Building, id=pk)
    if request.method == 'POST':
        building.title = request.POST.get('title')
        building.building_address = request.POST.get('building_address')
        building.establishment_date = timezone.now()
        building.save()
        return redirect(to='building_detail', pk=building.id)
    elif request.method == 'GET':
        return render(
            request=request,
            template_name='mainpage/building_detail.html',
            context={'building': building}
        )
    else:
        return Http404('Not supported action 404')


def building_new(request):
    if request.method == 'POST':
        building = Building.objects.create(
            title=request.POST.get('title'),
            building_address=request.POST.get('building_address'),
            establishment_date=timezone.now()
        )
        building.save()
        return redirect(to='building_detail', pk=building.id)
    return render(
        request=request,
        template_name='mainpage/builidng_edit.html'
    )


def add_bricks(request):
    if request.method == 'POST':
        task = Task.objects.create(
            building_number=request.POST.get('building_number'),
            bricks_quantity=request.POST.get('bricks_quantity')
        )
        task.save()
        return redirect(to='stats')
