def review_test(function_name, generated_test, attempt=1, max_attempts=3):
    """Show the human the generated test and ask for approval"""

    print("\n" + "="*60)
    if attempt > 1:
        print(f"  RETRY #{attempt} — REWRITTEN TEST FOR: {function_name}")
    else:
        print(f"  GENERATED TEST FOR: {function_name}")
    print("="*60)
    print(generated_test)
    print("="*60)

    print("\n  Checklist — does this test:")
    print("    [?] Test the normal case correctly?")
    print("    [?] Check for None/null inputs?")
    print("    [?] Check boundary values (0, -1, very large)?")
    print("    [?] Check security edge cases?")

    if attempt > 1:
        print(f"\n  ⚠️  This is retry attempt {attempt} of {max_attempts}")

    while True:
        answer = input("\n  Accept this test? (yes / no / edit): ").strip().lower()

        if answer == "yes":
            return {"accepted": True, "test": generated_test, 
                    "edited": False, "reason": "", "attempts": attempt}

        elif answer == "no":
            reason = input("  Why rejected? (be specific — AI will use this to rewrite): ")
            return {"accepted": False, "test": "", 
                    "edited": False, "reason": reason, "attempts": attempt}

        elif answer == "edit":
            print("  Paste your edited version below. Type END on a new line when done:")
            lines = []
            while True:
                line = input()
                if line.strip() == "END":
                    break
                lines.append(line)
            edited = "\n".join(lines)
            return {"accepted": True, "test": edited, 
                    "edited": True, "reason": "", "attempts": attempt}

        else:
            print("  Please type yes, no, or edit")