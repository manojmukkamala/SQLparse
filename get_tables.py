sample_query = """SELECT * FROM     TableA a JOIN 'db'. 'sc'. 'TableB' b ON a.id = b.id 
JOIN ( SELECT id FROM  "sc". "TableC") d ON a.id = d.id 
LEFT JOIN db2 .sc2 .TableD;"""

sample_query = sample_query.upper()

query_tokens = sample_query.split()

indexes = []

for i in range(len(query_tokens)):

    if query_tokens[i] in ['FROM', 'JOIN']:

        indexes.append(i)
        
indexes

table_list = []

for j in indexes:
    
    if query_tokens[j-1] not in ['DAY', 'MONTH', 'YEAR']:

        if (query_tokens[j+1] not in ['(', 'SELECT', '(SELECT']):

#             #table_list = query_tokens[j+1].replace("\"", "")
            
#             table_name = query_tokens[j+1]
            
#             l =  table_name[-1]
            
#             f = query_tokens[j+2][0]
            
#             if l == '.':
            
#                 while l == '.':

#                     j += 1
#                     table_name = table_name + query_tokens[j+1]
#                     l =  table_name[-1]
            
#             if f == '.':
            
#                 while f == '.':

#                     j += 1
#                     table_name = table_name + query_tokens[j+1]
#                     print(table_name)
#                     f = query_tokens[j+2][0]
#                     print(f)

            a, b, c = query_tokens[j+1 : j+4]

            if (a[-1] == '.') or (b[0] == '.'): 
                t = a + b
                if (b[-1] == '.') or (c[0] == '.'):
                    t = t + c
            else:
                t = a
            
            print(t)
