import tkinter as tk 
import numpy as np
from sympy import *
import numpy.linalg as nlg

#-------------------------------------------------------------------------------------------------------------------------------------------------------------------
#Setup
#-------------------------------------------------------------------------------------------------------------------------------------------------------------------

window = tk.Tk()
window.title("Calculator")
window.geometry('545x550')
window.configure(background='#151515')

#-------------------------------------------------------------------------------------------------------------------------------------------------------------------
#Math functions
#-------------------------------------------------------------------------------------------------------------------------------------------------------------------

#Create dot product function
def vect_dot():
    all_vecs = [get_v1(),get_v2(),get_v3(),get_v4(),get_v5(),get_v6(),get_v7(),get_v8()]
    dot_list = []
    code = 1
    #Find all vector entry fields that are nonempty
    for vec in all_vecs:
        if vec != []:
            dot_list.append(list(vec))
    #Ensure that all vectors match in dimension
    for vec_ind in range(len(dot_list)-1):
        if len(dot_list[vec_ind]) == len(dot_list[vec_ind+1]):
            code = 0
        else:
            code = 1
            break
    answer = 0
    #Calculate dot product
    if code == 0:
        for i in range(len(dot_list[0])):
            temp_prod = 1
            for j in dot_list:
                temp_prod *= j[i]
            answer += temp_prod
    else:
        answer = "error"
    return answer

#Create cross product function
def vect_cross():
    all_vecs = [get_v1(),get_v2(),get_v3(),get_v4(),get_v5(),get_v6(),get_v7(),get_v8()]
    c_list = []
    code = 1
    #Find all vector entry fields that are nonempty
    for vec in all_vecs:
        if vec != []:
            c_list.append(list(vec))
    #Ensure vectors are of correct dimension, and that there are only 3 nonempty vector entry fields
    for vec_ind in range(len(c_list)):
        if len(c_list[vec_ind]) == 3 and len(c_list) == 2 :
            code = 0
        else:
            code = 1
            break
    answer = 0
    #Calculate cross product
    if code == 0:
        answer = [c_list[0][1]*c_list[1][2]-c_list[0][2]*c_list[1][1], c_list[0][2]*c_list[1][0]-c_list[0][0]*c_list[1][2], c_list[0][0]*c_list[1][1]-c_list[0][1]*c_list[1][0]]
    else:
        answer = "error"
    return answer

#Create function to calculate any arithmetic expression with vectors
def vect_arith(expression):
    all_vecs = [get_v1(),get_v2(),get_v3(),get_v4(),get_v5(),get_v6(),get_v7(),get_v8()]
    vectors = {"v1":np.array(all_vecs[0]),"v2":np.array(all_vecs[1]),"v3":np.array(all_vecs[2]),"v4":np.array(all_vecs[3]),"v5":np.array(all_vecs[4]),"v6":np.array(all_vecs[5]),"v7":np.array(all_vecs[6]),"v8":np.array(all_vecs[7])}
    answer = eval(expression, vectors)
    return answer

#Create function to calculate any arithmetic expression with matrices
def mat_arith(expression):
    all_mats = [get_m1(),get_m2(),get_m3(),get_m4()]
    matrices = {"m1":np.array(all_mats[0]),"m2":np.array(all_mats[1]),"m3":np.array(all_mats[2]),"m4":np.array(all_mats[3])}
    answer = eval(expression, matrices)
    return answer

#Create function to calculate determinant of all valid entered matricies
def mat_det():
    all_mats = [np.array(get_m1()), np.array(get_m2()), np.array(get_m3()), np.array(get_m4())]
    pre_ans = []
    for mat in all_mats:
        if mat.size > 0 and mat.shape[0] == mat.shape[1]:
            pre_ans.append(mat)
    answer = []
    for mat in pre_ans:
        answer.append(nlg.det(mat))
    return answer

#Create function to multiply two matricies (note that this only multiplies matrix 1 and 2 together)
def mat_mul():
    answer = np.matmul(np.array(get_m1()),np.array(get_m2()))
    return answer

#Create function to calculate the vector projection of vector 1 on vector 2
def vect_vproj():
    v1 = np.array(get_v1())
    v2 = np.array(get_v2())
    vecs = [v1,v2]
    dot_ans = 0
    for i in range(len(v1)):
            temp_prod = 1
            for j in vecs:
                temp_prod *= j[i]
            dot_ans += temp_prod
    v1_mag = 0
    for i in range(len(v1)):
        v1_mag += v1[i]**2
    mult_fact = dot_ans/v1_mag
    answer = mult_fact*v1
    return answer

