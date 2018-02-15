from models import Customer
from quickbooks.objects.customer import Customer as QbCustomer
from qbclient import client

customersLeft = True 
totalCustomers = []
startPosition = 1
maxResults = 1000
page = 1
qbLastUpdate = None

while customersLeft:
	startPosition = (page - 1) * maxResults + 1
	customers = QbCustomer.query("SELECT * FROM Customer STARTPOSITION {0} MAXRESULTS {1}".format(startPosition, maxResults),qb=client)
	totalCustomers.extend(customers)

	page += 1

	if len(customers) < 1000:
		customersLeft = False

for customer in totalCustomers:

	newCustomer = Customer()
	newCustomer.from_quickbooks(customer)
	newCustomer.save()
