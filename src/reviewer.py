def review_test(function_name, generated_test):
    """Show the human the generated test and ask for approval"""

    print("\n" + "="*60)
    print(f"  GENERATED TEST FOR: {function_name}")
    print("="*60)
    print(generated_test)
    print("="*60)

    print("\n  Checklist — does this test:")
    print("    [?] Test the normal case correctly?")
    print("    [?] Check for None/null inputs?")
    print("    [?] Check boundary values (0, -1, very large)?")
    print("    [?] Check security edge cases?")

    while True:
        answer = input("\n  Accept this test? (yes / no / edit): ").strip().lower()

        if answer == "yes":
            return {"accepted": True, "test": generated_test, "edited": False}

        elif answer == "no":
            reason = input("  Why rejected? ")
            return {"accepted": False, "test": "", "edited": False, "reason": reason}

        elif answer == "edit":
            print("  Paste your edited version below. Type END on a new line when done:")
            lines = []
            while True:
                line = input()
                if line.strip() == "END":
                    break
                lines.append(line)
            edited = "\n".join(lines)
            return {"accepted": True, "test": edited, "edited": True, "reason": ""}

        else:
            print("  Please type yes, no, or edit")