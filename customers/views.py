# from django.shortcuts import render, redirect, get_object_or_404
# from django.contrib import messages
# from .models import Customer, PersonalLoan, BusinessLoan


# # ===================== CUSTOMER LIST =====================

# def customer_list(request):

#     customers = Customer.objects.all().order_by('-id')

#     return render(request, 'customers/customer_list.html', {
#         'customers': customers
#     })


# # ===================== ADD CUSTOMER =====================

# def add_customer(request):

#     if request.method == 'POST':

#         loan_type = request.POST.get('loan_type')

#         customer = Customer.objects.create(
#             name=request.POST.get('name'),
#             address=request.POST.get('address'),
#             contact_no=request.POST.get('contact'),
#             whatsapp_no=request.POST.get('whatsapp'),
#             email=request.POST.get('email'),
#             loan_type=loan_type,
#             required_amount=request.POST.get('amount') or 0,
#             cibil_score=request.POST.get('cibil') or 0,
#         )

#         messages.success(request, "Customer Basic Details Saved ✅")

#         # Redirect based on loan type
#         if loan_type == 'PL':
#             return redirect('add_pl', pk=customer.id)

#         elif loan_type == 'BL':
#             return redirect('add_bl', pk=customer.id)

#         return redirect('customer_list')

#     return render(request, 'customers/add_customer.html')


# # ===================== PERSONAL LOAN =====================

# def add_pl(request, pk):

#     customer = get_object_or_404(Customer, id=pk)

#     if request.method == 'POST':

#         # 🔥 Yes/No → Boolean Conversion (SAFE)
#         pf_value = request.POST.get('pf')
#         itr_value = request.POST.get('itr')

#         is_pf = True if pf_value == 'Yes' else False
#         is_itr = True if itr_value == 'Yes' else False

#         # Prevent duplicate entry
#         if PersonalLoan.objects.filter(customer=customer).exists():
#             messages.warning(request, "Personal Loan already exists for this customer ⚠️")
#             return redirect('customer_list')

#         PersonalLoan.objects.create(
#             customer=customer,
#             salary_amount=request.POST.get('salary') or 0,
#             company_name=request.POST.get('company'),
#             is_pf=is_pf,
#             is_itr=is_itr,
#             residence_type=request.POST.get('residence'),
#         )

#         messages.success(request, "Personal Loan Details Saved Successfully 🎉")

#         return redirect('customer_list')

#     return render(request, 'customers/add_pl.html', {
#         'customer': customer
#     })


# # ===================== BUSINESS LOAN =====================

# # def add_bl(request, pk):

# #     customer = get_object_or_404(Customer, id=pk)

# #     if request.method == 'POST':

# #         itr_value = request.POST.get('itr')
# #         is_itr = True if itr_value == 'Yes' else False

# #         # Prevent duplicate entry
# #         if BusinessLoan.objects.filter(customer=customer).exists():
# #             messages.warning(request, "Business Loan already exists for this customer ⚠️")
# #             return redirect('customer_list')

# #         BusinessLoan.objects.create(
# #             customer=customer,
# #             business_name=request.POST.get('business'),
# #             establish_year=request.POST.get('year'),
# #             business_type=request.POST.get('type'),
# #             is_itr=is_itr,
# #             residence_type=request.POST.get('residence'),
# #             office_space=request.POST.get('office'),
# #         )

# #         messages.success(request, "Business Loan Details Saved Successfully 🎉")

# #         return redirect('customer_list')

# #     return render(request, 'customers/add_bl.html', {
# #         'customer': customer
# #     })
    
    
    
   
# def add_bl(request, pk):

#     customer = get_object_or_404(Customer, id=pk)

#     if request.method == 'POST':

#         itr_value = request.POST.get('itr') == 'Yes'

#         # 🔥 Safe Year Conversion
#         year_value = request.POST.get('year')

#         try:
#             year_value = int(year_value)
#         except:
#             year_value = 0

#         BusinessLoan.objects.create(
#             customer=customer,
#             business_name=request.POST.get('business'),
#             establish_year=year_value,
#             business_type=request.POST.get('type'),
#             is_itr=itr_value,
#             residence_type=request.POST.get('residence'),
#             office_space=request.POST.get('office'),
#         )

#         messages.success(request, "Business Loan Details Saved Successfully 🎉")

#         return redirect('customer_list')

