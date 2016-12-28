from django.db import models

class Customer(models.Model):
	customerid = models.CharField(max_length=10)
	name = models.CharField(max_length=120,null=True)
	email =models.EmailField()
	mobile = models.IntegerField()

	def __str__(self):
		return self.name


class Transaction(models.Model):
	txnid = models.CharField(max_length=10,null=True)
	customerid = models.ForeignKey(Customer)
	amount = models.DecimalField(max_digits=6,decimal_places=2)
	time = models.DateTimeField(auto_now_add=True,auto_now=False)

	def __str__(self):
		return self.customerid.name

class File_upload(models.Model):
	files = models.FileField()
	number = models.CharField(max_length=5)

	def __str__(self):
		return self.number
