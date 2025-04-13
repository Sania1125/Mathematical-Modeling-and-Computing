# Newton-Raphson Method
def newton_raphson(f, df, x0, tol=1e-7, max_iter=100):
    xn = x0
    for n in range(max_iter):
        fxn = f(xn)
        if abs(fxn) < tol:
            print(f"Found solution after {n} iterations.")
            return xn
        dfxn = df(xn)
        if dfxn == 0:
            print("Zero derivative. No solution found.")
            return None
        xn = xn - fxn / dfxn
    print("Exceeded maximum iterations. No solution found.")
    return None

# Example usage
if __name__ == "__main__":
    f = lambda x: x**3 - x - 2
    df = lambda x: 3*x**2 - 1
    root = newton_raphson(f, df, 1.5)
    print(f"Root: {root}")
Added Newton-Raphson Method in Python