#     return render(request, 'customers/add_bl.html', {
#         'customer': customer
#     })    
# # ===================== CUSTOMER DETAIL =====================
# def customer_detail(request, pk):

#     customer = get_object_or_404(Customer, id=pk)

#     pl = PersonalLoan.objects.filter(customer=customer).first()
#     bl = BusinessLoan.objects.filter(customer=customer).first()

#     context = {
#         'customer': customer,
#         'pl': pl,
#         'bl': bl
#     }

#     return render(request, 'customers/customer_detail.html', context)


from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from .models import Customer, PersonalLoan, BusinessLoan
from .models import CustomerStatus

from datetime import datetime

# def dashboard(request):

#     total_customers = Customer.objects.count()

#     total_pl = Customer.objects.filter(loan_type="PL").count()
#     total_bl = Customer.objects.filter(loan_type="BL").count()

#     total_login = CustomerStatus.objects.filter(is_login=True).count()
#     total_process = CustomerStatus.objects.filter(is_process=True).count()
#     total_sanction = CustomerStatus.objects.filter(is_sanction=True).count()
#     total_reject = CustomerStatus.objects.filter(is_reject=True).count()
#     total_disburse = CustomerStatus.objects.filter(is_disbursement=True).count()

#     recent_customers = Customer.objects.order_by("-id")[:5]

#     context = {
#         "total_customers": total_customers,
#         "total_pl": total_pl,
#         "total_bl": total_bl,
#         "total_login": total_login,
#         "total_process": total_process,
#         "total_sanction": total_sanction,
#         "total_reject": total_reject,
#         "total_disburse": total_disburse,
#         "recent_customers": recent_customers
#     }

#     return render(request, "dashboard.html", context)





# def dashboard(request):

#     total_customers = Customer.objects.count()

#     pl_count = Customer.objects.filter(loan_type='PL').count()
#     bl_count = Customer.objects.filter(loan_type='BL').count()

#     login_count = CustomerStatus.objects.filter(is_login=True).count()
#     process_count = CustomerStatus.objects.filter(is_process=True).count()
#     sanction_count = CustomerStatus.objects.filter(is_sanction=True).count()
#     reject_count = CustomerStatus.objects.filter(is_reject=True).count()
#     disbursement_count = CustomerStatus.objects.filter(is_disbursement=True).count()

#     pending_count = CustomerStatus.objects.filter(
#         is_login=True,
#         is_disbursement=False,
#         is_reject=False
#     ).count()

#     context = {
#         "total_customers": total_customers,
#         "pl_count": pl_count,
#         "bl_count": bl_count,
#         "login_count": login_count,
#         "process_count": process_count,
#         "sanction_count": sanction_count,
#         "reject_count": reject_count,
#         "disbursement_count": disbursement_count,
#         "pending_count": pending_count
#     }

#     return render(request, "customers/dashboard.html", context)





# def dashboard(request):

#     total_customers = Customer.objects.count()

#     pl_count = Customer.objects.filter(loan_type='PL').count()
#     bl_count = Customer.objects.filter(loan_type='BL').count()

#     login_count = CustomerStatus.objects.filter(is_login=True).count()
#     process_count = CustomerStatus.objects.filter(is_process=True).count()
#     sanction_count = CustomerStatus.objects.filter(is_sanction=True).count()
#     reject_count = CustomerStatus.objects.filter(is_reject=True).count()
#     disbursement_count = CustomerStatus.objects.filter(is_disbursement=True).count()

#     pending_count = CustomerStatus.objects.filter(
#         is_login=True,
#         is_disbursement=False,
#         is_reject=False
#     ).count()

#     context = {
#         "total_customers": total_customers,
#         "pl_count": pl_count,
#         "bl_count": bl_count,
#         "login_count": login_count,
#         "process_count": process_count,
#         "sanction_count": sanction_count,
#         "reject_count": reject_count,
#         "disbursement_count": disbursement_count,
#         "pending_count": pending_count,
#     }

#     return render(request, "dashboard.html", context)





# def dashboard(request):

#     total_customers = Customer.objects.count()
#     pl_count = Customer.objects.filter(loan_type='PL').count()

#     login_count = CustomerStatus.objects.filter(is_login=True).count()
#     process_count = CustomerStatus.objects.filter(is_process=True).count()
#     sanction_count = CustomerStatus.objects.filter(is_sanction=True).count()
#     reject_count = CustomerStatus.objects.filter(is_reject=True).count()
#     disbursement_count = CustomerStatus.objects.filter(is_disbursement=True).count()

