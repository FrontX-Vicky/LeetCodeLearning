# Test Cases for Valid Parentheses

from main import is_valid_stack_dict, is_valid_stack_direct, is_valid_optimized

# Test data: (input_string, expected_result, description)
test_cases = [
    # Basic cases
    ("()", True, "single pair"),
    ("()[]{}", True, "multiple types"),
    ("(]", False, "wrong type"),
    ("([)]", False, "wrong order"),
    ("{[]}", True, "valid nesting"),
    
    # Edge cases
    ("", True, "empty string"),
    ("((((", False, "only opening"),
    ("))))", False, "only closing"),
    ("(", False, "single opening"),
    (")", False, "single closing"),
    
    # Complex valid cases
    ("((()))", True, "nested same type"),
    ("{[()]}", True, "deeply nested"),
    ("(){}[]", True, "sequential pairs"),
    ("(()()())", True, "multiple nested"),
    ("{[()()]}", True, "complex valid"),
    
    # Complex invalid cases
    ("(()())()", True, "tricky valid"),
    ("(()", False, "extra opening"),
    ("())", False, "extra closing"),
    ("({[}])", False, "wrong nesting order"),
    ("(([]){", False, "incomplete"),
    
    # Stress tests
    ("()()()()", True, "many pairs"),
    ("((((((((((", False, "many opening"),
    ("))))))))))", False, "many closing"),
    ("({[({[({[", False, "pattern opening"),
    ("]})]})]})]})", False, "pattern closing"),
]


def run_tests():
    print("Testing is_valid_stack_dict:")
    passed = 0
    for i, (input_str, expected, description) in enumerate(test_cases, 1):
        result = is_valid_stack_dict(input_str)
        status = "✅" if result == expected else "❌"
        display_str = input_str if len(input_str) <= 20 else input_str[:20] + "..."
        print(f"  {status} Test {i:2d}: {description:25s} '{display_str:22s}' → {result}")
        if result == expected:
            passed += 1
    print(f"  Summary: {passed}/{len(test_cases)} passed\n")
    
    print("Testing is_valid_stack_direct:")
    passed = 0
    for i, (input_str, expected, description) in enumerate(test_cases, 1):
        result = is_valid_stack_direct(input_str)
        status = "✅" if result == expected else "❌"
        display_str = input_str if len(input_str) <= 20 else input_str[:20] + "..."
        print(f"  {status} Test {i:2d}: {description:25s} '{display_str:22s}' → {result}")
        if result == expected:
            passed += 1
    print(f"  Summary: {passed}/{len(test_cases)} passed\n")
    
    print("Testing is_valid_optimized:")
    passed = 0
    for i, (input_str, expected, description) in enumerate(test_cases, 1):
        result = is_valid_optimized(input_str)
        status = "✅" if result == expected else "❌"
        display_str = input_str if len(input_str) <= 20 else input_str[:20] + "..."
        print(f"  {status} Test {i:2d}: {description:25s} '{display_str:22s}' → {result}")
        if result == expected:
            passed += 1
    print(f"  Summary: {passed}/{len(test_cases)} passed\n")
    
    total_tests = len(test_cases) * 3
    print(f"TOTAL: {total_tests} tests to pass (3 approaches × {len(test_cases)} cases)")


if __name__ == "__main__":
    run_tests()
