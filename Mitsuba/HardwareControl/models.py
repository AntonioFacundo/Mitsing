# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class THardwareControl(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    hardware_name = models.CharField(db_column='HARDWARE_NAME', max_length=15)  # Field name made lowercase.
    class_field = models.CharField(db_column='CLASS',
                                   max_length=40)  # Field name made lowercase. Field renamed because it was a Python reserved word.
    vendor = models.CharField(db_column='VENDOR', max_length=100, blank=True, null=True)  # Field name made lowercase.
    model = models.CharField(db_column='MODEL', max_length=50)  # Field name made lowercase.
    serial_number = models.CharField(db_column='SERIAL_NUMBER', max_length=30, blank=True,
                                     null=True)  # Field name made lowercase.
    department = models.CharField(db_column='DEPARTMENT', max_length=50)  # Field name made lowercase.
    administrator = models.CharField(db_column='ADMINISTRATOR', max_length=50, blank=True,
                                     null=True)  # Field name made lowercase.
    os = models.CharField(db_column='OS', max_length=20, blank=True, null=True)  # Field name made lowercase.
    name_cpu = models.CharField(db_column='NAME_CPU', max_length=20, blank=True,
                                null=True)  # Field name made lowercase.
    cpu_capacity = models.FloatField(db_column='CPU_CAPACITY', blank=True, null=True)  # Field name made lowercase.
    ram_capacity = models.IntegerField(db_column='RAM_CAPACITY', blank=True, null=True)  # Field name made lowercase.
    harddisc_capacity = models.IntegerField(db_column='HARDDISC_CAPACITY', blank=True,
                                            null=True)  # Field name made lowercase.
    date_purchase = models.DateTimeField(db_column='DATE_PURCHASE', blank=True, null=True)  # Field name made lowercase.
    date_discard = models.DateTimeField(db_column='DATE_DISCARD', blank=True, null=True)  # Field name made lowercase.
    net_access = models.NullBooleanField(db_column='NET_ACCESS')  # Field name made lowercase.
    office_software = models.CharField(db_column='OFFICE_SOFTWARE', max_length=20, blank=True,
                                       null=True)  # Field name made lowercase.
    antivirus_software = models.CharField(db_column='ANTIVIRUS_SOFTWARE', max_length=20, blank=True,
                                          null=True)  # Field name made lowercase.
    stock_taking_date = models.DateTimeField(db_column='STOCK_TAKING_DATE', blank=True,
                                             null=True)  # Field name made lowercase.
    external_support = models.NullBooleanField(db_column='EXTERNAL_SUPPORT')  # Field name made lowercase.
    remarks = models.TextField(db_column='REMARKS', blank=True, null=True)
# Field name made lowercase. This field type is a guess.


