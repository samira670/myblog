from django.contrib.auth.models import User

# Update the user settings for 'samira_mohammadi'
user = User.objects.get(username='samira_mohammadi')  # Replace with your username

# Ensure the user is a superuser and has staff status
user.is_superuser = True
user.is_staff = True

# Optionally, reset the password
user.set_password('your_new_password')  # Replace with your desired new password

user.save()

print("User updated successfully!")
