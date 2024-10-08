from django.db import models
from django.contrib.auth.models import BaseUserManager, AbstractBaseUser

class MyUserManager(BaseUserManager):
    def create_user(self, email, username, date_of_birth, password=None):
        """
        Creates and saves a User with the given email, date of
        birth and password.
        """
        if not email:
            raise ValueError("Users must have an email address")

        user = self.model(
            email=self.normalize_email(email),
            username=username,
            date_of_birth=date_of_birth,
        )

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, username, date_of_birth, password=None):
        """
        Creates and saves a superuser with the given email, date of
        birth and password.
        """
        user = self.create_user(
            email,
            username=username,
            password=password,
            date_of_birth=date_of_birth,
        )
        user.is_admin = True
        user.save(using=self._db)
        return user

class MyUser(AbstractBaseUser):
    email = models.EmailField(
        verbose_name="email address",
        max_length=255,
        unique=True,
    )
    username = models.CharField(max_length=64)
    first_name = models.CharField(max_length=64, default="")
    last_name = models.CharField(max_length=64, default="")
    date_of_birth = models.DateField()
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)

    objects = MyUserManager()

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["date_of_birth", "username"]

    def __str__(self):
        return self.email

    def has_perm(self, perm, obj=None):
        "Does the user have a specific permission?"
        # Simplest possible answer: Yes, always
        return True

    def has_module_perms(self, app_label):
        "Does the user have permissions to view the app `app_label`?"
        # Simplest possible answer: Yes, always
        return True

    @property
    def is_staff(self):
        "Is the user a member of staff?"
        # Simplest possible answer: All admins are staff
        return self.is_admin

# Create your models here.
class Recipe(models.Model):
    REGIONS = {
        "RegionI" : "Ilocos Region",
        "RegionII" : "Cagayan Valley",
        "RegionIII" : "Central Luzon",
        "RegionIV‑A" : "CALABARZON",
        "MIMAROPA" : "MIMAROPA Region",
        "RegionV" : "Bicol Region",
        "CAR" : "Cordillera Administrative Region",
        "NCR" : "National Capital Region" 
    }

    name = models.CharField(max_length=171)
    description = models.CharField(max_length=750)
    region = models.CharField(max_length=64, choices=REGIONS)
    author = models.ForeignKey(MyUser, on_delete=models.CASCADE, related_name="recipes")
    ingredients = models.JSONField(blank=True)
    steps = models.JSONField(blank=True)

    def __str__(self):
        return f"{self.name}, description: {self.description}, region: {self.region}, author: {self.author.username}, ingredients: {self.ingredients}"

class Customer(models.Model):
    

    '''
    recipe = Recipe.objects.all()
    recipe = Recipe.objects.first()
    user = MyUser.objects.get(email="gavila_02@mtc.edu.ph")
    region = Recipe.REGIONS["RegionI"]
    recipe = Recipe(name="Pinakbet", description="Has vegetables.", region=region, author=user, ingredients="")
    '''