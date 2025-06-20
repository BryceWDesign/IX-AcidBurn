"""
IX-AcidBurn User Interaction Interface

Handles command line interaction with the user and routes queries to AcidBurnCore,
which communicates with IX-Gibson for expert knowledge.
"""

from core.acidburn_core import AcidBurnCore

def run_acidburn_cli():
    acidburn_core = AcidBurnCore()
    print("IX-AcidBurn AI Module — Type your question or 'exit' to quit.")
    while True:
        user_input = input("You: ").strip()
        if user_input.lower() in ("exit", "quit"):
            print("Exiting IX-AcidBurn. Goodbye!")
            break
        answer = acidburn_core.answer_query(user_input)
        print(f"AcidBurn: {answer}")

if __name__ == "__main__":
    run_acidburn_cli()
