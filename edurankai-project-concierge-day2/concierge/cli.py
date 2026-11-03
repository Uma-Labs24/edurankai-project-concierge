"""Command-line demo for Project Concierge Day 2."""
from .answering import answer_question
from .orders import lookup_order

def main():
    print("Project Concierge - Day 2 demo")
    print("1. Ask a policy question")
    print("2. Look up a mock order")
    choice = input("Choose 1 or 2: ").strip()
    if choice == "1":
        result = answer_question(input("Question: "))
        print("\nStatus:", result["status"])
        print("Answer:", result["answer"])
        for cite in result["citations"]:
            print("Citation:", cite)
    elif choice == "2":
        result = lookup_order(input("Order ID (try ORD-1001): "))
        print("\nStatus:", result.status)
        print(result.message)
        if result.order:
            print("Order:", result.order)
    else:
        print("Please choose 1 or 2.")

if __name__ == "__main__":
    main()
