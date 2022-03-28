from django.shortcuts import render, get_object_or_404, redirect
from fusioncharts import FusionCharts
from guj.forms import *
from guj.models import *


def show(request):
    res = render(request, 'guj/projectfrontend.html')
    return res  # Create your views here.


def candidate_info_views(request):
    res = render(request, 'guj/home.html')
    return res


def detail(request, pk, model):
    candidate = get_object_or_404(model, pk=pk)
    return render(request, 'guj/detail.html', {'candidate': candidate})


def chart(request, model, year):
    dataSource = {}
    i = year
    dataSource['chart'] = {
        "caption": "Candidate Statistics for " + i,
        "xAxisName": "Candidate",
        "yAxisName": "Number of Votes",
        "theme": "zune"
    }
    dataSource['data'] = []

    for key in model.objects.all():
        data = {}
        data['label'] = key.Candidate
        data['value'] = key.Votes
        dataSource['data'].append(data)

    column2d = FusionCharts('column3d', 'ex1', '1225', '650', 'chart-1', 'json', dataSource)
    return render(request, 'guj/charts.html', {'output': column2d.render()})


'''def add_data(request):
	return render(request,'guj/form.html')

def added_data(request):
	candidate = request.POST["Candidate"]
	party = request.POST["Party"]
	votes = request.POST["Votes"]
	per_votes = request.POST["Per_Votes"]
	canadidate_data = Candidatedata(Candidate = candidate,Party = party,Votes = votes,Per_Votes = per_votes)
	canadidate_data.save()
	return render(request,'guj/form.html')'''


def add_data(request, cls):
    if request.method == "POST":
        form = cls(request.POST)
        if form.is_valid():
            form.save()
            return render(request, "guj/add_form.html")
    else:
        form = cls()
        return render(request, "guj/add_form.html", {form: 'form'})


def edit_data(request, model, pk, cls, header):
    item = get_object_or_404(model, pk=pk)
    if request.method == "POST":
        form = cls(request.POST, instance=item)
        if form.is_valid():
            form.save()
            if header.lower() == 'amreli candidates':
                return redirect('display_amreli')
            elif header.lower() == 'lathi candidates':
                return redirect('display_lathi')
            else:
                return redirect('display_dhari')
    else:
        form = cls(instance=item)
        return render(request, 'guj/form.html', {'form': form})


def delete_data(request, pk, model, header):
    model.objects.filter(id=pk).delete()
    if header.lower() == 'amreli candidates':
        return redirect('display_amreli')
    elif header.lower() == 'lathi candidates':
        return redirect('display_lathi')
    else:
        return redirect('display_dhari')


def display_model(request, cls, header):
    candidates = cls.objects.all()
    return render(request, 'guj/candidates.html', {'candidates': candidates, 'header': header})


def display_amreli(request):
    return display_model(request, Amreli, 'Amreli Candidates')


def display_lathi(request):
    return display_model(request, Lathi, 'Lathi Candidates')


def add_amreli(request):
    return add_data(request, AmreliForm)


def add_lathi(request):
    return add_data(request, LathiForm)


def edit_amreli(request, pk):
    return edit_data(request, Amreli, pk, AmreliForm, 'Amreli candidates')


def edit_lathi(request, pk):
    return edit_data(request, Lathi, pk, LathiForm, 'Lathi candidates')


def delete_amreli(request, pk):
    return delete_data(request, pk, Amreli, 'Amreli candidates')


def delete_lathi(request, pk):
    return delete_data(request, pk, Lathi, 'Lathi candidates')


def amreli_chart(request):
    return chart(request, Amreli, '2012')


def lathi_chart(request):
    return chart(request, Lathi, '2012')


def amreli_candidate_detail(request, pk):
    return detail(request, pk, Amreli)


def lathi_candidate_detail(request, pk):
    return detail(request, pk, Lathi)


def dhari_candidate_detail(request, pk):
    return detail(request, pk, Candidatedata)


def display_dhari(request):
    return display_model(request, Candidatedata, 'Dhari Candidates')


def add_dhari(request):
    return add_data(request, CandidateForm)


def edit_dhari(request, pk):
    return edit_data(request, Candidatedata, pk, CandidateForm, 'Dhari candidates')


def delete_dhari(request, pk):
    return delete_data(request, pk, Candidatedata, 'Dhari candidates')


def dhari_chart(request):
    return chart(request, Candidatedata, '2012')


def win_chart(request):
    dataSource = {}

    dataSource['chart'] = {
        "caption": 'Party Statistics for 2012',
        'xAxisName': 'Party Name',
        'yAxisName': 'Number of Seats Won',
        'theme': 'zune'
    }

    dataSource['data'] = []
    for par in Party.objects.all():
        data = {}
        data['label'] = par.Party
        data['value'] = par.Seats_Won
        dataSource['data'].append(data)

    pie = FusionCharts('pie3d', 'ex1', '1225', '650', 'chart-1', 'json', dataSource)
    return render(request, 'guj/pchart.html', {'output': pie.render()})


def party_chart(request):
    partys = Party.objects.all()
    return render(request, 'guj/party.html', {'party': partys, 'header': 'Winning Party Statistics 2012'})


def compare_info_views(request):
    return render(request, 'guj/home_compare.html')


def dhari_compare(request):
    return display_model(request, Dhari_compare, 'Dhari compare')


def dhari_compare_detail(request, pk):
    return detail(request, pk, Dhari_compare)


def amreli_compare(request):
    return display_model(request, Amreli_compare, 'Amreli compare')


def amreli_compare_detail(request):
    return detail(request, pk, Amreli_compare)


def lathi_compare(request):
    return display_model(request, Lathi_compare, 'Lathi compare')


def lathi_compare_detail(request):
    return detail(request, pk, Lathi_compare)


def amreli_chart(request):
    return chart(request, Amreli_compare, '2012-2017')


def dhari_chart(request):
    return chart(request, Dhari_compare, '2012-2017')


def lathi_chart(request):
    return chart(request, Lathi_compare, '2012-2017')
