import datetime
from hunger.models import InvitationCode

#send invitation code to user
def invitation_code_sent(sender, email, **kwargs):
    try:
        invitation_code = InvitationCode.objects.get(email=email)
        invitation_code.is_invited = True
        invitation_code.invited = datetime.datetime.now()
        invitation_code.save()
    except InvitationCode.DoesNotExist:
        pass

#when user with corresponding email has been created then set the code as used.
def invitation_code_used(sender, user, invitation_code, **kwargs):
    try:
        invitation_code = InvitationCode.objects.get(code=invitation_code)
        invitation_code.user = user
        invitation_code.is_used = True
        invitation_code.used = datetime.datetime.now()
        invitation_code.save()
    except InvitationCode.DoesNotExist:
        pass