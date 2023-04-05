def print_operation_table(operation, num_rows=6, num_columns=6):
    # Print column headers
    print('{:>4}'.format(''), *('{:>4}'.format(j) for j in range(1, num_columns+1)))
    print('{:>5}'.format('-' * 6 * num_columns))

    # Print table
    for i in range(1, num_rows+1):
        print('{:>2} |'.format(i), *('{:>4}'.format(operation(i, j)) for j in range(1, num_columns+1)))


print_operation_table(lambda x,y: x**y, 4, 4)
print()
print_operation_table(lambda x,y: x*y)
