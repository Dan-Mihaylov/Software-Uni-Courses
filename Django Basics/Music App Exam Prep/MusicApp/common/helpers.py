from MusicApp.account.models import Profile


def check_if_profile_exist():
    if Profile.objects.all():
        return True
    return False


def get_profile_object():
    profile = Profile.objects.first()
    return profile


def get_user_albums(user: Profile):
    return user.albums.all()

