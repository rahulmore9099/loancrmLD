# from django.db import models





# class Customer(models.Model):

#     LOAN_TYPE_CHOICES = (
#         ('PL', 'Personal Loan'),
#         ('BL', 'Business Loan'),
#     )

#     STATUS_CHOICES = (
#         ('New', 'New'),
#         ('Process', 'Process'),
#         ('Approved', 'Approved'),
#         ('Rejected', 'Rejected'),
#     )

#     name = models.CharField(max_length=200)
#     address = models.TextField()
#     contact_no = models.CharField(max_length=20)
#     whatsapp_no = models.CharField(max_length=20)
#     email = models.EmailField(blank=True, null=True)

#     loan_type = models.CharField(max_length=10, choices=LOAN_TYPE_CHOICES)
#     required_amount = models.DecimalField(max_digits=12, decimal_places=2)

#     cibil_score = models.IntegerField(blank=True, null=True)

#     joining_date = models.DateField(auto_now_add=True)
#     status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='New')

#     def __str__(self):
#         return self.name


# # ---------------- PERSONAL LOAN ----------------

# class PersonalLoan(models.Model):

#     RESIDENCE_CHOICES = (
#         ('Owned', 'Owned'),
#         ('Rented', 'Rented'),
#     )

#     customer = models.OneToOneField(Customer, on_delete=models.CASCADE)

#     salary_amount = models.DecimalField(max_digits=10, decimal_places=2)
#     company_name = models.CharField(max_length=200)

#     is_pf = models.BooleanField(default=False)
#     is_itr = models.BooleanField(default=False)

#     residence_type = models.CharField(max_length=20, choices=RESIDENCE_CHOICES)

#     def __str__(self):
#         return self.customer.name


# # ---------------- BUSINESS LOAN ----------------

# class BusinessLoan(models.Model):

#     OFFICE_CHOICES = (
#         ('Owned', 'Owned'),
#         ('Rented', 'Rented'),
#     )

#     customer = models.OneToOneField(Customer, on_delete=models.CASCADE)

#     business_name = models.CharField(max_length=200)
#     establish_year = models.IntegerField()

#     business_type = models.CharField(max_length=200)

#     is_itr = models.BooleanField(default=False)

#     residence_type = models.CharField(max_length=20)
#     office_space = models.CharField(max_length=20, choices=OFFICE_CHOICES)

#     def __str__(self):
#         return self.customer.name



# class CustomerStatus(models.Model):

#     customer = models.ForeignKey(Customer, on_delete=models.CASCADE)

#     bank_name = models.CharField(max_length=200, blank=True, null=True)

#     # LOGIN
#     is_login = models.BooleanField(default=False)
#     login_date = models.DateField(blank=True, null=True)
#     login_remark = models.TextField(blank=True, null=True)

#     # PROCESS
#     is_process = models.BooleanField(default=False)
#     process_date = models.DateField(blank=True, null=True)
#     process_remark = models.TextField(blank=True, null=True)

#     # QUERY
#     is_query = models.BooleanField(default=False)
#     query_date = models.DateField(blank=True, null=True)
#     query_remark = models.TextField(blank=True, null=True)

#     # SANCTION
#     is_sanction = models.BooleanField(default=False)
#     sanction_date = models.DateField(blank=True, null=True)
#     sanction_remark = models.TextField(blank=True, null=True)

#     # REJECT
#     is_reject = models.BooleanField(default=False)
#     reject_date = models.DateField(blank=True, null=True)
#     reject_remark = models.TextField(blank=True, null=True)

#     # DISBURSEMENT
#     is_disbursement = models.BooleanField(default=False)
#     disbursement_date = models.DateField(blank=True, null=True)
#     disbursement_remark = models.TextField(blank=True, null=True)

#     created_at = models.DateTimeField(auto_now_add=True)

# # from django.db import models


# # class CustomerStatus(models.Model):

#     STATUS_CHOICES = [
#         ('New', 'New Lead'),
#         ('Login', 'Login Done'),
#         ('Process', 'In Process'),
#         ('Query', 'Query'),
#         ('Rejected', 'Rejected'),
#         ('Sanctioned', 'Sanctioned'),
#         ('Disbursed', 'Disbursed'),
#         ('Closed', 'Closed'),
#     ]

