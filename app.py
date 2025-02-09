"""Validate Best Pracitces."""

# File: vulnerable_script.py
import numpy as np

# Explicitly hardcoded sensitive data
API_KEY = "AIzaSyD-EXAMPLE1234567890abcdefgHIJKLM"
SECRET_KEY = "sk_test_4eC39HqLyjWDarjtT1zdp7dc"
password = "P@ssw0rd123!"
a = 1 + 2


def connect_to_service(API_KEY, SECRET_KEY):
    """To connect to service."""
    print(f"Connecting with API key: {API_KEY} and secret: {SECRET_KEY}")
    print(f"""Hello""")
    print(
        "Hello Hello Hello Hello Hello Hello Hello Hello Hello Hello Hello Hello Hello Hello Hello Hello Hello Hello Hello Hello Hello Hello Hello Hello Hello Hello Hello Hello Hello Hello Hello Hello Hello Hello Hello Hello Hello Hello Hello Hello Hello Hello Hello Hello Hello Hello Hello Hello Hello Hello Hello Hello Hello Hello Hello Hello Hello Hello Hello Hello Hello Hello Hello Hello Hello Hello Hello Hello Hello Hello "
    )
