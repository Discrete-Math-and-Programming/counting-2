# Basics of counting

## Reading

* [Levin's chapter](https://discrete.openmathbooks.org/dmoi4/sec_counting-pascal.html).
* Solve the exercises of the chapter. You can ask in class those that challenged you. Lack of questions means you understood the material.

## Coding

Please use, as the need arises, the functions you have implemented in the
previous assignments. Put your modules (= Python files) in the `lib` directory
and import from there.

* Define a function that takes a set and returns a random subset. Sets are of
    our custom type.
* Define a function that maps the parameters `length` and `weight` (both `int`)
    to a random bit string of length `length` with exactly `weight` ones. The
    return type will be a string.
* Define a function that takes an `int` parameter `n` and prints out the
    Pascal Triangle up to that height.
    ```python
    >>> draw_pascal(10)
    1
    1 1
    1 2 1
    1 3 3 1
    1 4 6 4 1
    1 5 10 10 5 1
    1 6 15 20 15 6 1
    1 7 21 35 35 21 7 1
    1 8 28 56 70 56 28 8 1
    1 9 36 84 126 126 84 36 9 1
    1 10 45 120 210 252 210 120 45 10 1
    >>>
    ```

    Try to solve the questions both with imperative and functional programming.
