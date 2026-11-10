from django.shortcuts import render
from .models import Employee
from django.db.models import Avg, Q
from datetime import date


def employee_overview(request):

    employees = Employee.objects.all()

    high_salary_employees = Employee.objects.filter(salary__gt=3000)

    count_high_salary = Employee.objects.filter(salary__gte=5000).count()

    average_sales_salary = Employee.objects.filter(
        department__name="Sales"
    ).aggregate(avg_salary=Avg("salary"))["avg_salary"]

    old_non_hr_employees = Employee.objects.filter(
        hire_date__lt=date(2022, 1, 1)
    ).exclude(
        department__name="HR"
    )

    context = {
        "employees": employees,
        "high_salary_employees": high_salary_employees,
        "count_high_salary": count_high_salary,
        "average_sales_salary": average_sales_salary,
        "old_non_hr_employees": old_non_hr_employees,
    }

    return render(request, "employee_list.html", context)