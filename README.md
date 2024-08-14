# Matrix Calculator

Matrix Calculator is a web-based tool designed for performing a variety of matrix operations, such as determinant calculation, rank determination, and arithmetic operations like addition, subtraction, and multiplication.

## Features

- **Determinant Calculation**: Compute the determinant of a matrix.
- **Rank Determination**: Find the rank of a matrix.
- **Matrix Arithmetic**: Perform addition, subtraction, and multiplication on matrices.
- **User-Friendly Interface**: The tool is designed with a focus on simplicity and ease of use, ensuring a smooth user experience.

## Technologies Used

- **Flask**: A lightweight web framework for Python, used to build the backend of the application.
- **Python**: The core programming language used for developing the logic of the matrix operations.

## Installation

To run the Matrix Calculator locally, follow these steps:

1. Clone the repository:
    ```bash
    git clone https://github.com/alandeabhijeet/matrixcal.git
    ```

2. Navigate to the project directory:
    ```bash
    cd matrixcal
    ```

3. Create and activate a virtual environment:
    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    ```

4. Install the required dependencies:
    ```bash
    pip install -r requirements.txt
    ```

5. Run the Flask application:
    ```bash
    flask run
    ```

6. Open your web browser and go to `http://127.0.0.1:5000/` to use the Matrix Calculator.

## Usage

1. Select the number of matrices and the dimensions of each matrix.
2. Input the matrix values.
3. Choose the desired operation (determinant, rank, addition, subtraction, multiplication).
4. View the result displayed on the web page.

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

