from __future__ import unicode_literals

from django.db import models
"@python_2_unicode_compatible"
class Programme(models.Model):
	name = models.CharField(max_length=50, null=False, blank=False)
	descr = models.CharField(max_length=1000,null=False,blank=False)
	tags = models.ManyToManyField(Tag)
	users = models.ManyToManyField(User)
	courses= models.ManyToManyField(Course)
	rating = models.ForeignKey(Rating, on_delete=models.CASCADE)

"@python_2_unicode_compatible"
class Course(models.Model):
	name = models.CharField(max_length=50, null=False, blank=False)
	descr = models.CharField(max_length=1000,null=False,blank=False)
	beginDate = models.DateTimeField('Begin Date')
	duration = models.IntegerField(default=0)
	author = models.CharField(max_length=40)
	tags = models.ManyToManyField(Tag)
	#veya sa Userom preko manytomany - CourseEnrollement
	rating = models.ForeignKey(Rating, on_delete=models.CASCADE)



"@python_2_unicode_compatible"
class Section(models.Model):
	name = models.CharField(max_length=50, null=False, blank=False)
	descr = models.CharField(max_length=1000,null=False,blank=False)
	beginDate = models.DateTimeField('Begin Date')
	index = models.IntegerField(default=0)
	nextSect = models.ForeignKey(NextSection, on_delete=models.CASCADE)
	course = models.ForeignKey(Course, on_delete=models.CASCADE)


"@python_2_unicode_compatible"
class Progress(models.Model):
	value = models.CharField(max_length=2000)
	users = models.ForeignKey(User, on_delete=model.CASCADE)
	blocks = models.ForeignKey(Block, on_delete=model.CASCADE)


"@python_2_unicode_compatible"
class Tag(models.Model):
	name = model.CharField(max_length=25)