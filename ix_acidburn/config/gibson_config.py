"""
Configuration file for IX-AcidBurn Gibson connection settings.
"""

# URL endpoint for the IX-Gibson API
GIBSON_API_URL = "http://localhost:9000/api/query"

# Timeout in seconds for Gibson API requests
REQUEST_TIMEOUT_SECONDS = 5

# Number of retry attempts for failed requests
RETRY_ATTEMPTS = 3

# Delay in seconds between retry attempts
RETRY_BACKOFF_SECONDS = 2
