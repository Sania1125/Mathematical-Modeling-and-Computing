# Regular Falsi (False Position) Method
def regular_falsi(f, a, b, tol=1e-7, max_iter=100):
    if f(a) * f(b) >= 0:
        print("Function must have different signs at endpoints.")
        return None

    for n in range(max_iter):
        c = b - f(b) * (b - a) / (f(b) - f(a))
        if abs(f(c)) < tol:
            print(f"Found solution after {n} iterations.")
            return c
        if f(c) * f(a) < 0:
            b = c
        else:
            a = c
    print("Exceeded maximum iterations. No solution found.")
    return None

# Example usage
if __name__ == "__main__":
    f = lambda x: x**3 - x - 2
    root = regular_falsi(f, a=1, b=2)
    print(f"Root: {root}")