#Create function to calculate the scalar projection of vector 1 on vector 2
def vect_sproj():
    v1 = np.array(get_v1())
    v2 = np.array(get_v2())
    vecs = [v1,v2]
    dot_ans = 0
    for i in range(len(v1)):
            temp_prod = 1
            for j in vecs:
                temp_prod *= j[i]
            dot_ans += temp_prod
    v1_mag = 0
    for i in range(len(v1)):
        v1_mag += v1[i]**2
    v1_mag = np.sqrt(v1_mag)
    answer = dot_ans/v1_mag
    return answer

#-------------------------------------------------------------------------------------------------------------------------------------------------------------------
#Vectors
#-------------------------------------------------------------------------------------------------------------------------------------------------------------------

#Setup styling
vector_font = ("Fira Code", 9, "normal")
vector_width = 8
vector_height = 1
vector_x = 10
vector_y = 10
vector_bg = "#2a2d2e"

#Vector 1
def get_v1():
    v1 = list(map(float, v1_entry.get().strip().split())) #Retrieve the input for vector 1 and put it into array format
    return v1

#Vector 1 label
v1_name = tk.Label(window, text="Vector 1", bg=vector_bg, font=vector_font, width=vector_width, height=vector_height, foreground="white")
v1_name.place(x=10,y=10)

#Vector 1 entry field
v1_entry = tk.Entry(window, width=30)
v1_entry.place(x=80, y=10)
v1_entry.bind("<Return>", get_v1)

#Vector 2
def get_v2():
    v2 = list(map(float, v2_entry.get().strip().split())) #Retrieve the input for vector 2 and put it into array format
    return v2

#Vector 2 label
v2_name = tk.Label(window, text="Vector 2", bg=vector_bg, font=vector_font, width=vector_width, height=vector_height, foreground="white")
v2_name.place(x=10,y=40)

#Vector 2 entry field
v2_entry = tk.Entry(window, width=30)
v2_entry.place(x=80, y=40)
v2_entry.bind("<Return>", get_v2)

#Vector 3
def get_v3():
    v3 = list(map(float, v3_entry.get().strip().split())) #Retrieve the input for vector 3 and put it into array format
    return v3

#Vector 3 label
v3_name = tk.Label(window, text="Vector 3", bg=vector_bg, font=vector_font, width=vector_width, height=vector_height, foreground="white")
v3_name.place(x=10,y=70)

#Vector 3 entry field
v3_entry = tk.Entry(window, width=30)
v3_entry.place(x=80, y=70)
v3_entry.bind("<Return>", get_v3)

#Vector 4
def get_v4():
    v4 = list(map(float, v4_entry.get().strip().split())) #Retrieve the input for vector 4 and put it into array format
    return v4

#Vector 4 label
v4_name = tk.Label(window, text="Vector 4", bg=vector_bg, font=vector_font, width=vector_width, height=vector_height, foreground="white")
v4_name.place(x=10,y=100)

#Vector 4 entry field
v4_entry = tk.Entry(window, width=30)
v4_entry.place(x=80, y=100)
v4_entry.bind("<Return>", get_v4)

#Vector 5
def get_v5():
    v5 = list(map(float, v5_entry.get().strip().split()))
    return v5

#Vector 5 label
v5_name = tk.Label(window, text="Vector 5", bg=vector_bg, font=vector_font, width=vector_width, height=vector_height, foreground="white")
v5_name.place(x=280,y=10)

#Vector 5 entry field
v5_entry = tk.Entry(window, width=30)
v5_entry.place(x=350, y=10)
v5_entry.bind("<Return>", get_v5)

#Vector 6
def get_v6():
    v6 = list(map(float, v6_entry.get().strip().split()))
    return v6

#Vector 6 label
v6_name = tk.Label(window, text="Vector 6", bg=vector_bg, font=vector_font, width=vector_width, height=vector_height, foreground="white")
v6_name.place(x=280,y=40)

#Vector 6 entry field
v6_entry = tk.Entry(window, width=30)
v6_entry.place(x=350, y=40)
v6_entry.bind("<Return>", get_v6)

#Vector 7
def get_v7():
    v7 = list(map(float, v7_entry.get().strip().split()))
    return v7

#Vector 7 label
v7_name = tk.Label(window, text="Vector 7", bg=vector_bg, font=vector_font, width=vector_width, height=vector_height, foreground="white")
v7_name.place(x=280,y=70)

#Vector 7 entry field
v7_entry = tk.Entry(window, width=30)
v7_entry.place(x=350, y=70)
v7_entry.bind("<Return>", get_v7)

#Vector 8
def get_v8():
    v8 = list(map(float, v8_entry.get().strip().split()))
    return v8

#Vector 8 label
v8_name = tk.Label(window, text="Vector 8", bg=vector_bg, font=vector_font, width=vector_width, height=vector_height, foreground="white")
v8_name.place(x=280,y=100)

