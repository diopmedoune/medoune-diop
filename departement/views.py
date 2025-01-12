from django.shortcuts import render
from .models import ProfesseurModel, DepartementModel
from .form import DepartementForm, ProfessorForm



def home(request):
    return render(request, 'home.html')

# Methode 1 (100% HTML Form)
def create_departement(request):
    if request.method == 'POST':
        form = DepartementForm(request.POST)
        if form.is_valid():
            form.save()
        
            return render(request, 'departement/success_save_dept.html')

    return render(request, 'departement/html_form.html')


# Methode 2 (Django + HTML form)
def add_departement(request):
    form = DepartementForm()
    if request.method == 'POST':
        form = DepartementForm(request.POST)
        if form.is_valid():
            form.save()

            return render(request, 'departement/success_save_dept.html')
        
    context = {"form": form}
    return render(request, "departement/django_html_form.html", context=context)

# Add new professor view
def add_professor(request):
    form = ProfessorForm
    if request.method == 'POST':
        form = ProfessorForm(request.POST)
        if form.is_valid():
            form.save()
    
            return render(request, 'departement/success_save_profs.html')

    context = {'form': form}

    return render(request, 'departement/add_professor.html', context=context)

# View ised to show all profs
def show_all_prof(request):
    profs = ProfesseurModel.objects.prefetch_related('chef_departement').all()
    context = {'profs': profs}

    return render(request, 'departement/show_all_prof.html', context=context)

# View ised to show all departments
def show_all_depts(request):
    depts = DepartementModel.objects.all()
    context = {'depts': depts}

    return render(request, 'departement/show_all_depts.html', context=context)
