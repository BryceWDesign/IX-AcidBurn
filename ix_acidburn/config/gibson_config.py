"""
Gibson Configuration — IX-AcidBurn

Defines connection parameters for communication with IX-Gibson central node.
"""

# IX-Gibson API endpoint URL
GIBSON_API_URL = "http://localhost:9000/api/query"

# Timeout for API requests in seconds
REQUEST_TIMEOUT_SECONDS = 5

# Number of retry attempts for failed requests
RETRY_ATTEMPTS = 3

# Backoff interval between retries in seconds
RETRY_BACKOFF_SECONDS = 2
