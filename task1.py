import streamlit as st
import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import quad

st.set_option('deprecation.showPyplotGlobalUse', False)

def area_under_curve():
    st.header("Area Under Curve")
    func_input = st.text_input("Enter the function (e.g., x**2, np.sin(x)):")
    a = st.number_input("Enter the lower limit:", value=0.0)
    b = st.number_input("Enter the upper limit:", value=1.0)

    if st.button("Calculate Area"):
        try:
            func = eval(f"lambda x: {func_input}")
            area, _ = quad(func, a, b)
            st.write(f"The area under the curve {func_input} from {a} to {b} is: {area:.4f}")

            x = np.linspace(a, b, 100)
            y = [func(x_val) for x_val in x]
            fig, ax = plt.subplots()
            ax.plot(x, y)
            ax.set_xlabel("x")
            ax.set_ylabel("y")
            ax.set_title(f"Area Under Curve: {func_input}")
            st.pyplot(fig)
        except Exception as e:
            st.error(f"Error: {e}")

def determinant_product():
    st.header("Determinant Product")
    matrix1 = st.text_area("Enter the first matrix (space-separated values):")
    matrix2 = st.text_area("Enter the second matrix (space-separated values):")

    if st.button("Calculate Determinant Product"):
        try:
            matrix1 = np.array([[float(x) for x in row.split()] for row in matrix1.split('\n')])
            matrix2 = np.array([[float(x) for x in row.split()] for row in matrix2.split('\n')])
            det1 = np.linalg.det(matrix1)
            det2 = np.linalg.det(matrix2)
            product = det1 * det2
            st.write(f"Determinant of the first matrix: {det1:.4f}")
            st.write(f"Determinant of the second matrix: {det2:.4f}")
            st.write(f"Product of determinants: {product:.4f}")
        except Exception as e:
            st.error(f"Error: {e}")

def check_singularity():
    st.header("Check Matrix Singularity")
    matrix_input = st.text_area("Enter the matrix (space-separated values):")

    if st.button("Check Singularity"):
        try:
            matrix = np.array([[float(x) for x in row.split()] for row in matrix_input.split('\n')])
            det = np.linalg.det(matrix)
            if np.isclose(det, 0):
                st.write("The matrix is singular.")
            else:
                st.write("The matrix is non-singular.")
        except Exception as e:
            st.error(f"Error: {e}")

st.title("Matrix Operations")

area_under_curve()
determinant_product()
check_singularity()