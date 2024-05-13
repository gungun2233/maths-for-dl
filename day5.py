import streamlit as st
import numpy as np
import matplotlib.pyplot as plt

def display_matrix_order(matrix):
    order = len(matrix)
    st.write(f"Matrix Order: {order}x{order}")

def main():
    st.title("Vector, Matrix, and Equation Operations")

    # Select operation type
    operation_type = st.sidebar.selectbox("Select Operation Type", ["Vector", "Matrix", "Equation Solving"])

    if operation_type == "Vector":
        st.header("Vector Operations")
        vec1 = st.text_input("Enter vector 1 (comma-separated values)").split(",")
        vec2 = st.text_input("Enter vector 2 (comma-separated values)").split(",")

        vec1 = np.array([float(x) for x in vec1])
        vec2 = np.array([float(x) for x in vec2])

        st.write(f"Vector 1: {vec1}")
        st.write(f"Vector 2: {vec2}")

        operation = st.selectbox("Select Vector Operation", ["Addition", "Subtraction", "Dot Product"])

        if st.button("Perform Operation"):
            if operation == "Addition":
                vec_sum = vec1 + vec2
                st.write(f"Result: {vec_sum}")
            elif operation == "Subtraction":
                vec_diff = vec1 - vec2
                st.write(f"Result: {vec_diff}")
            elif operation == "Dot Product":
                vec_dot = np.dot(vec1, vec2)
                st.write(f"Result: {vec_dot}")

    elif operation_type == "Matrix":
        st.header("Matrix Operations")
        matrix1_input = st.text_area("Enter matrix 1 (one row per line, comma-separated values)")
        matrix2_input = st.text_area("Enter matrix 2 (one row per line, comma-separated values)")

        matrix1 = np.array([np.fromstring(row, dtype=float, sep=',') for row in matrix1_input.split('\n')])
        matrix2 = np.array([np.fromstring(row, dtype=float, sep=',') for row in matrix2_input.split('\n')])

        display_matrix_order(matrix1)
        display_matrix_order(matrix2)

        operation = st.selectbox("Select Matrix Operation", ["Addition", "Subtraction", "Multiplication", "Determinant", "Inverse"])

        if st.button("Perform Operation"):
            if operation == "Addition":
                matrix_sum = matrix1 + matrix2
                st.write(f"Result:\n{matrix_sum}")
            elif operation == "Subtraction":
                matrix_diff = matrix1 - matrix2
                st.write(f"Result:\n{matrix_diff}")
            elif operation == "Multiplication":
                matrix_mult = np.matmul(matrix1, matrix2)
                st.write(f"Result:\n{matrix_mult}")
            elif operation == "Determinant":
                det1 = np.linalg.det(matrix1)
                det2 = np.linalg.det(matrix2)
                st.write(f"Determinant of Matrix 1: {det1}")
                st.write(f"Determinant of Matrix 2: {det2}")
            elif operation == "Inverse":
                try:
                    inv1 = np.linalg.inv(matrix1)
                    st.write(f"Inverse of Matrix 1:\n{inv1}")
                except np.linalg.LinAlgError:
                    st.write("Matrix 1 is not invertible.")

                try:
                    inv2 = np.linalg.inv(matrix2)
                    st.write(f"Inverse of Matrix 2:\n{inv2}")
                except np.linalg.LinAlgError:
                    st.write("Matrix 2 is not invertible.")

    elif operation_type == "Equation Solving":
        st.header("Equation Solving")
        num_equations = st.number_input("Enter the number of equations", min_value=2, step=1)

        coefficients = []
        constants = []

        for i in range(num_equations):
            st.subheader(f"Equation {i+1}")
            coeff = st.text_input(f"Enter coefficients for equation {i+1} (comma-separated values)").split(",")
            const = st.text_input(f"Enter constant for equation {i+1}")
            coefficients.append([float(x) for x in coeff])
            constants.append(float(const))

        coefficients = np.array(coefficients)
        constants = np.array(constants)

        if st.button("Solve Equations"):
            try:
                solutions = np.linalg.solve(coefficients, constants)
                st.write(f"Solutions: {solutions}")

                # Graphical Representation
                st.subheader("Graphical Representation")
                x = np.linspace(-10, 10, 100)
                fig, ax = plt.subplots()

                for coeff, const in zip(coefficients, constants):
                    y = -coeff[0] / coeff[1] * x + const / coeff[1]
                    ax.plot(x, y, label=f"{coeff[0]}x + {coeff[1]}y = {const}")

                ax.set_xlabel("x")
                ax.set_ylabel("y")
                ax.legend()
                st.pyplot(fig)

            except np.linalg.LinAlgError:
                st.write("The system of equations has no solution or infinitely many solutions.")

if __name__ == "__main__":
    main()
