#------------------------------------------------------------------------------
# Copyright (c) 2016, 2020, Oracle and/or its affiliates. All rights reserved.
#------------------------------------------------------------------------------

#------------------------------------------------------------------------------
# QueryArraysize.py
#
# Demonstrate how to alter the array size and prefetch rows value on a cursor
# in order to reduce the number of network round trips and overhead required to
# fetch all of the rows from a large table.
#------------------------------------------------------------------------------

import time
import cx_Oracle
import sample_env

connection = cx_Oracle.connect(sample_env.get_main_connect_string())

start = time.time()

cursor = connection.cursor()
cursor.prefetchrows = 1000
cursor.arraysize = 1000
cursor.execute('select * from bigtab')
res = cursor.fetchall()
# print(res)  # uncomment to display the query results

elapsed = (time.time() - start)
print("Retrieved", len(res), "rows in", elapsed, "seconds")