#     pending_count = CustomerStatus.objects.filter(
#         is_login=True,
#         is_disbursement=False,
#         is_reject=False
#     ).count()

#     context = {
#         "total_customers": total_customers,
#         "pl_count": pl_count,
#         "pending_count": pending_count,
#         "disbursement_count": disbursement_count,

#         "login_count": login_count,
#         "process_count": process_count,
#         "sanction_count": sanction_count,
#         "reject_count": reject_count,
#     }

#     return render(request, "customers/dashboard.html", context)




# def dashboard(request):

#     total_customers = Customer.objects.count()

#     pl_count = Customer.objects.filter(loan_type='PL').count()
#     bl_count = Customer.objects.filter(loan_type='BL').count()

#     login_count = CustomerStatus.objects.filter(is_login=True).count()
#     process_count = CustomerStatus.objects.filter(is_process=True).count()
#     sanction_count = CustomerStatus.objects.filter(is_sanction=True).count()
#     reject_count = CustomerStatus.objects.filter(is_reject=True).count()
#     disbursement_count = CustomerStatus.objects.filter(is_disbursement=True).count()

#     pending_count = CustomerStatus.objects.filter(
#         is_login=True,
#         is_disbursement=False,
#         is_reject=False
#     ).count()

#     context = {
#         "total_customers": total_customers,
#         "pl_count": pl_count,
#         "bl_count": bl_count,

#         "login_count": login_count,
#         "process_count": process_count,
#         "sanction_count": sanction_count,
#         "reject_count": reject_count,
#         "disbursement_count": disbursement_count,
#         "pending_count": pending_count,
#     }

#     return render(request, "customers/dashboard.html", context)



def dashboard(request):

    total_customers = Customer.objects.count()

    pl_count = Customer.objects.filter(loan_type='PL').count()
    bl_count = Customer.objects.filter(loan_type='BL').count()

    login_count = CustomerStatus.objects.filter(is_login=True).count()
    process_count = CustomerStatus.objects.filter(is_process=True).count()
    sanction_count = CustomerStatus.objects.filter(is_sanction=True).count()
    reject_count = CustomerStatus.objects.filter(is_reject=True).count()
    query_count = CustomerStatus.objects.filter(is_query=True).count()
    disbursement_count = CustomerStatus.objects.filter(is_disbursement=True).count()

    pending_count = CustomerStatus.objects.filter(
        is_login=True,
        is_disbursement=False,
        is_reject=False
    ).count()

    # Top 5 Personal Loans
    top_pl = Customer.objects.filter(loan_type='PL').order_by('-id')[:5]

    # Top 5 Business Loans
    top_bl = Customer.objects.filter(loan_type='BL').order_by('-id')[:5]

    # Recent Files
    recent_files = Customer.objects.order_by('-id')[:5]

    context = {
        "total_customers": total_customers,
        "pl_count": pl_count,
        "bl_count": bl_count,
        "pending_count": pending_count,

        "login_count": login_count,
        "process_count": process_count,
        "sanction_count": sanction_count,
        "reject_count": reject_count,
         "query_count": query_count,                 # ✅ ADD THIS
        "disbursement_count": disbursement_count,

        "top_pl": top_pl,
        "top_bl": top_bl,
        "recent_files": recent_files,
    }

    return render(request, "customers/dashboard.html", context)


# def dashboard(request):

#     total_customers = Customer.objects.count()

#     pl_count = Customer.objects.filter(loan_type='PL').count()
#     bl_count = Customer.objects.filter(loan_type='BL').count()

#     login_count = CustomerStatus.objects.filter(is_login=True).count()
#     process_count = CustomerStatus.objects.filter(is_process=True).count()
#     sanction_count = CustomerStatus.objects.filter(is_sanction=True).count()
#     reject_count = CustomerStatus.objects.filter(is_reject=True).count()
#     disbursement_count = CustomerStatus.objects.filter(is_disbursement=True).count()

#     pending_count = CustomerStatus.objects.filter(
#         is_login=True,
#         is_disbursement=False,
#         is_reject=False
#     ).count()

