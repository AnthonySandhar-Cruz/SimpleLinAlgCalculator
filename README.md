# SimpleLinAlgCalculator
A calculator interface to quickly compute simple vector operations, simple matrix operations, and compute symbolic integrals.

### Converting to .exe
To convert this calculator application to a .exe file, first install PyInstaller using:
```
pip install pyinstaller
```
Then run:
```
pyinstaller --onefile --noconsole Calculator.py
```

## Using the Calculator
Note that the output of any computation will appear in the 'Output' field at the bottom of the application.

### Vector Operations
To input a vector, insert the entries seperated by spaces. There are 8 fields to enter vectors. They do not need to all be full. In the case of computing a dot product, the program will take the dot product of all nonempty vector entry fields. For the cross product, only 2 vector entry fields can be in use. It does not matter which two, but the cross product will compute the answer by doing (lower vector number $\times$ higher vector number). Both the vector and scalar projection will only work if both vectors are in the first and second entry fields. It will always compute the projection of vector 1 on vector 2. 'V. Arith.' stands for vector arithmetic. In this field, you can type any general vector expression such as: 3\*v1+2.54\*v2-19\*v7. Note that all vectors are represented by "v#" where # is replaced with the number of the vector. Pressing enter will compute the result. 

### Matrix Operations
To insert a matrix, the entries in a row are seperated by spaces, and rows are seperated by a comma (ex: "1 0 0, 0 1 0, 0 0 1" is a 3x3 identity matrix). The determinant function will calculate the determinant of any valid nonempty matrix entry field. It will output them in the ascending numerical order. i.e, if matrix 1, 3, and 4 are valid, their determinants will be calculated and outputted in an array in the following way: [det(m1), det(m3), det(m4)]. Matrix multiplication only works with matrix 1 and 2, and it will compute matrix 1 times matrix 2. The matrix arithmetic function works in the same way as the vector arithmetic section with "v#" replaced by "m#".

### Integration
There is a field to input a function, and the output will be the integral of that function. When entering the function, follow it with a comma, then the variable that the function is being integrated over (ex: 3\*x\*\*2+2\*x,x). Press enter to compute the result.

## Packages Used
NumPy was used for working with arrays and calculating matrix operations. SymPy was used to compute the symbolic integrals. The GUI was made using the tkinter package.
