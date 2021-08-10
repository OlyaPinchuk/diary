from django.contrib.auth.base_user import BaseUserManager


class CustomUserManager(BaseUserManager):
    def create_user(self, email, password, **extra_kwargs):
        if not email:
            return ValueError('Email must be set.')
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_kwargs)
        user.set_password(password)
        user.save()
        return user

    def create_superuser(self, email, password, **extra_kwargs):
        extra_kwargs.setdefault('is_staff', True)
        extra_kwargs.setdefault('is_superuser', True)
        extra_kwargs.setdefault('is_active', True)

        if extra_kwargs.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff = True.')
        if extra_kwargs.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser = True.')
        return self.create_user(email, password, **extra_kwargs)