#     context = {
#         "total_customers": total_customers,
#         "pl_count": pl_count,
#         "bl_count": bl_count,
#         "login_count": login_count,
#         "process_count": process_count,
#         "sanction_count": sanction_count,
#         "reject_count": reject_count,
#         "disbursement_count": disbursement_count,
#         "pending_count": pending_count,
#     }

#     return render(request, "dashboard.html", context)


# ================= CUSTOMER LIST =================

def customer_list(request):

    customers = Customer.objects.all().order_by('-id')

    return render(request, 'customers/customer_list.html', {
        'customers': customers
    })


# ================= CUSTOMER DETAIL =================

# def customer_detail(request, pk):

#     customer = get_object_or_404(Customer, id=pk)

#     pl = PersonalLoan.objects.filter(customer=customer).first()
#     bl = BusinessLoan.objects.filter(customer=customer).first()
    
#     return render(request, 'customers/customer_detail.html', {
#         'customer': customer,
#         'pl': pl,
#         'bl': bl
#     })




# def customer_detail(request, pk):

#     customer = get_object_or_404(Customer, id=pk)

#     pl = PersonalLoan.objects.filter(customer=customer).first()
#     bl = BusinessLoan.objects.filter(customer=customer).first()

#     latest_status = CustomerStatus.objects.filter(customer=customer).last()

#     return render(request, "customers/customer_detail.html", {
#         "customer": customer,
#         "pl": pl,
#         "bl": bl,
#         "latest_status": latest_status
#     })


def customer_detail(request, pk):

    customer = get_object_or_404(Customer, id=pk)

    pl = PersonalLoan.objects.filter(customer=customer).first()
    bl = BusinessLoan.objects.filter(customer=customer).first()

    status = CustomerStatus.objects.filter(customer=customer).first()

    current_stage = "New"

    if status:
        if status.is_disbursement:
            current_stage = "Disbursed"
        elif status.is_reject:
            current_stage = "Rejected"
        elif status.is_sanction:
            current_stage = "Sanctioned"
        elif status.is_query:
            current_stage = "Query"
        elif status.is_process:
            current_stage = "In Process"
        elif status.is_login:
            current_stage = "Login Done"

    context = {
        "customer": customer,
        "pl": pl,
        "bl": bl,
        "status": status,
        "current_stage": current_stage
    }

    return render(request, "customers/customer_detail.html", context)

# ================= ADD CUSTOMER =================

def add_customer(request):

    if request.method == 'POST':

        loan_type = request.POST.get('loan_type')

        customer = Customer.objects.create(
            name=request.POST.get('name'),
            address=request.POST.get('address'),
            contact_no=request.POST.get('contact'),
            whatsapp_no=request.POST.get('whatsapp'),
            email=request.POST.get('email'),
            loan_type=loan_type,
            required_amount=request.POST.get('amount') or 0,
            cibil_score=request.POST.get('cibil') or 0,
        )

        messages.success(request, "Customer Basic Details Saved ✅")

        if loan_type == 'PL':
            return redirect('add_pl', pk=customer.id)

        elif loan_type == 'BL':
            return redirect('add_bl', pk=customer.id)

        return redirect('customer_list')

    return render(request, 'customers/add_customer.html')


# ================= PERSONAL LOAN =================

def add_pl(request, pk):

    customer = get_object_or_404(Customer, id=pk)

    if request.method == 'POST':

        pf_value = request.POST.get('pf') == 'Yes'
        itr_value = request.POST.get('itr') == 'Yes'

        PersonalLoan.objects.create(
            customer=customer,
            salary_amount=request.POST.get('salary') or 0,
            company_name=request.POST.get('company'),
            is_pf=pf_value,
            is_itr=itr_value,
            residence_type=request.POST.get('residence'),
        )

        messages.success(request, "Personal Loan Details Saved 🎉")

        return redirect('customer_list')

    return render(request, 'customers/add_pl.html', {'customer': customer})


# ================= BUSINESS LOAN =================

def add_bl(request, pk):

    customer = get_object_or_404(Customer, id=pk)

    if request.method == 'POST':

        itr_value = request.POST.get('itr') == 'Yes'

        year_value = request.POST.get('year')
        try:
            year_value = int(year_value)
        except:
            year_value = 0

        BusinessLoan.objects.create(
            customer=customer,
            business_name=request.POST.get('business'),
            establish_year=year_value,
            business_type=request.POST.get('type'),
            is_itr=itr_value,
            residence_type=request.POST.get('residence'),
            office_space=request.POST.get('office'),
        )

        messages.success(request, "Business Loan Details Saved 🎉")

        return redirect('customer_list')

    return render(request, 'customers/add_bl.html', {'customer': customer})


