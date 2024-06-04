import streamlit as st
import sympy as sp

def display_derivative(func, var):
    derivative = sp.diff(func, var)
    st.latex(f"f(x) = {sp.latex(func)}")
    st.latex(f"f'(x) = {sp.latex(derivative)}")

def main():
    st.title("Common Derivatives Explorer")
    st.write("This tool helps you understand common derivatives and their properties.")

    x = sp.Symbol('x')
    functions = {
        "Polynomial (x³ - 2x² + 3x - 1)": x**3 - 2*x**2 + 3*x - 1,
        "Trigonometric (sin(x))": sp.sin(x),
        "Trigonometric (cos(x))": sp.cos(x),
        "Trigonometric (tan(x))": sp.tan(x),
        "Exponential (e^x)": sp.exp(x),
        "Exponential (2^x)": 2**x,
        "Logarithmic (ln(x))": sp.log(x),
        "Logarithmic (log₁₀(x))": sp.log(x, 10),
        "Power Function (x^a)": x**sp.Symbol('a'),
        "Inverse Function (arcsin(x))": sp.asin(x),
        "Inverse Function (arctan(x))": sp.atan(x),
        "Hyperbolic (sinh(x))": sp.sinh(x),
        "Composite (e^(sin(x)))": sp.exp(sp.sin(x)),
        "Rational Function (1 / (1 + x²))": 1 / (1 + x**2)
    }

    st.header("Common Functions")
    selected_func = st.selectbox("Choose a function:", list(functions.keys()))
    st.write("The derivative of the selected function:")
    display_derivative(functions[selected_func], x)

    st.header("Properties of Derivatives")

    st.subheader("1. Multiplication by Scalars")
    st.write("If f(x) is a function and c is a constant, then:")
    st.latex(r"\frac{d}{dx}[c \cdot f(x)] = c \cdot \frac{d}{dx}[f(x)]")
    
    col1, col2 = st.columns(2)
    with col1:
        c = st.text_input("Enter a constant (c):", "3")
        f_input = st.text_input("Enter a function f(x):", "sin(x)")
    with col2:
        if st.button("Calculate d/dx[c * f(x)]"):
            try:
                c = sp.sympify(c)
                f = sp.sympify(f_input)
                display_derivative(c * f, x)
            except sp.SympifyError:
                st.error("Invalid input. Please enter valid expressions.")

    st.subheader("2. Sum Rule")
    st.write("If f(x) and g(x) are functions, then:")
    st.latex(r"\frac{d}{dx}[f(x) + g(x)] = \frac{d}{dx}[f(x)] + \frac{d}{dx}[g(x)]")
    
    col1, col2 = st.columns(2)
    with col1:
        f_sum = st.text_input("Enter function f(x):", "exp(x)")
        g_sum = st.text_input("Enter function g(x):", "log(x)")
    with col2:
        if st.button("Calculate d/dx[f(x) + g(x)]"):
            try:
                f = sp.sympify(f_sum)
                g = sp.sympify(g_sum)
                display_derivative(f + g, x)
            except sp.SympifyError:
                st.error("Invalid input. Please enter valid functions.")

    st.subheader("3. Product Rule")
    st.write("If f(x) and g(x) are functions, then:")
    st.latex(r"\frac{d}{dx}[f(x) \cdot g(x)] = f'(x) \cdot g(x) + f(x) \cdot g'(x)")
    
    col1, col2 = st.columns(2)
    with col1:
        f_prod = st.text_input("Enter function f(x):", "x^2")
        g_prod = st.text_input("Enter function g(x):", "sin(x)")
    with col2:
        if st.button("Calculate d/dx[f(x) * g(x)]"):
            try:
                f = sp.sympify(f_prod)
                g = sp.sympify(g_prod)
                display_derivative(f * g, x)
            except sp.SympifyError:
                st.error("Invalid input. Please enter valid functions.")
                
    st.subheader("4. Quotient Rule")
    st.write("If f(x) and g(x) are functions, then:")
    st.latex(r"\frac{d}{dx}\left[\frac{f(x)}{g(x)}\right] = \frac{g(x) \cdot f'(x) - f(x) \cdot g'(x)}{[g(x)]^2}")
    
    col1, col2 = st.columns(2)
    with col1:
        f_quot = st.text_input("Enter function f(x) (numerator):", "x^2")
        g_quot = st.text_input("Enter function g(x) (denominator):", "1 + x^2")
    with col2:
        if st.button("Calculate d/dx[f(x) / g(x)]"):
            try:
                f = sp.sympify(f_quot)
                g = sp.sympify(g_quot)
                display_derivative(f / g, x)
            except sp.SympifyError:
                st.error("Invalid input. Please enter valid functions.")

    st.subheader("5. Chain Rule")
    st.write("If y = f(u) and u = g(x), then:")
    st.latex(r"\frac{dy}{dx} = \frac{dy}{du} \cdot \frac{du}{dx} = f'(u) \cdot g'(x)")
    
    col1, col2 = st.columns(2)
    with col1:
        f_chain = st.text_input("Enter outer function f(u):", "sin(u)")
        g_chain = st.text_input("Enter inner function u = g(x):", "x^2 + 1")
    with col2:
        if st.button("Calculate d/dx[f(g(x))]"):
            try:
                u = sp.Symbol('u')
                f = sp.sympify(f_chain.replace('u', 'x'))
                g = sp.sympify(g_chain)
                composite = f.subs(x, g)
                display_derivative(composite, x)
            except sp.SympifyError:
                st.error("Invalid input. Please enter valid functions.")

    st.header("Explore Your Own Function")
    user_input = st.text_input("Enter a function (using 'x' as the variable):", "x^2 * sin(x)")
    if st.button("Calculate d/dx[Your Function]"):
        try:
            user_func = sp.sympify(user_input)
            st.write("The derivative of your function:")
            display_derivative(user_func, x)
        except sp.SympifyError:
            st.error("Invalid input. Please enter a valid function.")

if __name__ == "__main__":
    main()