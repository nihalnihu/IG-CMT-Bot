import os

# Access the secret stored in the environment variable
my_secret = os.getenv('GETCODE')

# Use the secret in your script
print(f'The secret is: {my_secret}')
