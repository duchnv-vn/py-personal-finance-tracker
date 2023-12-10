from django.db import models
from django.utils.timezone import now
from django.contrib.auth.models import User
from django.conf import settings
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.db.models import Sum

EXPENSE_CATEGORY_CHOICES = [
    ("Food-beverage", "Food-beverage"),
    ("Transportation", "Transportation"),
    ("Necessities", "Necessities"),
    ("Beauty-care", "Beauty-care"),
    ("Family-support", "Family-support"),
    ("Shopping", "Shopping"),
    ("Entertainment", "Entertainment"),
    ("Other", "Other")
]

TYPE_CHOICES = [
    ("Expense", "Expense"),
    ("Income", "Income")
]

RESOURCE_CHOICES = [
    ("Fulltime-job", "Fulltime-job"),
    ("Parttime-job", "Parttime-job"),
    ("Other", "Other")
]


class Saving:
    money = models.BigIntegerField()
    description = models.CharField()
    createdAt = models.DateField(default=now)
    updatedAt = models.DateField(default=now)


class Expense:
    category = models.CharField(choices=EXPENSE_CATEGORY_CHOICES)
    description = models.CharField()


class Income:
    income_resource = models.CharField(choices=RESOURCE_CHOICES)
    description = models.CharField()


class Transaction(Expense, Income):
    type = models.OneToOneField(choices=TYPE_CHOICES)
    money = models.BigIntegerField()
    createdAt = models.DateField(default=now)
    updatedAt = models.DateField(default=now)


class YearFinance:
    year = models.IntegerField(max_length=4)
    expense_money = models.BigIntegerField()
    income_money = models.BigIntegerField()
    saving_money = models.BigIntegerField()
    transactions = models.ForeignKey(Transaction)
    savings = models.ForeignKey(Saving)


class MonthFinance:
    month = models.IntegerField(min=1, max=12)
    max_expect_expense_money = models.BigIntegerField()
    expense_money = models.BigIntegerField()
    income_money = models.BigIntegerField()
    saving_money = models.BigIntegerField()
    transactions = models.ForeignKey(Transaction)
    savings = models.ForeignKey(Saving)
