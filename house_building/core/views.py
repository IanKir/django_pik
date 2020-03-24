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
    building = get_object_or_404(Building, pk=pk)
    return render(
        request=request,
        template_name='mainpage/building_detail.html',
        context={'building': building}
    )


def building_edit(request, pk):
    building = get_object_or_404(Building, pk=pk)
    if request.method == 'POST':
        building.pk = building.pk
        building.title = request.POST.get('title')
        building.building_address = request.POST.get('building_address')
        building.establish()
        return redirect(to='building_detail', pk=building.pk)
    elif request.method == 'GET':
        return render(
            request=request,
            template_name='mainpage/building_edit.html',
            context={'building': building}
        )
    else:
        return Http404('Not supported action 404')


def building_new(request):
    if request.method == 'POST':
        building_pk = request.POST.get('building_pk')
        building_title = request.POST.get('title')
        building_address = request.POST.get('building_address')
        if building_pk:
            building = get_object_or_404(Building, pk=building_pk)
            building.title = building_title
            building.building_address = building_address
            building.establish()
        else:
            building = Building.objects.create(
                title=building_title,
                building_address=building_address
            )
            building.establish()
        return redirect(to='building_detail', pk=building.pk)
    return render(
        request=request,
        template_name='mainpage/building_edit.html'
    )


def add_bricks(request, pk):
    building_pk = pk
    if request.method == 'POST':
        building = get_object_or_404(Building, pk=building_pk)
        task = Task.objects.create(
            building_number=building,
            bricks_quantity=request.POST.get('bricks_quantity')
        )
        task.save()
        return redirect(to='get_stats')
    elif request.method == 'GET':
        return render(
            request=request,
            template_name='mainpage/building_add_bricks.html',
            context={'building_pk': building_pk}
        )