#Vector 8 entry field
v8_entry = tk.Entry(window, width=30)
v8_entry.place(x=350, y=100)
v8_entry.bind("<Return>", get_v8)

#Vector arithmetic
def get_va():
    va = va_entry.get()  #Retrieve arithmetic expression for vectors
    return va

#Vector arithmetic label
va_name = tk.Label(window, text="V. Arith.", bg=vector_bg, font=vector_font, width=vector_width, height=vector_height, foreground="white")
va_name.place(x=10,y=130)

#Vector arithmetic entry field
va_entry = tk.Entry(window, width=63)
va_entry.place(x=80, y=130)
va_entry.bind("<Return>", get_va)

#-------------------------------------------------------------------------------------------------------------------------------------------------------------------
#Functions to output vector calculation results
#-------------------------------------------------------------------------------------------------------------------------------------------------------------------

def vect_dot_ans():
    output_entry.delete(0, tk.END)
    output_entry.insert(0, str(vect_dot()))

def vect_cross_ans():
    output_entry.delete(0, tk.END)
    output_entry.insert(0, str(vect_cross()))

def vect_arith_ans():
    output_entry.delete(0, tk.END)
    output_entry.insert(0, str(vect_arith(get_va())))

def vect_vproj_ans():
    output_entry.delete(0, tk.END)
    output_entry.insert(0, str(vect_vproj()))

def vect_sproj_ans():
    output_entry.delete(0, tk.END)
    output_entry.insert(0, str(vect_sproj()))

#-------------------------------------------------------------------------------------------------------------------------------------------------------------------
#Button setup
#-------------------------------------------------------------------------------------------------------------------------------------------------------------------

button_width = 10
button_height = 1
button_x = 10
button_y = 10
button_font = ("Fira Code", 12, "bold")
button_bg = "#f3c877"

#-------------------------------------------------------------------------------------------------------------------------------------------------------------------
#Vector operations buttons
#-------------------------------------------------------------------------------------------------------------------------------------------------------------------

dot_b = tk.Label(window,text="Dot",bg=button_bg,width=vector_width,height=vector_height,font=vector_font)
dot_b.place(x=10,y=175)
dot_b.bind("<Button-1>", lambda event: vect_dot_ans())

cross_b = tk.Label(window,text="Cross",bg=button_bg,width=vector_width,height=vector_height,font=vector_font)
cross_b.place(x=80,y=175)
cross_b.bind("<Button-1>", lambda event: vect_cross_ans())

vecta_b = tk.Label(window,text="Enter",bg=button_bg,width=vector_width,height=vector_height,font=vector_font)
vecta_b.place(x=470,y=130)
vecta_b.bind("<Button-1>", lambda event: vect_arith_ans())

vproj_b = tk.Label(window,text="V Proj",bg=button_bg,width=vector_width,height=vector_height,font=vector_font)
vproj_b.place(x=150,y=175)
vproj_b.bind("<Button-1>", lambda event: vect_vproj_ans())

sproj_b = tk.Label(window,text="S Proj",bg=button_bg,width=vector_width,height=vector_height,font=vector_font)
sproj_b.place(x=220,y=175)
sproj_b.bind("<Button-1>", lambda event: vect_sproj_ans())

#-------------------------------------------------------------------------------------------------------------------------------------------------------------------
#Matrices
#-------------------------------------------------------------------------------------------------------------------------------------------------------------------

#Define a function to turn a single string into a matrix
def create_mat(input_str):
    parts = input_str.split(',')
    result_array = [[float(num) for num in part.split()] for part in parts]
    return result_array

#Matrix 1
def get_m1():
    m1 = create_mat(m1_entry.get())
    return m1

m1_name = tk.Label(window, text="Matrix 1", bg=vector_bg, font=vector_font, width=vector_width, height=vector_height, foreground="white")
m1_name.place(x=10,y=190+30)

m1_entry = tk.Entry(window, width=75)
m1_entry.place(x=80, y=190+30)
m1_entry.bind("<Return>", get_m1)

#Matrix 2
def get_m2():
    m2 = create_mat(m2_entry.get())
    return m2

m2_name = tk.Label(window, text="Matrix 2", bg=vector_bg, font=vector_font, width=vector_width, height=vector_height, foreground="white")
m2_name.place(x=10,y=220+30)

m2_entry = tk.Entry(window, width=75)
m2_entry.place(x=80, y=220+30)
m2_entry.bind("<Return>", get_m2)

#Matrix 3
def get_m3():
    m3 = create_mat(m3_entry.get())
    return m3

m3_name = tk.Label(window, text="Matrix 3", bg=vector_bg, font=vector_font, width=vector_width, height=vector_height, foreground="white")
m3_name.place(x=10,y=250+30)

