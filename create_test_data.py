# import random

# # Open the TSV file for reading and writing
# with open('candidate-passages-top1000.tsv', 'r') as input_file, open('test_data.tsv', 'w') as output_file:
#     # Read the header row and add a new column header
#     header = input_file.readline().strip()
#     output_file.write(header + '\tnew_column\n')

#     # Iterate over each row in the input file
#     for line in input_file:
#         # Strip any whitespace from the line and split it into columns
#         columns = line.strip().split('\t')

#         # Generate a random value between 0 and 1 and add it as a new column
#         new_value = str(random.uniform(0, 1))
#         output_file.write(line.strip() + '\t' + new_value + '\n')

# Define the column names
col_names = ["qid", "pid", "queries", "passage", "relevancy"]
col_names_test_queries = ["qid", "queries"]

# Open the TSV file for reading and writing
with open('db/test-queries.tsv', 'r') as input_file, open('new_file.tsv', 'w') as output_file:
    # Read the header row and modify it to include the column names
    header = input_file.readline().strip()
    header = '\t'.join(col_names) + '\t' + header + '\n'
    output_file.write(header)

    # Iterate over each row in the input file
    for line in input_file:
        # Strip any whitespace from the line and split it into columns
        columns = line.strip().split('\t')

        # Write the new row to the output file with the column names
        output_file.write('\t'.join(columns) + '\n')