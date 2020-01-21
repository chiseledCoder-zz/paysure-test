from django.db import models

# Create your models here.

BENEFITS = (
	("dentist", "dentist"),
	("optician", "optician"),
	("gynecologist", "gynecologist"),
	("orthopedic", "orthopedic"),
)


class Policy(models.Model):
	user_ext_id = models.CharField(max_length=20, unique=True)
	benefits = models.CharField(choices=BENEFITS, default=1, max_length=50)
	currency = models.CharField(max_length=3)
	total_max_amount = models.DecimalField(max_digits=8, decimal_places=2)
	timestamp = models.DateTimeField(auto_now_add=True, auto_now=False)
	updated = models.DateTimeField(auto_now_add=False, auto_now=True)

	def __str__(self):
		return self.user_ext_id


class Payment(models.Model):
	user_ext_id = models.CharField(max_length=20, unique=True)
	benefits = models.CharField(choices=BENEFITS, default=1, max_length=50)
	currency = models.CharField(max_length=3)
	amount = models.DecimalField(max_digits=8, decimal_places=2)
	timestamp = models.DateTimeField(auto_now_add=True, auto_now=False)
	updated = models.DateTimeField(auto_now_add=False, auto_now=True)

	def __str__(self):
		return self.user_ext_id
