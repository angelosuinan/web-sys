from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.contrib.auth.decorators import login_required, permission_required
from django.utils.decorators import method_decorator
from django.core.exceptions import ObjectDoesNotExist
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.views.generic import View
from models import Item


class Index(View):
    template_name = 'inventory/index.html'

    @method_decorator(login_required(login_url='/login'), )
    def get(self, request):
        user = request.user
        item_list = Item.objects.filter(employee=user)
        paginator = Paginator(item_list, 20)

        page = request.GET.get('page')
        if page is None:
            return redirect('/inventory?page=1')

        try:
            items = paginator.page(page)
        except PageNotAnInteger:
            # If page is not an integer, deliver first page.
            items = paginator.page(1)
        except EmptyPage:
            # If page is out of range (e.g. 9999), deliver last page of results.
            items = paginator.page(paginator.num_pages)

        context = {'items': items}
        return render(request, self.template_name, context)


class Add(View):
    template_name = 'inventory/add.html'

    def get(self, request,):
        context = {}
        context['employees'] = self.get_employees(request)
        return render(request, self.template_name, context)

    def post(self, request,):
        context = {}
        context['employees'] = self.get_employees(request)
        name = request.POST.get('name', '')
        description = request.POST.get('description', '')
        unit = request.POST.get('unit', '')
        quantity = request.POST.get('quantity', '')
        date_acquired = request.POST.get('date_acquired', '')
        amount = request.POST.get('amount', '')
        issued_by = request.POST.get('issued_by', '')
        received_by = request.POST.get('received_by', '')
        remarks = request.POST.get('remarks', '')
        photo = ''
        for filename, file in request.FILES.iteritems():
            photo = request.FILES[filename]
        received_by = User.objects.get(username=received_by)
        issued_by = User.objects.get(username=issued_by)
        item = Item(
            employee=request.user, name=name, description=description,
            unit=unit, quantity=quantity,
            date_acquired=date_acquired, amount=amount, issued_by=issued_by,
            received_by=received_by, remarks=remarks, photo=photo)
        item.save()
        return redirect('/inventory?change='+str(item.pk))

    def get_employees(self, request ):
        user = request.user
        employees = User.objects.all()

        return employees


class Change(View):
    template_name = 'inventory/change.html'

    def process(self, request):
        key = request.GET.get('id')
        try:
            item = Item.objects.get(pk=key)
        except ObjectDoesNotExist:
            return redirect('/error')

        if item.employee != request.user:
            return redirect('/error')
        context = {}
        context['item'] = item
        context['date_acquired'] = str(item.date_acquired)
        context['employees'] = self.get_employees(request)
        return context

    def get(self, request):
        context = self.process(request)
        return render(request, self.template_name, context)

    def post(self, request):
        key = request.GET.get('id')
        remarks = request.POST.get('remarks', '')
        photo = ''
        for filename, file in request.FILES.iteritems():
            photo = request.FILES[filename]

        item = Item.objects.get(pk=key)
        item.remarks = remarks
        if photo:
            item.photo = photo
        item.save()
        context = self.process(request)
        return render(request, self.template_name, context)

    def get_employees(self, request):
        user = request.user
        employees = User.objects.all()

        return employees
