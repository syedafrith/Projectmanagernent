from django.contrib.auth.models import User,AbstractUser
from django.db import models

# we are using inbuilt user model and changing the behaviour of email field
User._meta.get_field('email')._unique = True

class TflProjectModel(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField()
    owner = models.ForeignKey(User,on_delete=models.CASCADE,related_name='%(class)s_owner_id')
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 'tfl_projects'
        app_label = 'projects'


class TflProjectMemberModel(models.Model):
    class ProjectMemberRole(models.TextChoices):
        ADMIN = "AN", "Admin"
        MEMBER = "MR", "Member"

    project = models.ForeignKey(User,on_delete=models.CASCADE,related_name='%(class)s_project_id')
    user = models.ForeignKey(User,on_delete=models.CASCADE,related_name='%(class)s_user_id')
    role = models.CharField(max_length=20,choices=ProjectMemberRole)

    class Meta:
        db_table = 'tfl_project_members'
        app_label = 'projects'

class TflTaskModel(models.Model):
    class TaskStatus(models.TextChoices):
        TODO = "0", "Todo"
        INPROGRESS = "1", "In Progress"
        DONE = "2", "Done"

    class TaskPriority(models.TextChoices):
        LOW = "L", "High"
        MEDIUM = "M", "Medium"
        HIGH = "H", "High"

    title = models.CharField(max_length=100)
    description = models.TextField()
    status = models.CharField(max_length=10,choices=TaskStatus)
    priority = models.CharField(max_length=10,choices=TaskPriority)
    assigned_to = models.ForeignKey(User,on_delete=models.CASCADE,null=True,related_name='%(class)s_assigned_user_id')
    project = models.ForeignKey(TflProjectModel,on_delete=models.CASCADE,related_name='%(class)s_project_id')
    created_at = models.DateTimeField(auto_now_add=True)
    due_date = models.DateTimeField()

    class Meta:
        db_table = 'tfl_tasks'
        app_label = 'tasks'

class TflCommentModel(models.Model):
    context = models.TextField()
    user = models.ForeignKey(User,on_delete=models.CASCADE,related_name='%(class)s_user_id')
    task = models.ForeignKey(TflTaskModel,on_delete=models.CASCADE,related_name='%(class)s_task_id')
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 'tfl_comments'
        app_label = 'tasks'







