from django.db import models
class Register(models.Model):
    Name=models.CharField(max_length=100)
    Email=models.CharField(max_length=100)
    account=models.CharField(max_length=30)
    password=models.CharField(max_length=100)
    amount=models.IntegerField()

    def __str__(self):
        return self.Name

class Deposit(models.Model):
    account=models.CharField(max_length=30)
    password=models.CharField(max_length=100)
    amount=models.IntegerField()

    def __str__(self):
        return self.account

class Comment(models.Model):
    Name=models.CharField(max_length=100)
    Email=models.CharField(max_length=100)
    account=models.CharField(max_length=30)
    comment=models.CharField(max_length=100)

    def __str__(self):
        return self.Name

class WithDraw(models.Model):
    account=models.CharField(max_length=30)
    password=models.CharField(max_length=100)
    amount=models.IntegerField()


    def __str__(self):
        return self.account

class Bill(models.Model):
    account=models.CharField(max_length=30)
    password=models.CharField(max_length=100)
    amount=models.IntegerField()
    billno=models.IntegerField()

    def __str__(self):
        return self.account
