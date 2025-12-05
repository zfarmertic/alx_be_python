def safe_divide(numerator, denominator):
    try:
        nume = float(numerator)
        deno = float(denominator)

        return f"The result of the division is {nume/deno}"
    except ZeroDivisionError:
        return "Error: Cannot divide by zero."
    except ValueError:
        return "Error: Please enter numeric values only."
    # else:
    #     return nume/deno
    # finally:
    #     return "succesful"
    