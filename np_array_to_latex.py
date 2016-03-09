import numpy as np
def np_array_to_latex(X,filename,row_headers = None,column_headers = None,
 column = True):
    '''
    Exports the np.array provided as argument to a latex file that can be imported
    By B.Bercovici (03/2016)
    Inputs:
    ------
    X : (N_row-by-N_column np.array) numpy array to export
    filename : (string) name of the file into which the converted 
    array is dumped (ex: filename = 'my_array' will result in my_array.tex)
    column_headers : (list of strings) column headers
    row_headers : (list of strings) row headers
    column : (boolean) True if one-dimensional arrays are displayed
    as column vectors, False otherwise
    '''

    ## Check the size and extract dimensions
    if len(X.shape) == 1:
        X = np.array([X])
        if column == True:
            X = X.T
            N_row = X.shape[0]
            N_column = 1
        else:
            N_row = 1
            N_column = X.shape[1]
    else:
        N_row = X.shape[0]
        N_column = X.shape[1]

    ## Generate the file line by line
    # The file is created first
    f = open(filename + '.tex','w')

    # If the np.array is exported as an array
    if (column_headers != None or row_headers != None):

        # The array header is generated
        style = ['|c' for x in range(N_column + (row_headers is not None))]
        style = ''.join([str(num) for num in style])
        style = style + '|'

        # Fetch the first two lines
        f.write(r'\begin{tabular}{' + style + '}'+'\n')
        f.write(r'\hline ' + '\n')

        # The rest of the array is written to the file
        for i in range(-1,N_row):
            for j in range(-1,N_column):
                # upper-left cell (outside array), with column and row headers
                if (i == -1 and j == - 1 and column_headers != None and row_headers != None ):
                    f.write(' ' + r' & ')
                # upper-left cell (outside array), column headers but no row headers
                elif (i == -1 and j == - 1 and column_headers != None ):
                    None
                # column header row (including the first out-of-array cell) up to the before last cell: 
                # column headers (if any) are written
                elif (i == -1 and j != N_column - 1 and column_headers != None):
                    f.write(column_headers[j] + r' & ')
                # last cell of column header row : the last column header (if any) is added along with and end-of-line character
                elif (i == -1 and j == N_column - 1 and column_headers != None):
                    f.write(column_headers[j] + r'\\' + '\n' +r'\hline ' + '\n' )
                # row header column is filled with row headers (if any)
                elif (i != -1 and j == -1 and row_headers != None):
                    f.write(row_headers[i] + r' & ' )
                # data is fetched to the array 
                elif ( i != -1 and j != -1 and j != N_column - 1):
                    f.write(str(X[i,j]) + r' & ')
                # when at the last data column, an end-of-line character is added
                elif ( i != -1 and j != -1 and j == N_column - 1  ):
                    f.write(str(X[i,j]) + r'\\' + '\n' +r'\hline ' + '\n' )
        f.write(r'\end{tabular}')


    # Else the array is simply exported as a bmatrix
    else:
        # Fetch the first two lines
        f.write(r'\begin{bmatrix}'+'\n')
        for i in range(N_row):
            for j in range(N_column):
                if (j == N_column - 1 and N_row != 1):
                    f.write(str(X[i,j]) + r'\\' + '\n' )
                elif (j == N_column - 1 and N_row == 1):
                    f.write(str(X[i,j]) + '\n' )
                else:
                    f.write(str(X[i,j]) + r' & ')
        f.write(r'\end{bmatrix}')

    f.close() 

