# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Project(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.TextField(blank=True, null=True)
    client_name = models.TextField(blank=True, null=True)
    status = models.TextField(blank=True, null=True)
    def __str__(self):
     return self.name  # or whatever your project name field is called

    class Meta:
        managed = True
        db_table = 'project'


class Tasks(models.Model):
    id = models.BigAutoField(primary_key=True)
    # We call the variable 'project' (cleaner)
# But we tell Django the real DB column is 'project-id'
    project = models.ForeignKey(
    'Project', 
     models.CASCADE, 
     db_column='project-id', 
      blank=True, 
    null=True
    )
       
    task_description = models.TextField(blank=True, null=True)
    assigned_to = models.TextField(blank=True, null=True)
    priority = models.TextField(blank=True, null=True)
    is_completed = models.BooleanField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'tasks'
        db_table_comment = 'My dynamic project tasks'
def __str__(self):
    return self.name