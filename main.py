import sys
import os
from src.parser import parse_python_file
from src.generator import generate_tests
from src.reviewer import review_test
from src.logger import setup_database, log_session

def run_testforge(filepath):
    print("\n" + "="*60)
    print("  TESTFORGE — AI Test Generator")
    print("="*60)

    # Step 1: Set up database
    setup_database()

    # Step 2: Check the file exists
    if not os.path.exists(filepath):
        print(f"\n  ERROR: File not found → {filepath}")
        return

    # Step 3: Parse the file
    print(f"\n  Reading: {filepath}")
    functions = parse_python_file(filepath)

    if not functions:
        print("  No functions found in this file.")
        return

    print(f"  Found {len(functions)} function(s): {[f['name'] for f in functions]}")

    # Step 4: For each function, generate → review → log
    accepted_tests = []

    for func in functions:
        print(f"\n  Generating tests for → {func['name']}()...")
        
        generated = generate_tests(func, filepath)

        result = review_test(func['name'], generated)

        log_session(
            function_name=func['name'],
            accepted=result['accepted'],
            was_edited=result.get('edited', False),
            reason=result.get('reason', '')
        )

        if result['accepted']:
            accepted_tests.append(result['test'])

    # Step 5: Save all accepted tests to one file
    if accepted_tests:
        filename = os.path.basename(filepath)
        output_path = f"tests/test_{filename}"
        with open(output_path, 'w') as f:
            f.write("\n\n".join(accepted_tests))
        print(f"\n  Tests saved to → {output_path}")
    else:
        print("\n  No tests were accepted.")

    print("\n  Done! Check the tests/ folder.\n")

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("\n  Usage: python main.py <path_to_python_file>")
        print("  Example: python main.py src/calculator.py\n")
    else:
        run_testforge(sys.argv[1])