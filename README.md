# SimpleLinAlgCalculator
A calculator interface to quickly compute simple vector operations, simple matrix operations, and compute symbolic integrals.

### Converting to .exe
To convert this calculator application to a .exe file, first install PyInstaller using:
```bash
pip install pyinstaller
```
Then run:
```
pyinstaller --onefile --noconsole Calculator.py
```

## Using the Calculator
### Vector Operations
To input a vector, insert the entries seperated by spaces. There are 8 fields to enter vectors. They do not need to all be full. In the case of computing a dot product, the program will take the dot product of all nonempty vector entry fields. For the cross product, only 2 vector entry fields can be in use. It does not matter which two, but the cross product will compute the answer by doing (lower vector number $\times$ higher vector number). Both the vector and scalar projection will only work if both vectors are in the first and second entry fields. It will always compute the projection of vector 1 on vector 2. 'V. Arith.' stands for vector arithmetic. In this field, you can type any general vector expression such as: 3*v1+2.54*v2-19*v7. Note that all vectors are represented by "v#" where # is replaced with the number of the vector.
