from django.db import models
from django.utils.text import slugify

# Create your models here.

# Model/table name: Category
class Category(models.Model):
	# Detail Category fields
	name = models.CharField(max_length=50)

	# Human readable Category
	class Meta:
		verbose_name = 'Category'
		verbose_name_plural = 'Categories'

	# Display Category name
	def __str__(self):
		return self.name	

# Model/table name: Menu
class Menu(models.Model):
	# Detail Menu fields
	name = models.CharField(max_length=50)
	description = models.TextField(max_length=500)
	category = models.ForeignKey('category', on_delete=models.SET_NULL, null=True)
	price = models.DecimalField(max_digits=5, decimal_places=2)
	people = models.IntegerField()
	image = models.ImageField(upload_to='menus/', null=True, blank=True)
	slug = models.SlugField(blank=True, null=True)

	# Create slug to automatically created for link
	def save(self, *args, **kwargs):
		if not self.slug and self.name :
			self.slug = slugify(self.name)
		super(Menu, self).save(*args, **kwargs)	

	# Human readable Menu
	class Meta:
		verbose_name = 'Menu'
		verbose_name_plural = 'Menus'

	# Display Menu name
	def __str__(self):
		return self.name			