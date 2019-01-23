import numpy as np

def np_array_to_latex(X,
    filename,
    row_headers = None,
    column_headers = None,
 column = True,
 type = 'f', 
 decimals = 2, 
 ante_decimals = 6,
 is_symmetric = "no"):
    '''
    Exports the np.array provided as argument to a latex file that can be imported
    By B.Bercovici (03/2016)
    Inputs:
    ------
    - X : (N_row-by-N_column np.array) numpy array to export
    - filename : (string) name of the file into which the converted 
    array is dumped (ex: filename = 'my_array' will result in my_array.tex)
    - column_headers : (list of strings) column headers
    - row_headers : (list of strings) row headers
    - column : (boolean) True if one-dimensional arrays are displayed
    as column vectors, False otherwise
    - type : (string) Format type. 'f' for float or 'e' for scientific exponent notation
    - decimals : (integer) Number of decimals
    - ante_decimants : (integer) Number of ante-decimal digits
    - is_symmetric : 
    -- "no" : self explanatory, all components are saved.
    -- "upper" : symmetric, will only save upper triangular component
    -- "lower" : symmetric, will only save lower triangular component

    '''
    ## Format specifier
    format_string = '{:' + str(ante_decimals) + '.' + str(decimals) + str(type) + '}'
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

        # Write the first two lines
        f.write(r'\begin{tabular}{' + style + '}'+'\n')
        f.write(r'\hline ' + '\n')

        # The rest of the array is written to the file
        for i in range(-1,N_row):
            for j in range(-1,N_column):

                formatted_number = format_string.format(X[i,j])
                split_number = formatted_number.split("e")
                
                if len(split_number) != 1:
                    exponent = str(int(split_number[1].split("+")[-1]))
                    if (int(exponent) != 0):

                        formatted_number = split_number[0] + r"\cdot 10^{" + exponent +"}"
                    else:
                        formatted_number = split_number[0]



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
                        
                    if is_symmetric == "no":
                        f.write(formatted_number + r' & ')
                    else:
                        if (is_symmetric == "upper"):
                            if (i <= j):
                                f.write(formatted_number + r' & ')
                            else:
                                f.write(r"\cdot" + r' & ')
                        elif (is_symmetric == "lower"):
                            if (i >= j):
                                f.write(formatted_number + r' & ')
                            else:
                                f.write(r"\cdot" + r' & ')



                # when at the last data column, an end-of-line character is added
                elif ( i != -1 and j != -1 and j == N_column - 1  ):

                    if is_symmetric == "no":
                        f.write(formatted_number + r'\\' + '\n' +r'\hline ' + '\n')
                    else:
                        if (is_symmetric == "upper"):
                            if (i <= j):
                                f.write(formatted_number + r'\\' + '\n' +r'\hline ' + '\n')
                            else:
                                f.write(r"\cdot" + r'\\' + '\n' +r'\hline ' + '\n')
                        elif (is_symmetric == "lower"):
                            if (i >= j):
                                f.write(formatted_number + r'\\' + '\n' +r'\hline ' + '\n')
                            else:
                                f.write(r"\cdot" + r'\\' + '\n' +r'\hline ' + '\n')

        f.write(r'\end{tabular}')


    # Else the array is simply exported as a bmatrix
    else:

        if (min(X.shape) == 1):
            matrix_type = "pmatrix"
        else:
            matrix_type = "bmatrix"




        f.write(r'\begin{'+ matrix_type +'}'+'\n')
        for i in range(N_row):
            for j in range(N_column):

                formatted_number = format_string.format(X[i,j])
                split_number = formatted_number.split("e")
                
                if len(split_number) != 1:
                    exponent = str(int(split_number[1].split("+")[-1]))
                    if (int(exponent) != 0):

                        formatted_number = split_number[0] + r"\cdot 10^{" + exponent +"}"
                    else:
                        formatted_number = split_number[0]


                if (j == N_column - 1 and N_row != 1):


                    if is_symmetric == "no":
                        f.write(formatted_number + r'\\' + '\n' )
                    else:
                        if (is_symmetric == "upper"):
                            if (i <= j):
                                f.write(formatted_number + r'\\' + '\n' )
                            else:
                                f.write(r"\cdot" + r'\\' + '\n' )
                        elif (is_symmetric == "lower"):
                            if (i >= j):
                                f.write(formatted_number + r'\\' + '\n' )
                            else:
                                f.write(r"\cdot"+ r'\\' + '\n' )



                elif (j == N_column - 1 and N_row == 1):

                    if is_symmetric == "no":
                        f.write(formatted_number + '\n' )
                    else:
                        if (is_symmetric == "upper"):
                            if (i <= j):
                                f.write(formatted_number + '\n' )
                            else:
                                f.write(r"\cdot" + '\n' )
                        elif (is_symmetric == "lower"):
                            if (i >= j):
                                f.write(formatted_number + '\n' )
                            else:
                                f.write(r"\cdot"+ '\n' )



                else:
                    # f.write(str(X[i,j]) + r' & ')

                    if is_symmetric == "no":
                        f.write(formatted_number + r' & ')
                    else:
                        if (is_symmetric == "upper"):
                            if (i <= j):
                                f.write(formatted_number + r' & ')
                            else:
                                f.write(r"\cdot" + r' & ')
                        elif (is_symmetric == "lower"):
                            if (i >= j):
                                f.write(formatted_number + r' & ')
                            else:
                                f.write(r"\cdot"+ r' & ')



        f.write(r'\end{'+ matrix_type +'}'+'\n')

    f.close() 
