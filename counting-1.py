from random import randint

#'random_subset' : Map a set to a random subset of it.

# 'random_bit_string' : Generate a random bit string of `length` with `weight`.

# 'draw_pascal' : Draw the Pascal triangle for `n` rows.


##### Tests #####

def test_random_subset():
    try:
        test_set = {1: 'a', 2: 'b', 3: 'c', 4: 'd', 5: 'e'}
        subset = random_subset(test_set.items())
        
        for k, v in subset.items():
            assert k in test_set and test_set[k] == v, "Subset contains elements not in the original set"
        
        assert len(subset) <= len(test_set), "Subset is larger than the original set"
        
        return "OK"
    except Exception as e:
        return f"Not OK ({str(e)})"

def test_random_bit_string():
    try:
        # Test case 1: length = 10, weight = 3
        length = 10
        weight = 3
        bit_string = random_bit_string(length, weight)
        assert len(bit_string) == length, f"Expected length {length}, but got {len(bit_string)}"
        assert sum(bit_string) == weight, f"Expected weight {weight}, but got {sum(bit_string)}"
        
        # Test case 2: length = 5, weight = 5
        length = 5
        weight = 5
        bit_string = random_bit_string(length, weight)
        assert len(bit_string) == length, f"Expected length {length}, but got {len(bit_string)}"
        assert sum(bit_string) == weight, f"Expected weight {weight}, but got {sum(bit_string)}"
        
        # Test case 3: length = 5, weight = 0
        length = 5
        weight = 0
        bit_string = random_bit_string(length, weight)
        assert len(bit_string) == length, f"Expected length {length}, but got {len(bit_string)}"
        assert sum(bit_string) == weight, f"Expected weight {weight}, but got {sum(bit_string)}"
        
        # Test case 4: length = 0, weight = 0
        length = 0
        weight = 0
        bit_string = random_bit_string(length, weight)
        assert len(bit_string) == length, f"Expected length {length}, but got {len(bit_string)}"
        assert sum(bit_string) == weight, f"Expected weight {weight}, but got {sum(bit_string)}"

        return "OK"
    except Exception as e:
        return f"Not OK ({str(e)})"

def test_draw_pascal():
    try:
        import io
        import sys

        # Helper function to capture the output of draw_pascal
        def capture_output(func, *args, **kwargs):
            old_stdout = sys.stdout
            new_stdout = io.StringIO()
            sys.stdout = new_stdout
            try:
                func(*args, **kwargs)
            finally:
                sys.stdout = old_stdout
            return new_stdout.getvalue()

        # n = 4
        output = capture_output(draw_pascal, 4)
        expected_output = "1\n1 1\n1 2 1\n1 3 3 1\n1 4 6 4 1\n"
        assert output == expected_output, f"Expected output {expected_output}, but got {output}"

        return "OK"
    except Exception as e:
        return f"Not OK ({str(e)})"

def test():
    results = {
        "random_subset": test_random_subset(),
        "random_bit_string": test_random_bit_string(),
        "draw_pascal": test_draw_pascal()
    }
    print("Function Name            | Status")
    print("-------------------------|--------")
    for func_name, status in results.items():
        print(f"{func_name:<24} | {status}")