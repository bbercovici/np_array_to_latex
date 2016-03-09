import numpy as np
from np_array_to_latex import np_array_to_latex

## Export an np.array to the bmatrix format
a = np.array(range(0,16)).reshape([4,4])
# a == [[ 0  1  2  3]
#    [ 4  5  6  7]
#    [ 8  9 10 11]
#    [12 13 14 15]]

np_array_to_latex(a,'a_to_latex')
# a_to_latex.tex:
# \begin{bmatrix}
# 0 & 1 & 2 & 3\\
# 4 & 5 & 6 & 7\\
# 8 & 9 & 10 & 11\\
# 12 & 13 & 14 & 15\\
# \end{bmatrix}






## Export a one-dimensional np.array to the bmatrix format,
# choosing between column vector or row vector format
b = a[0,:]
# b ==  [[0 1 2 3]

# column vector format
np_array_to_latex(b,'b_to_latex_column')
# b_to_latex_column.tex:
# \begin{bmatrix}
# 0\\
# 1\\
# 2\\
# 3\\
# 4\\
# 5\\
# \end{bmatrix}

# row vector format 
np_array_to_latex(b,'b_to_latex_row',column = False)
# b_to_latex_row.tex:
# \begin{bmatrix}
# 0 & 1 & 2 & 3
# \end{bmatrix}







## Export an np.array to the tabular format using column/row headers
c = a[0:2,:]
# c == [[0 1 2 3]
#  	  [4 5 6 7]]

np_array_to_latex(c,'c_to_latex_with_headers',row_headers = ['a','b'],column_headers = ['A','B','C','D'])
# c_to_latex_with_headers.tex:
# \begin{tabular}{|c|c|c|c|c|}
# \hline 
#   & A & B & C & D\\
# \hline 
# a & 0 & 1 & 2 & 3\\
# \hline 
# b & 4 & 5 & 6 & 7\\
# \hline 
# \end{tabular}

np_array_to_latex(c,'c_to_latex_with_column_headers',column_headers = ['A','B','C','D'])
# c_to_latex_with_column_headers.tex : 
# \begin{tabular}{|c|c|c|c|}
# \hline 
# A & B & C & D\\
# \hline 
# 0 & 1 & 2 & 3\\
# \hline 
# 4 & 5 & 6 & 7\\
# \hline 
# \end{tabular}

np_array_to_latex(c,'c_to_latex_with_row_headers',row_headers = ['a','b'])
# c_to_latex_with_row_headers.tex
# \begin{tabular}{|c|c|c|c|c|}
# \hline 
# a & 0 & 1 & 2 & 3\\
# \hline 
# b & 4 & 5 & 6 & 7\\
# \hline 
# \end{tabular}