m3_entry = tk.Entry(window, width=75)
m3_entry.place(x=80, y=250+30)
m3_entry.bind("<Return>", get_m3)

#Matrix 4
def get_m4():
    m4 = create_mat(m4_entry.get())
    return m4

m4_name = tk.Label(window, text="Matrix 4", bg=vector_bg, font=vector_font, width=vector_width, height=vector_height, foreground="white")
m4_name.place(x=10,y=280+30)

m4_entry = tk.Entry(window, width=75)
m4_entry.place(x=80, y=280+30)
m4_entry.bind("<Return>", get_m4)

#Matrix arithmetic
def get_ma():
    ma = ma_entry.get()
    return ma

ma_name = tk.Label(window, text="M. Arith.", bg=vector_bg, font=vector_font, width=vector_width, height=vector_height, foreground="white")
ma_name.place(x=10,y=310+30)

ma_entry = tk.Entry(window, width=63)
ma_entry.place(x=80, y=310+30)
ma_entry.bind("<Return>", get_ma)

mata_b = tk.Label(window,text="Enter",bg=button_bg,width=vector_width,height=vector_height,font=vector_font)
mata_b.place(x=470,y=310+30)
mata_b.bind("<Button-1>", lambda event: mat_arith_ans())

#-------------------------------------------------------------------------------------------------------------------------------------------------------------------
#Functions to output matrix calculation results
#-------------------------------------------------------------------------------------------------------------------------------------------------------------------

def mat_arith_ans():
    output_entry.delete(0, tk.END)
    output_entry.insert(0, str(mat_arith(get_ma())))

def mat_det_ans():
    output_entry.delete(0, tk.END)
    output_entry.insert(0, str(mat_det()))

def mat_mul_ans():
    output_entry.delete(0, tk.END)
    output_entry.insert(0, str(mat_mul()))

#-------------------------------------------------------------------------------------------------------------------------------------------------------------------
#Matrix operations buttons
#-------------------------------------------------------------------------------------------------------------------------------------------------------------------

det_b = tk.Label(window,text="Det",bg=button_bg,width=vector_width,height=vector_height,font=vector_font)
det_b.place(x=10,y=355+30)
det_b.bind("<Button-1>", lambda event: mat_det_ans())

mul_b = tk.Label(window,text="Mult",bg=button_bg,width=vector_width,height=vector_height,font=vector_font)
mul_b.place(x=80,y=355+30)
mul_b.bind("<Button-1>", lambda event: mat_mul_ans())

#-------------------------------------------------------------------------------------------------------------------------------------------------------------------
#Symbolic integration
#-------------------------------------------------------------------------------------------------------------------------------------------------------------------

a, b, c, d, e, x, y, z = symbols('a b c d e x y z', real = True)
locals = {"a":a,"b":b,"c":c,"d":d,"e":e,"x":x,"y":y,"z":z}

#Retrieve function to integrate
def get_intg():
    intg_func, intg_var = list(map(str, intg_entry.get().split(',')))
    return intg_func, intg_var

#Integration button label
intg_name = tk.Label(window, text="Integrate", bg=vector_bg, font=vector_font, width=vector_width, height=vector_height, foreground="white")
intg_name.place(x=10,y=400+30)

#Integration entry section
intg_entry = tk.Entry(window, width=63)
intg_entry.place(x=80, y=400+30)
intg_entry.bind("<Return>", get_ma)

#Integration enter button
intga_b = tk.Label(window,text="Enter",bg=button_bg,width=vector_width,height=vector_height,font=vector_font)
intga_b.place(x=470,y=400+30)
intga_b.bind("<Button-1>", lambda event: comp_intg_ans())

#Function to compute integral
def comp_intg():
    intg_func, intg_var = get_intg()
    intg_func = sympify(intg_func, locals=locals)
    intg_var = sympify(intg_var, locals=locals)
    return integrate(intg_func,intg_var)

#Function to output results of integration calculation
def comp_intg_ans():
    output_entry.delete(0, tk.END)
    output_entry.insert(0, str(comp_intg()))
  
#-------------------------------------------------------------------------------------------------------------------------------------------------------------------
#Output field
#-------------------------------------------------------------------------------------------------------------------------------------------------------------------

output_name = tk.Label(window, text="Output:", bg=vector_bg, font=vector_font, width=vector_width, height=vector_height, foreground="white")
output_name.place(x=10,y=520)

output_entry = tk.Entry(window, width=75)
output_entry.place(x=80, y=520)

#-------------------------------------------------------------------------------------------------------------------------------------------------------------------
#Run
#-------------------------------------------------------------------------------------------------------------------------------------------------------------------

window.mainloop()
