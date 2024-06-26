# models.py
from django.contrib.auth.models import AbstractUser
from django.db import models
from django.core.exceptions import ValidationError
from django.core.validators import MinValueValidator,MaxValueValidator
from django.utils import timezone
from django.db.models.signals import post_save
from django.dispatch import receiver
from datetime import datetime


class CustomUser(AbstractUser):
    ROLE_CHOICES = [
        ('receptionist', 'Lễ tân'),
        ('doctor', 'Bác sĩ'),
        ('hr_manager', 'Quản lý nhân sự'),
        ('warehouse_manager', 'Quản lý kho'),
    ]

    GENDER_CHOICES = [
        ('male', 'Male'),
        ('female', 'Female'),
    ]
    
    role = models.CharField(max_length=20, choices=ROLE_CHOICES)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    date_of_birth = models.DateField(null=True, blank=True)
    gender = models.CharField(max_length=10, choices=GENDER_CHOICES, blank=True, null=True)
    start_date = models.DateField(null=True, blank=True)  # Ngày vào làm
    address = models.CharField(max_length=255, blank=True)  # Địa chỉ


class Benhnhan(models.Model):
	hoten = models.CharField(max_length = 100)
	gioitinh = models.CharField(max_length = 100)
	namsinh = models.IntegerField()
	diachi = models.CharField(max_length = 100)
	ngaykham = models.DateField(default='2024-01-01')

class Hoadon(models.Model):
    benhnhan = models.OneToOneField(Benhnhan,on_delete=models.CASCADE)
    tienkham = models.IntegerField()
    tienthuoc = models.IntegerField()
    
class PhieuKB(models.Model):
    benhnhan = models.OneToOneField(Benhnhan,on_delete=models.CASCADE)
    trieuchung = models.CharField(max_length=100)
    dudoan = models.CharField(max_length=100)
    
class Thuoc(models.Model):
    tenThuoc = models.CharField(max_length=50)
    giatheovien = models.IntegerField()
    giatheochai = models.IntegerField()
    soviencon = models.IntegerField()
    sochaicon = models.IntegerField()

class PKBthuoc(models.Model):
    phieukb = models.ForeignKey(PhieuKB,on_delete=models.CASCADE)
    thuoc = models.ForeignKey(Thuoc,on_delete=models.CASCADE)
    donvi = models.CharField(max_length=50)
    soluong = models.IntegerField()
    cachdung = models.CharField(max_length=50)
    
class DefaultValues(models.Model):
    max_patient = models.IntegerField(default=40)
    cachdung = models.CharField(max_length = 500,default='A B C D')
    loaibenh = models.CharField(max_length = 500,default='A B C D E')
    tienkham = models.IntegerField(default=30000)
    
class thietbiYte(models.Model):
    SUPPLIER_CHOICES = [
        ('Supplier A', 'Supplier A'),
        ('Supplier B', 'Supplier B'),
        ('Supplier C', 'Supplier C'),
        ('Supplier D', 'Supplier D'),
        ('Supplier E', 'Supplier E'),
    ]

    name = models.CharField(max_length=200)
    quantity = models.IntegerField()
    supplier = models.CharField(max_length=200, choices=SUPPLIER_CHOICES)
    import_date = models.DateField()
    price = models.IntegerField()
    purpose = models.TextField()

    def __str__(self):
        return self.name
    
