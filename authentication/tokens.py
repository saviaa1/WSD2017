from django.contrib.auth.tokens import PasswordResetTokenGenerator
from django.utils import six

# Extending PasswordResetTokenGenerator to create a unique email verification
class AccountActivationTokenGenerator(PasswordResetTokenGenerator):
    def _make_hash_value(self, user, timestamp):
        return (
            six.text_type(user.pk) + six.text_type(timestamp) +
            six.text_type(user.profile.email_confirmed))

authenticationToken = AccountActivationTokenGenerator()
