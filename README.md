# Ex.03 Design a Website for Server Side Processing
## Date:17-11-2026

## AIM:
To create a web page to calculate Churn Rate using server-side scripts.

## FORMULA:
Churn Rate = (CustLost / InitCust) * 100
<br> InitCust --> Initial Customers Count
<br> CustLost --> Customers Lost Count

## DESIGN STEPS:

### Step 1:
Clone the repository from GitHub.

### Step 2:
Create Django Admin project.

### Step 3:
Create a New App under the Django Admin project.

### Step 4:
Create a HTML file to implement form based input and output.

### Step 5:
Create python programs for views and urls to perform server side processing.

### Step 6:
Receive input values from the form using request.POST.get().

### Step 7:
Calculate the Result using the given formula.

### Step 8:
Display the calculated result in the server console.

### Step 9:
Render the result to the HTML template.

### Step 10:
Publish the website in Localhost.

## PROGRAM:
```<head>
        <title>FWAD experiment 3</title>
    </head>
    <body>
        <h1 align="center">churn rate calculator</h1><br>
        <h2 align="center">FAISAL S ( 26018146 )</h2>
        <form method="post">
            {% csrf_token %}
            <label>Initial Customers Count:</label>
            <input type="text" name="InitCust" value="{{In}}"><br><br>
            
            <label>Customers Lost Count:</label>
            <input type="text" name="CustLost" value="{{Cl}}"><br><br>
            
            <input type="submit" value="calculate"><br><br>
            <lable><b>Churn Rate:</b></lable>
            <input type="text" value="{{churn_rate}}">
            
        </form>
    </body>
</html>

views.py

from django.shortcuts import render
def Churn_rate(request):
    In= float(request.POST.get('InitCust', '0'))
    Cl= float(request.POST.get('CustLost', '0'))
    churn_rate = ((In-Cl)*100)/In if request.method == 'POST' and In != 0 else 0
    print("Customers Lost Count =",Cl)
    print("Initial Customers Count =",In)
    print("Churn Rate =",churn_rate)
    return render(request, 'mathapp/math.html',{'In': In, 'Cl': Cl, 'churn_rate': churn_rate})


urls.py

from django.contrib import admin
from django.urls import path
from mathapp import views

urlpatterns = [path('', views.Churn_rate, name='Churn_rate'),]

```


## OUTPUT - SERVER SIDE:
![alt text](<Screenshot (10).png>)

## OUTPUT - WEBPAGE:
![alt text](<Screenshot (9).png>)

## RESULT:
The the web page to calculate Churn Rate using server-side scripts is created successfully.
