from django.db import models
from django.contrib.auth.models import BaseUserManager, AbstractBaseUser
from simple_history.models import HistoricalRecords


class UserManager(BaseUserManager):
    def create_user(self, email: str, first_name: str, last_name: str, dni: int, phone: int, password=None) -> object:
        if not email:
            raise ValueError('User must have an email')

        user = self.model(
            email=self.normalize_email(email),
            first_name=first_name,
            last_name=last_name,
            dni=dni,
            phone=phone
        )

        user.set_password(password)
        user.save()
        return user

    def create_superuser(self, email: str, first_name: str, last_name: str, dni: int, phone: int,
                         password=None) -> object:
        admin = self.create_user(
            email=self.normalize_email(email),
            first_name=first_name,
            last_name=last_name,
            dni=dni,
            phone=phone,
            password=password
        )

        admin.is_admin = True
        admin.save()
        return admin


class UserModel(AbstractBaseUser):
    email = models.EmailField(unique=True, max_length=250)
    first_name = models.CharField(max_length=150)
    last_name = models.CharField(max_length=150)
    dni = models.IntegerField(unique=True)
    phone = models.IntegerField(unique=True)
    is_admin = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    historical = HistoricalRecords()
    objects = UserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ('first_name', 'last_name', 'dni', 'phone')

    def has_perm(self, perm, obj=None) -> bool:
        return True

    def has_module_perms(self, app_label) -> bool:
        return True

    @property
    def is_staff(self) -> object:
        return self.is_admin

    def __str__(self) -> str:
        return f'{self.first_name} {self.last_name}'


