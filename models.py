from peewee import *
from nameparser import HumanName

db = SqliteDatabase('jobs.db')


class BaseModel(Model):
    class Meta:
        database = db


class Customer(BaseModel):
    quickbooks_id = IntegerField(null = True)
    old_id = IntegerField(null = True)
    title = CharField(null = True)
    given_name = CharField(null = True)
    family_name = CharField(null = True)
    display_name = CharField(null = True)
    company_name = CharField(null = True)
    email_address = CharField(null = True)
    mobile = CharField(null = True)
    phone = CharField(null = True)
    line1 = CharField(null = True)
    line2 = CharField(null = True)
    line3 = CharField(null = True)
    city = CharField(null = True)
    postal_code = CharField(null = True)

    def correct_numbers(self):
        wxmPrefix = "01978"

        if self.mobile:
            self.mobile.replace(" ", "")

            if len(self.mobile) == 6:
                self.mobile = wxmPrefix + self.mobile

        if self.phone:    
            self.phone.replace(" ", "")

            if len(self.phone) == 6:
                self.phone = wxmPrefix + self.phone

    def check_names_match(self, customer):
        if self.display_name and self.display_name.lower() == customer.display_name.lower():
            print("Display Name Matched")
            return True
        elif self.given_name and self.family_name is not None and self.given_name.lower() == customer.given_name.lower() and self.family_name.lower() == customer.family_name.lower():
            print("all names Matched")
            return True
        elif self.title and self.family_name and self.title.lower() == customer.title.lower() and self.family_name.lower() == customer.family_name.lower():
            print("title Matched")
            return True
        elif self.company_name and self.company_name == customer.company_name:
            print("Company Matched")
            return True
        else:
            return False

    def check_match(self, customer):
        customer.correct_numbers()

        if self.has_details and customer.has_details:

            if self.email_address and self.email_address == customer.email_address:
                print("Email Address Matched")
                return True
            elif self.mobile and self.mobile == customer.mobile:
                print("mobile Matched")
                return True 
            elif self.phone and self.phone == customer.phone:
                print("phone Matched")
                return True
            elif self.phone and self.phone == customer.mobile:
                print("phone 2 Matched")
                return True
            elif self.mobile and self.mobile == customer.phone:
                print("mobile 2 Matched")
                return True
            elif self.line1  and self.line1 == customer.line1:
                print("Line 1 Matched")
                return True
            elif self.postal_code and self.postal_code == customer.postal_code:
                print("old postcode is {0}, existing postcode is {1}".format(self.postal_code, customer.postal_code))
                print("Postcode Matched")
                return True
        elif check_names_match(customer):
            return True
        else:
            return False

    def from_quickbooks(self, qbCustomer):
        self.quickbooks_id = qbCustomer.Id
        self.title = qbCustomer.Title
        self.deleted = qbCustomer.Active
        self.given_name = qbCustomer.GivenName
        self.family_name = qbCustomer.FamilyName
        self.company_name = qbCustomer.CompanyName
        self.display_name = qbCustomer.DisplayName

        if qbCustomer.Active:
            self.deleted = False
        else:
            self.deleted = True

        if qbCustomer.PrimaryEmailAddr:
            self.email_address = qbCustomer.PrimaryEmailAddr.Address
        else:
            self.email_address = None

        if qbCustomer.Mobile:
            self.mobile = qbCustomer.Mobile.FreeFormNumber
        else:
            self.mobile = None

        if qbCustomer.PrimaryPhone:
            self.phone = qbCustomer.PrimaryPhone.FreeFormNumber
        else:
            self.phone = None


        if qbCustomer.BillAddr:
            self.line1 = qbCustomer.BillAddr.Line1
            self.line2 = qbCustomer.BillAddr.Line2
            self.line3 = qbCustomer.BillAddr.Line3
            self.city = qbCustomer.BillAddr.City
            self.postal_code = qbCustomer.BillAddr.PostalCode
        else:
            self.line1 = None
            self.line2 = None
            self.line3 = None
            self.city = None
            self.postal_code = None

    def has_details(self):
        if self.email_address or self.mobile or self.phone or self.line1 or self.postal_code:
            return True
        else:
            return False

    def parse_names(self, fullName):
        self.display_name = fullName
        parsedName = HumanName(fullName)
        self.title = parsedName.title
        self.given_name = parsedName.first
        self.family_name = parsedName.last


