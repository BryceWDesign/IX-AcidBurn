"""
IX-AcidBurn CLI Interface

Command-line entry point for asking cybersecurity exploit and vulnerability questions.
"""

import sys
from core.query_processor import IXAcidBurnQueryProcessor

def main():
    if len(sys.argv) < 2:
        print("Usage: python main.py \"Your cybersecurity question here\"")
        sys.exit(1)

    query = sys.argv[1]
    processor = IXAcidBurnQueryProcessor()
    response = processor.process_query(query)

    print("\n💻 IX-AcidBurn Response 💻")
    print(response)

if __name__ == "__main__":
    main()
