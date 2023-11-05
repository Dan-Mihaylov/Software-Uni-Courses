from django.db import models
from django.core.exceptions import ValidationError


# 01 Character Classes
class BaseCharacter(models.Model):

    class Meta:
        abstract = True

    name = models.CharField(max_length=100)
    description = models.TextField()


class Mage(BaseCharacter):
    elemental_power = models.CharField(max_length=100)
    spellbook_type = models.CharField(max_length=100)


class Assassin(BaseCharacter):
    weapon_type = models.CharField(max_length=100)
    assassination_technique = models.CharField(max_length=100)


class DemonHunter(BaseCharacter):
    weapon_type = models.CharField(max_length=100)
    demon_slaying_ability = models.CharField(max_length=100)


class TimeMage(Mage):
    time_magic_mastery = models.CharField(max_length=100)
    temporal_shift_ability = models.CharField(max_length=100)


class Necromancer(Mage):
    raise_dead_ability = models.CharField(max_length=100)


class ViperAssassin(Assassin):
    venomous_strikes_mastery = models.CharField(max_length=100)
    venomous_bite_ability = models.CharField(max_length=100)


class ShadowbladeAssassin(Assassin):
    shadowstep_ability = models.CharField(max_length=100)


class VengeanceDemonHunter(DemonHunter):
    vengeance_mastery = models.CharField(max_length=100)
    retribution_ability = models.CharField(max_length=100)


class FelbladeDemonHunter(DemonHunter):
    felblade_ability = models.CharField(max_length=100)


# 02 Chat App
class UserProfile(models.Model):
    username = models.CharField(max_length=70, unique=True)
    email = models.EmailField(unique=True)
    bio = models.TextField(null=True, blank=True)


class Message(models.Model):
    sender = models.ForeignKey("UserProfile", related_name="sent_messages", on_delete=models.CASCADE)
    receiver = models.ForeignKey("UserProfile", related_name="received_messages", on_delete=models.CASCADE)
    content = models.TextField()
    timestamp = models.TimeField(auto_now_add=True)
    is_read = models.BooleanField(default=False)

    def mark_as_read(self) -> None:
        if not self.is_read:
            self.is_read = not self.is_read

    def mark_as_unread(self) -> None:
        if self.is_read:
            self.is_read = False

    def reply_to_message(self, reply_content, receiver) -> object:
        new_message = Message.objects.create(
            sender=self.receiver,
            receiver=receiver,
            content=reply_content,
        )
        return new_message

    def forward_message(self, sender, receiver) -> object:
        forwarded_message = Message.objects.create(
            sender=sender,
            receiver=receiver,
            content=self.content
        )
        return forwarded_message


# 03 Student Information
class StudentIDField(models.PositiveIntegerField):

    # This preps the data to be inserted to the db
    def get_prep_value(self, value):
        if value is None:
            return value
        if isinstance(value, float) and value > 0:
            return int(value)
        elif isinstance(value, str) and all([x.isnumeric() for x in value]):
            return int(value)
        elif isinstance(value, int):
            return value
        else:
            raise ValueError

    # This takes the info already stored in the db
    # def from_db_value(self, value ,expression, connection):
    #     if value is None:
    #         return value
    #     if isinstance(value, float) and value > 0:
    #         return int(value)
    #     elif isinstance(value, str) and all([x.isnumeric() for x in value]):
    #         return int(value)
    #     else:
    #         return None


class Student(models.Model):
    name = models.CharField(max_length=100)
    student_id = StudentIDField()


# 04 Credit Card Masking
class MaskedCreditCardField(models.CharField):

    def __init__(self, *args, **kwargs):
        kwargs["max_length"] = 20
        super().__init__(*args, **kwargs)

    # def from_db_value(self, value, expression, connection):
    #     return value

    def to_python(self, value):
        if not isinstance(value, str):
            raise ValidationError("The card number must be a string")
        elif not value.isnumeric():
            raise ValidationError("The card number must contain only digits")
        elif len(value) != 16:
            raise ValidationError("The card number must be exactly 16 characters long")
        return value

    def get_prep_value(self, value):
        return f"****-****-****-{value[-4:]}"


class CreditCard(models.Model):
    card_owner = models.CharField(max_length=100)
    card_number = MaskedCreditCardField(max_length=20)




