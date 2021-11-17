import os


def avatar_upload(instance, file) -> str:
    return os.path.join(instance.user.email, 'avatar', file)
