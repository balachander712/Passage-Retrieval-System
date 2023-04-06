import csv
import mysql.connector

# configure MySQL connection parameters
cnx = mysql.connector.connect(user='root', password='password',
                              host='localhost', database='test')


#open the TSV file
with open('test-queries.tsv', 'r') as tsvfile:
    reader = csv.reader(tsvfile, delimiter='\t')
    next(reader)  # skip header row

    # loop through the rows and insert into MySQL table
    for row in reader:
        cursor = cnx.cursor()
        query = """INSERT INTO test_queries (qid, query)
                   VALUES (%s, %s)"""
        cursor.execute(query, row)
        cnx.commit()

cnx.close()
