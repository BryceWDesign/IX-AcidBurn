"""
IX-AcidBurn Utility Functions

Provides text sanitization, formatting, and simple validation
for exploit-related input handling.
"""

import re

def clean_query(query: str) -> str:
    """
    Normalize and sanitize input query string.
    Removes extra whitespace and invalid characters.
    """
    query = query.strip()
    query = re.sub(r'\s+', ' ', query)
    query = re.sub(r'[^\w\s\-\.@:\']+', '', query)
    return query

def is_valid_query(query: str) -> bool:
    """
    Check if the query is minimally valid for processing.
    """
    return bool(query and len(query) > 3 and any(char.isalpha() for char in query))

# Example usage
if __name__ == "__main__":
    examples = [
        "Define SQL injection!",
        "   What is a rootkit?   ",
        "???",
        ""
    ]
    for example in examples:
        cleaned = clean_query(example)
        valid = is_valid_query(cleaned)
        print(f"Original: '{example}' → Cleaned: '{cleaned}' | Valid: {valid}")