#     customer = models.ForeignKey('Customer', on_delete=models.CASCADE, related_name='statuses')

#     status = models.CharField(max_length=20, choices=STATUS_CHOICES)

#     bank_name = models.CharField(max_length=100, blank=True, null=True)

#     remark = models.TextField(blank=True, null=True)

#     date = models.DateField()

#     created_at = models.DateTimeField(auto_now_add=True)

#     def __str__(self):
#         return f"{self.customer.name} - {self.status}"    

from django.db import models


class Customer(models.Model):

    LOAN_TYPE_CHOICES = (
        ('PL', 'Personal Loan'),
        ('BL', 'Business Loan'),
    )

    STATUS_CHOICES = (
        ('New', 'New'),
        ('Process', 'Process'),
        ('Approved', 'Approved'),
        ('Rejected', 'Rejected'),
    )

    name = models.CharField(max_length=200)
    address = models.TextField()
    contact_no = models.CharField(max_length=20)
    whatsapp_no = models.CharField(max_length=20)
    email = models.EmailField(blank=True, null=True)

    loan_type = models.CharField(max_length=10, choices=LOAN_TYPE_CHOICES)
    required_amount = models.DecimalField(max_digits=12, decimal_places=2)

    cibil_score = models.IntegerField(blank=True, null=True)

    joining_date = models.DateField(auto_now_add=True)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='New')

    def __str__(self):
        return self.name


# ---------------- PERSONAL LOAN ----------------

class PersonalLoan(models.Model):

    RESIDENCE_CHOICES = (
        ('Owned', 'Owned'),
        ('Rented', 'Rented'),
    )

    customer = models.OneToOneField(Customer, on_delete=models.CASCADE)

    salary_amount = models.DecimalField(max_digits=10, decimal_places=2)
    company_name = models.CharField(max_length=200)

    is_pf = models.BooleanField(default=False)
    is_itr = models.BooleanField(default=False)

    residence_type = models.CharField(max_length=20, choices=RESIDENCE_CHOICES)

    def __str__(self):
        return self.customer.name


# ---------------- BUSINESS LOAN ----------------

class BusinessLoan(models.Model):

    OFFICE_CHOICES = (
        ('Owned', 'Owned'),
        ('Rented', 'Rented'),
    )

    customer = models.OneToOneField(Customer, on_delete=models.CASCADE)

    business_name = models.CharField(max_length=200)
    establish_year = models.IntegerField()

    business_type = models.CharField(max_length=200)

    is_itr = models.BooleanField(default=False)

    residence_type = models.CharField(max_length=20)
    office_space = models.CharField(max_length=20, choices=OFFICE_CHOICES)

    def __str__(self):
        return self.customer.name


# ---------------- CUSTOMER STATUS WORKFLOW ----------------

class CustomerStatus(models.Model):

    customer = models.OneToOneField(Customer, on_delete=models.CASCADE)

    bank_name = models.CharField(max_length=200, blank=True, null=True)

    # LOGIN
    is_login = models.BooleanField(default=False)
    login_date = models.DateField(blank=True, null=True)
    login_remark = models.TextField(blank=True, null=True)

    # PROCESS
    is_process = models.BooleanField(default=False)
    process_date = models.DateField(blank=True, null=True)
    process_remark = models.TextField(blank=True, null=True)

    # QUERY
    is_query = models.BooleanField(default=False)
    query_date = models.DateField(blank=True, null=True)
    query_remark = models.TextField(blank=True, null=True)

    # SANCTION
    is_sanction = models.BooleanField(default=False)
    sanction_date = models.DateField(blank=True, null=True)
    sanction_remark = models.TextField(blank=True, null=True)

    # REJECT
    is_reject = models.BooleanField(default=False)
    reject_date = models.DateField(blank=True, null=True)
    reject_remark = models.TextField(blank=True, null=True)

    # DISBURSEMENT
    is_disbursement = models.BooleanField(default=False)
    disbursement_date = models.DateField(blank=True, null=True)
    disbursement_remark = models.TextField(blank=True, null=True)

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.customer.name} Status"