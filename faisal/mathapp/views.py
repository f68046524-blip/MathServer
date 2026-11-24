from django.shortcuts import render
def Churn_rate(request):
    In= float(request.POST.get('InitCust', '0'))
    Cl= float(request.POST.get('CustLost', '0'))
    churn_rate = ((In-Cl)*100)/In if request.method == 'POST' and In != 0 else 0
    print("Customers Lost Count =",Cl)
    print("Initial Customers Count =",In)
    print("Churn Rate =",churn_rate)
    return render(request, 'mathapp/math.html',{'In': In, 'Cl': Cl, 'churn_rate': churn_rate})