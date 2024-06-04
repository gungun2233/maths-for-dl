import streamlit as st
import sympy as sp
import numpy as np
import matplotlib.pyplot as plt

def plot_function_and_tangent(func, x_val, x_range=(-10, 10)):
    x = sp.Symbol('x')
    f = sp.lambdify(x, func, "numpy")
    derivative = sp.diff(func, x)
    df = sp.lambdify(x, derivative, "numpy")
    
    x_vals = np.linspace(x_range[0], x_range[1], 1000)
    y_vals = f(x_vals)
    
    slope = df(x_val)
    y_val = f(x_val)
    
    fig, ax = plt.subplots()
    ax.plot(x_vals, y_vals, label=f'f(x) = {sp.latex(func)}')
    ax.plot(x_val, y_val, 'ro', label='Point')
    
    # Plot tangent line
    tangent_x = np.array([x_val - 5, x_val + 5])
    tangent_y = slope * (tangent_x - x_val) + y_val
    ax.plot(tangent_x, tangent_y, 'g--', label=f'Tangent (slope = {slope:.2f})')
    
    ax.axhline(y=0, color='k', alpha=0.3)
    ax.axvline(x=0, color='k', alpha=0.3)
    ax.grid(alpha=0.3)
    ax.legend()
    ax.set_title(f'Function and Tangent Line at x = {x_val}')
    return fig

def display_derivative(func, var):
    derivative = sp.diff(func, var)
    st.latex(f"f(x) = {sp.latex(func)}")
    st.latex(f"f'(x) = {sp.latex(derivative)}")

def main():
    st.title("Derivative Explorer with Tangent Lines")
    st.write("Visualize functions, their derivatives, and tangent lines.")

    x = sp.Symbol('x')
    functions = {
        "Polynomial (x³ - 2x² + 3x - 1)": x**3 - 2*x**2 + 3*x - 1,
        "Trigonometric (sin(x))": sp.sin(x),
        "Exponential (e^x)": sp.exp(x),
        "Logarithmic (ln(x))": sp.log(x),
        "Rational (1 / (1 + x²))": 1 / (1 + x**2)
    }

    st.header("Visualize Function and Its Tangent")
    selected_func = st.selectbox("Choose a function:", list(functions.keys()))
    func = functions[selected_func]

    col1, col2 = st.columns(2)
    with col1:
        x_val = st.number_input("Enter x-value for tangent line:", value=1.0, step=0.1)
    with col2:
        x_min = st.number_input("Min x-value for graph:", value=-5.0, step=0.5)
        x_max = st.number_input("Max x-value for graph:", value=5.0, step=0.5)

    fig = plot_function_and_tangent(func, x_val, (x_min, x_max))
    st.pyplot(fig)

    st.write("The derivative of the selected function:")
    display_derivative(func, x)

    st.header("Properties of Derivatives")

    st.subheader("1. Multiplication by Scalars")
    st.write("If f(x) is a function and c is a constant, then:")
    st.latex(r"\frac{d}{dx}[c \cdot f(x)] = c \cdot \frac{d}{dx}[f(x)]")
    
    c = st.number_input("Enter a constant (c):", value=3.0, step=0.1)
    f_input = st.text_input("Enter a function f(x):", "sin(x)")
    if st.button("Calculate and Plot d/dx[c * f(x)]"):
        try:
            f = sp.sympify(f_input)
            display_derivative(c * f, x)
            fig = plot_function_and_tangent(c * f, x_val, (x_min, x_max))
            st.pyplot(fig)
        except sp.SympifyError:
            st.error("Invalid input. Please enter a valid function.")

    st.subheader("2. Sum Rule")
    st.write("If f(x) and g(x) are functions, then:")
    st.latex(r"\frac{d}{dx}[f(x) + g(x)] = \frac{d}{dx}[f(x)] + \frac{d}{dx}[g(x)]")
    
    f_sum = st.text_input("Enter function f(x):", "exp(x)")
    g_sum = st.text_input("Enter function g(x):", "log(x)")
    if st.button("Calculate and Plot d/dx[f(x) + g(x)]"):
        try:
            f = sp.sympify(f_sum)
            g = sp.sympify(g_sum)
            sum_func = f + g
            display_derivative(sum_func, x)
            fig = plot_function_and_tangent(sum_func, x_val, (x_min, x_max))
            st.pyplot(fig)
        except sp.SympifyError:
            st.error("Invalid input. Please enter valid functions.")

    st.subheader("3. Product Rule")
    st.write("If f(x) and g(x) are functions, then:")
    st.latex(r"\frac{d}{dx}[f(x) \cdot g(x)] = f'(x) \cdot g(x) + f(x) \cdot g'(x)")
    
    f_prod = st.text_input("Enter function f(x):", "x^2")
    g_prod = st.text_input("Enter function g(x):", "sin(x)")
    if st.button("Calculate and Plot d/dx[f(x) * g(x)]"):
        try:
            f = sp.sympify(f_prod)
            g = sp.sympify(g_prod)
            prod_func = f * g
            display_derivative(prod_func, x)
            fig = plot_function_and_tangent(prod_func, x_val, (x_min, x_max))
            st.pyplot(fig)
        except sp.SympifyError:
            st.error("Invalid input. Please enter valid functions.")

    st.subheader("4. Quotient Rule")
    st.write("If f(x) and g(x) are functions, then:")
    st.latex(r"\frac{d}{dx}\left[\frac{f(x)}{g(x)}\right] = \frac{g(x) \cdot f'(x) - f(x) \cdot g'(x)}{[g(x)]^2}")
    
    f_quot = st.text_input("Enter function f(x) (numerator):", "x^2")
    g_quot = st.text_input("Enter function g(x) (denominator):", "1 + x^2")
    if st.button("Calculate and Plot d/dx[f(x) / g(x)]"):
        try:
            f = sp.sympify(f_quot)
            g = sp.sympify(g_quot)
            quot_func = f / g
            display_derivative(quot_func, x)
            fig = plot_function_and_tangent(quot_func, x_val, (x_min, x_max))
            st.pyplot(fig)
        except sp.SympifyError:
            st.error("Invalid input. Please enter valid functions.")
                
    st.header("Explore Your Own Function")
    user_input = st.text_input("Enter a function (using 'x' as the variable):", "x^2 * sin(x)")
    if st.button("Calculate and Plot d/dx[Your Function]"):
        try:
            user_func = sp.sympify(user_input)
            display_derivative(user_func, x)
            fig = plot_function_and_tangent(user_func, x_val, (x_min, x_max))
            st.pyplot(fig)
        except sp.SympifyError:
            st.error("Invalid input. Please enter a valid function.")

if __name__ == "__main__":
    main()