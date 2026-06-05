from django.db import models

class Program(models.Model):
    p_name=models.CharField(max_length=100)

    def __str__(self):
        return self.p_name

class Student(models.Model):
    s_name=models.CharField(max_length=100)
    roll_no=models.CharField(max_length=20)
    fee_amount=models.IntegerField()
    is_paid=models.BooleanField(default=False)
    program=models.ForeignKey(Program, on_delete=models.CASCADE)

    def __str__(self):
        return self.s_name