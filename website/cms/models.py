from django.db import models
import datetime

# Create your models here.
class Story(models.Model):
	STATUS_CHOICES=(
		(1,"Needs Edit"),
		(2,"Needs Approval"),
		(3,"Published"),
		(4,"Archived"),
	)

	title=models.CharField(max_length=100)
	slug=models.SlugField()
	category=models.ForeignKey(Category)
	markdown_content=models.TextField()
	html_content=models.TextField(editable=False)
	owner=models.ForeignKey(User)
	status=models.IntegerField(choices=STATUS_CHOICES,default=1)
	created=models.DateTimeField(default=datetime.datetime.now)
	modified=models.DateTimeField(default=datetime.datetime.now)

	class Meta:
		ordering=['modified']
		verbose_name_plural="stories"
	
	@permalink
	def get_absolute_url(self):
		return {"cms-story",{},{}}

class StoryAdmin(admin.ModelAdmin):
	list_display=('title','owner','status','create','modified')
	search_fields=('title','content')
	list_filter=('status','owner','created','modified')
	prepopulated_field=('slug':('title',))
