import streamlit as st
import sympy as sp
import plotly.graph_objects as go
import numpy as np

# Define symbolic variable
x = sp.symbols('x')

# Function to plot the graph
def plot_function(func_str, t_value, show_derivative):
    try:
        func = sp.sympify(func_str)
        deriv = sp.diff(func, x)
        f = sp.lambdify(x, func, "numpy")
        df = sp.lambdify(x, deriv, "numpy")
        
        x_vals = np.linspace(-10, 10, 400)
        y_vals = f(x_vals)
        dy_vals = df(x_vals)

        fig = go.Figure()
        
        # Plot the function
        fig.add_trace(go.Scatter(x=x_vals, y=y_vals, mode='lines', name='f(x)'))
        
        if show_derivative:
            # Plot the derivative
            fig.add_trace(go.Scatter(x=x_vals, y=dy_vals, mode='lines', name="f'(x)"))
        
        # Plot the tangent line at t
        y_t = f(t_value)
        slope_t = df(t_value)
        tangent_line = slope_t * (x_vals - t_value) + y_t
        fig.add_trace(go.Scatter(x=x_vals, y=tangent_line, mode='lines', name=f'Tangent at t={t_value}'))
        
        # Highlight the point of tangency
        fig.add_trace(go.Scatter(x=[t_value], y=[y_t], mode='markers', marker=dict(color='red', size=10), name='Point of Tangency'))
        
        # Find and plot maxima and minima
        critical_points = sp.solve(deriv, x)
        maxima = []
        minima = []
        for point in critical_points:
            if point.is_real:
                point_val = float(point.evalf())
                second_deriv = sp.diff(deriv, x)
                second_deriv_val = second_deriv.evalf(subs={x: point_val})
                if second_deriv_val < 0:
                    maxima.append(point_val)
                elif second_deriv_val > 0:
                    minima.append(point_val)
        
        for point in maxima:
            fig.add_trace(go.Scatter(x=[point], y=[f(point)], mode='markers', marker=dict(color='blue', size=10), name='Maxima'))
        
        for point in minima:
            fig.add_trace(go.Scatter(x=[point], y=[f(point)], mode='markers', marker=dict(color='green', size=10), name='Minima'))
        
        fig.update_layout(title=f"Function: {func_str} and its Derivative",
                          xaxis_title="x",
                          yaxis_title="f(x)",
                          showlegend=True)
        
        return fig, slope_t, y_t, df(t_value)
    
    except Exception as e:
        st.error(f"Error: {e}")
        return None, None, None, None

# Streamlit App
st.title("Function Plotter with Derivatives and Tangents")

# Input the function
func_str = st.text_input("Enter a function in terms of x:", "x**2 + 3")

# Input the value of t
t_value = st.slider("Select the value of t:", -10.0, 10.0, 0.0)

# Checkbox for showing derivative
show_derivative = st.checkbox("Show Derivative")

# Plot the graph
fig, slope_t, y_t, deriv_t = plot_function(func_str, t_value, show_derivative)

if fig:
    st.plotly_chart(fig, use_container_width=True)
    st.write(f"Slope of the tangent line at t={t_value}: {slope_t}")
    st.write(f"Value of the function at t={t_value}: {y_t}")
    if show_derivative:
        st.write(f"Value of the derivative at t={t_value}: {deriv_t}")