# ================= EDIT CUSTOMER =================

def edit_customer(request, pk):

    customer = get_object_or_404(Customer, id=pk)

    if request.method == 'POST':

        customer.name = request.POST.get('name')
        customer.address = request.POST.get('address')
        customer.contact_no = request.POST.get('contact')
        customer.whatsapp_no = request.POST.get('whatsapp')
        customer.email = request.POST.get('email')
        customer.required_amount = request.POST.get('amount') or 0
        customer.cibil_score = request.POST.get('cibil') or 0

        customer.save()

        messages.success(request, "Customer Updated Successfully ✅")

        return redirect('customer_detail', pk=customer.id)

    return render(request, 'customers/edit_customer.html', {
        'customer': customer
    })


# ================= DELETE CUSTOMER =================

def delete_customer(request, pk):

    customer = get_object_or_404(Customer, id=pk)

    customer.delete()

    messages.success(request, "Customer Deleted Successfully 🗑️")

    return redirect('customer_list')




def add_status(request, pk):

    customer = get_object_or_404(Customer, id=pk)

    status_obj, created = CustomerStatus.objects.get_or_create(
        customer=customer
    )

    if request.method == "POST":

        step = request.POST.get("step")
        remark = request.POST.get("remark")
        date_val = request.POST.get("date")

        if date_val:
            date_val = datetime.strptime(date_val, "%Y-%m-%d").date()
        else:
            date_val = None

        if step == "login":
            status_obj.bank_name = request.POST.get("bank_name")
            status_obj.is_login = True
            status_obj.login_date = date_val
            status_obj.login_remark = remark

        elif step == "process":
            status_obj.is_process = True
            status_obj.process_date = date_val
            status_obj.process_remark = remark

        elif step == "query":
            status_obj.is_query = True
            status_obj.query_date = date_val
            status_obj.query_remark = remark

        elif step == "sanction":
            status_obj.is_sanction = True
            status_obj.sanction_date = date_val
            status_obj.sanction_remark = remark

        elif step == "reject":
            status_obj.is_reject = True
            status_obj.reject_date = date_val
            status_obj.reject_remark = remark

        elif step == "disbursement":
            status_obj.is_disbursement = True
            status_obj.disbursement_date = date_val
            status_obj.disbursement_remark = remark

        status_obj.save()

        return redirect("add_status", pk=pk)

    return render(request, "customers/add_status.html", {
        "customer": customer,
        "status": status_obj
    })


# def add_status(request, pk):

#     customer = get_object_or_404(Customer, id=pk)

#     status_obj, created = CustomerStatus.objects.get_or_create(
#         customer=customer
#     )

#     if request.method == "POST":

#         step = request.POST.get("step")
#         date_val = request.POST.get("date")
#         remark = request.POST.get("remark")

#         if step == "login":
#             status_obj.bank_name = request.POST.get("bank_name")
#             status_obj.is_login = True
#             status_obj.login_date = date_val
#             status_obj.login_remark = remark

#         elif step == "process":
#             status_obj.is_process = True
#             status_obj.process_date = date_val
#             status_obj.process_remark = remark

#         elif step == "query":
#             status_obj.is_query = True
#             status_obj.query_date = date_val
#             status_obj.query_remark = remark

#         elif step == "sanction":
#             status_obj.is_sanction = True
#             status_obj.sanction_date = date_val
#             status_obj.sanction_remark = remark

#         elif step == "reject":
#             status_obj.is_reject = True
#             status_obj.reject_date = date_val
#             status_obj.reject_remark = remark

#         elif step == "disbursement":
#             status_obj.is_disbursement = True
#             status_obj.disbursement_date = date_val
#             status_obj.disbursement_remark = remark

#         status_obj.save()

#         return redirect("add_status", pk=pk)

#     return render(request, "customers/add_status.html", {
#         "customer": customer,
#         "status": status_obj
#     })



# def add_status(request, pk):

#     customer = get_object_or_404(Customer, id=pk)

#     status_obj, created = CustomerStatus.objects.get_or_create(
#         customer=customer
#     )

#     if request.method == "POST":

#         step = request.POST.get("step")
#         remark = request.POST.get("remark")
#         date_val = request.POST.get("date")

