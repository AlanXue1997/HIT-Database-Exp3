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

class Education(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    PRIMATY = 'P'
    JUNIOR_HIGH = 'J'
    SENIOR_HIGT = 'S'
    UNDERGRADUATE = 'U'
    GRADUATE = 'G'
    LEVEL = (
        (PRIMATY, '小学'),
        (JUNIOR_HIGH, '初中'),
        (SENIOR_HIGT, '高中'),
        (UNDERGRADUATE, '本科'),
        (GRADUATE, '硕士'),
    )
    level = models.CharField(
        max_length = 1,
        choices=LEVEL,
    )
    begin = models.DateField('Begin Date')
    end = models.DateField('End Date')
    school = models.CharField(max_length=200)

    def __str__(self):
        return self.school

class  Work(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    company = models.CharField(max_length=200)
    begin = models.DateField('Begin Date')
    end = models.DateField('End Date')
    position = models.CharField(max_length=200)