class OldCustomer(BaseModel):
    quickbooks_id = IntegerField(null = True)
    old_id = IntegerField(null = True)
    title = CharField(null = True)
    given_name = CharField(null = True)
    family_name = CharField(null = True)
    display_name = CharField(null = True)
    company_name = CharField(null = True)
    email_address = CharField(null = True)
    mobile = CharField(null = True)
    phone = CharField(null = True)
    line1 = CharField(null = True)
    line2 = CharField(null = True)
    line3 = CharField(null = True)
    city = CharField(null = True)
    postal_code = CharField(null = True)

    def correct_numbers(self):
        wxmPrefix = "01978"

        if self.mobile:
            self.mobile.replace(" ", "")

            if len(self.mobile) == 6:
                self.mobile = wxmPrefix + self.mobile

        if self.phone:    
            self.phone.replace(" ", "")

            if len(self.phone) == 6:
                self.phone = wxmPrefix + self.phone

    def check_names_match(self, customer):
        if self.display_name and self.display_name.lower() == customer.display_name.lower():
            print("Display Name Matched")
            return True
        elif self.given_name and self.family_name is not None and self.given_name.lower() == customer.given_name.lower() and self.family_name.lower() == customer.family_name.lower():
            print("all names Matched")
            return True
        elif self.title and self.family_name and self.title.lower() == customer.title.lower() and self.family_name.lower() == customer.family_name.lower():
            print("title Matched")
            return True
        elif self.company_name and self.company_name == customer.company_name:
            print("Company Matched")
            return True
        else:
            return False

    def check_match(self, customer):
        customer.correct_numbers()

        if self.has_details and customer.has_details:

            if self.email_address and self.email_address == customer.email_address:
                print("Email Address Matched")
                return True
            elif self.mobile and self.mobile == customer.mobile:
                print("mobile Matched")
                return True 
            elif self.phone and self.phone == customer.phone:
                print("phone Matched")
                return True
            elif self.phone and self.phone == customer.mobile:
                print("phone 2 Matched")
                return True
            elif self.mobile and self.mobile == customer.phone:
                print("mobile 2 Matched")
                return True
            elif self.line1  and self.line1 == customer.line1:
                print("Line 1 Matched")
                return True
            elif self.postal_code and self.postal_code == customer.postal_code:
                print("old postcode is {0}, existing postcode is {1}".format(self.postal_code, customer.postal_code))
                print("Postcode Matched")
                return True
        elif check_names_match(customer):
            return True
        else:
            return False

    def from_quickbooks(self, qbCustomer):
        self.quickbooks_id = qbCustomer.Id
        self.title = qbCustomer.Title
        self.deleted = qbCustomer.Active
        self.given_name = qbCustomer.GivenName
        self.family_name = qbCustomer.FamilyName
        self.company_name = qbCustomer.CompanyName
        self.display_name = qbCustomer.DisplayName

        if qbCustomer.Active:
            self.deleted = False
        else:
            self.deleted = True

        if qbCustomer.PrimaryEmailAddr:
            self.email_address = qbCustomer.PrimaryEmailAddr.Address
        else:
            self.email_address = None

        if qbCustomer.Mobile:
            self.mobile = qbCustomer.Mobile.FreeFormNumber
        else:
            self.mobile = None

        if qbCustomer.PrimaryPhone:
            self.phone = qbCustomer.PrimaryPhone.FreeFormNumber
        else:
            self.phone = None


        if qbCustomer.BillAddr:
            self.line1 = qbCustomer.BillAddr.Line1
            self.line2 = qbCustomer.BillAddr.Line2
            self.line3 = qbCustomer.BillAddr.Line3
            self.city = qbCustomer.BillAddr.City
            self.postal_code = qbCustomer.BillAddr.PostalCode
        else:
            self.line1 = None
            self.line2 = None
            self.line3 = None
            self.city = None
            self.postal_code = None

    def has_details(self):
        if self.email_address or self.mobile or self.phone or self.line1 or self.postal_code:
            return True
        else:
            return False

    def parse_names(self, fullName):
        self.display_name = fullName
        parsedName = HumanName(fullName)
        self.title = parsedName.title
        self.given_name = parsedName.first
        self.family_name = parsedName.last


class Engineer(BaseModel):
    first_name = CharField(null = True)
    surname = CharField(null = True)
    mobile = CharField(null = True)
    email = CharField(null = True)


class Job(BaseModel):
    STATUS_LIST = ['Booked In', 'Call Out Requested', 'Initial Inspection',
                   'More Expertise', 'Parts Ordered', 'Not Repairable', 'Complete', 'Paid', 'Invoiced']
    created = DateTimeField()
    status = CharField(null = True)
    customer = ForeignKeyField(Customer, to_field="id", related_name="jobs")
    engineer_id = ForeignKeyField(Engineer, to_field="id", related_name="jobs")
    pc_make = CharField(null = True)
    password = CharField(null = True)
    work_details = TextField(null = True)
    technicians_comments = TextField(null = True)
    psu = BooleanField(default=False)
    carry_case = BooleanField(default=False)
    power_cable = BooleanField(default=False)
    cables = BooleanField(default=False)
    data_backup = BooleanField(default=False)
    software = CharField(null = True)
    other = CharField(null = True)