#         if not remark:
#             messages.error(request, "Remark is required ❗")
#             return redirect("add_status", pk=pk)

#         if step == "login":
#             status_obj.bank_name = request.POST.get("bank_name")
#             status_obj.is_login = True
#             status_obj.login_date = date_val
#             status_obj.login_remark = remark

#         elif step == "process":
#             status_obj.is_process = True
#             status_obj.process_date = date_val
#             status_obj.process_remark = remark

#         elif step == "query":
#             status_obj.is_query = True
#             status_obj.query_date = date_val
#             status_obj.query_remark = remark

#         elif step == "sanction":
#             status_obj.is_sanction = True
#             status_obj.sanction_date = date_val
#             status_obj.sanction_remark = remark

#         elif step == "reject":
#             status_obj.is_reject = True
#             status_obj.reject_date = date_val
#             status_obj.reject_remark = remark

#         elif step == "disbursement":
#             status_obj.is_disbursement = True
#             status_obj.disbursement_date = date_val
#             status_obj.disbursement_remark = remark

#         status_obj.save()

#         messages.success(request, "Status Updated Successfully ✅")
#         return redirect("add_status", pk=pk)

#     return render(request, "customers/add_status.html", {
#         "customer": customer,
#         "status": status_obj
#     })


# def add_status(request, pk):

#     customer = get_object_or_404(Customer, id=pk)

#     status_obj, created = CustomerStatus.objects.get_or_create(
#         customer=customer
#     )

#     if request.method == "POST":

#         step = request.POST.get("step")
#         remark = request.POST.get("remark")
#         date_val = request.POST.get("date")

#         if not remark:
#             messages.error(request, "Remark is required ❗")
#             return redirect("add_status", pk=pk)

#         if step == "login":
#             status_obj.bank_name = request.POST.get("bank_name")
#             status_obj.is_login = True
#             status_obj.login_date = date_val
#             status_obj.login_remark = remark

#         elif step == "process":
#             status_obj.is_process = True
#             status_obj.process_date = date_val
#             status_obj.process_remark = remark

#         elif step == "query":
#             status_obj.is_query = True
#             status_obj.query_date = date_val
#             status_obj.query_remark = remark

#         elif step == "sanction":
#             status_obj.is_sanction = True
#             status_obj.sanction_date = date_val
#             status_obj.sanction_remark = remark

#         elif step == "reject":
#             status_obj.is_reject = True
#             status_obj.reject_date = date_val
#             status_obj.reject_remark = remark

#         elif step == "disbursement":
#             status_obj.is_disbursement = True
#             status_obj.disbursement_date = date_val
#             status_obj.disbursement_remark = remark

#         status_obj.save()

#         messages.success(request, "Status Updated Successfully ✅")
#         return redirect("add_status", pk=pk)

#     return render(request, "customers/add_status.html", {
#         "customer": customer,
#         "status": status_obj
#     })

# def add_status(request, pk):

#     customer = get_object_or_404(Customer, id=pk)

#     if request.method == "POST":

#         CustomerStatus.objects.create(
#             customer=customer,
#             bank_name=request.POST.get("bank_name"),
#             status=request.POST.get("status"),
#             remark=request.POST.get("remark"),
#             date=request.POST.get("status_date") or date.today()   # ✅ FIELD NAME FIX
#         )

#         messages.success(request, "Status Updated Successfully ✅")
#         return redirect("customer_detail", pk=pk)

#     return render(request, "customers/add_status.html", {
#         "customer": customer
#     })


# def add_status(request, pk):

#     customer = get_object_or_404(Customer, id=pk)

#     if request.method == "POST":

#         CustomerStatus.objects.create(
#             customer=customer,
#             bank_name=request.POST.get("bank"),
#             status=request.POST.get("status"),
#             remark=request.POST.get("remark"),
#             status_date=request.POST.get("date") or date.today()
#         )

#         messages.success(request, "Status Updated Successfully ✅")
#         return redirect("customer_detail", pk=pk)

#     return render(request, "customers/add_status.html", {
#         "customer": customer
#     })


def status_history(request, pk):

    customer = get_object_or_404(Customer, id=pk)

    statuses = CustomerStatus.objects.filter(customer=customer).order_by("-created_at")

    return render(request, "customers/status_history.html", {
        "customer": customer,
        "statuses": statuses
    })
    
    
    