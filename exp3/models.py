from django.db import models

# Create your models here.
class User(models.Model):
    email = models.CharField(max_length=100, unique=True, blank=False)
    password = models.CharField(max_length=100, blank=False)
    name = models.CharField(max_length=100, blank=False)
    NOT_SET = 'N'
    MAN = 'M'
    WOMAN = 'W'
    OTHERS = 'O'
    SEX=(
        (NOT_SET, '未定义'),
        (MAN, '男'),
        (WOMAN, '女'),
        (OTHERS, '其他')
    )
    sex = models.CharField(
        max_length=1,
        choices=SEX,
        default=NOT_SET,
    )
    birth = models.DateField('Birthday')
    address = models.CharField(max_length=200)

    def __str__(self):
        return self.email