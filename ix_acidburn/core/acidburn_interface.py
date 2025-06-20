"""
IX-AcidBurn CLI Interface

Allows interactive cryptography queries routed through the AcidBurnCore
to IX-Gibson for expert cryptography and secure communication insights.
"""

from core.acidburn_core import AcidBurnCore

def run_acidburn_cli():
    core = AcidBurnCore()
    print("IX-AcidBurn — Cryptography and Secure Communications Specialist")
    print("Ask your cryptography questions below. Type 'exit' to quit.\n")

    while True:
        user_input = input("AcidBurn> ").strip()
        if user_input.lower() in ("exit", "quit"):
            print("Exiting IX-AcidBurn interface. Stay secure.")
            break
        output = core.handle_query(user_input)
        print(f"→ {output}")

if __name__ == "__main__":
    run_acidburn_cli()
