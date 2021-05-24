import mysql.connector
import re
from mysql.connector import FieldType

TAG_HTML = "html"
TAG_TD = "td"
TAG_TR = "tr"
TAG_BODY = "body"
TAG_PAR = "p"
TAG_HEAD = "head"
TAG_TABLE = "table"
TAG_TH = "th"
TAG_LINK = "link"
TAG_H1 = "h1"

def create_element(tag, content, endtag=True):
    if not endtag:
        m = '<' + tag + '>' + content + '</' + tag + '\n'
    else:
        m = '<'+tag+'>'+content+'</'+tag+'>'+'\n'
    return m

def create_element_table(tag, list_content):
    message = ''
    for content in list_content:
        m = '<'+tag+'>'+content+'</'+tag+'>'+'\n'
        message += m
    return message

def create_table(content_dict):
    rows_info = []
    for index in content_dict:
        row = create_element_table(index[0], index[1])
        rows_info += [row]
    rows = create_element_table(TAG_TR, rows_info)
    table = create_element(TAG_TABLE, rows)
    return table

def create_html(head_info, table_info, file_name):

    doc_type = '<!DOCTYPE html>'

    link = '<link rel="stylesheet" href="../static/website_style.css" >'
    title = '<title>Israeli Government</title>'
    meta = '<meta charset="UTF-8"><meta name="viewport" content="width=device-width, initial-scale=1">'

    head = create_element(TAG_HEAD, link + title + meta)
    h1 = create_element(TAG_H1, head_info)

    title = '<div class="header"><h1>Israeli Government</h1> </div>'

    option_bar = '<div class ="topnav" ><a href="/">Home</a><a href="../search">View</a><a href="../create">Create</a><a href="../update">Update</a><a href="../delete">Delete</a>  <a href="../select">Select</a></div>'
    body = create_element(TAG_BODY, title + option_bar + h1 + table_info)

    message = create_element(TAG_HTML, head+body)
    message = doc_type + message
    return message

# Inner function for printing a table when the query is a select statement:
def print_table(cursor, head_info, cssFileName, f=None, opt="C"):
    colName = []
    format_strings = []

    num_cols = len(cursor.description)
    col_widths = [20] * num_cols

    # Get all the collumn names:
    for i in range(num_cols):
        desc = cursor.description[i]
        colName.append(str(desc[0]))

    # Format the columns and print the column names:
    if opt == "H":
        info = []
    for i in range(len(cursor.description)):
        desc = cursor.description[i]
        format_string = "{:<" + str(col_widths[i]) + "}"
        format_strings.append(format_string)
        if opt == "F":
            f.write(format_strings[i].format(colName[i])+"|")
        if opt == "H":
            info += [colName[i]]
        else:
            print(format_strings[i].format(colName[i]), "|", end="")
    print()

    if opt == "H":
        outputTH = (TAG_TH, info)


    # Print a dashed line under the column names:
    ttl_width = sum(col_widths) + 2 * num_cols
    output = "-" * ttl_width
    if opt == "F":
        f.write(output + '\n')
    elif opt == "C":
        print(output)

    if opt == "H":
        outputHTML = (outputTH,)
    # Print each row in the table:
    for row in cursor:
        if opt == "H":
            info = []
        for i in range(num_cols):
            if isinstance(row[i], bytes):
                cur = row[i].decode("utf-8")
                if opt == "F":
                    f.write(format_strings[i].format(cur) + "|")
                elif opt == "H":
                    info += [str(cur)]
                else:
                    print(format_strings[i].format(cur), "|", end="")
            else:
                if opt == "F":
                    f.write(format_strings[i].format(row[i]) + "|")
                elif opt == "H":
                    info += [str(row[i])]
                else:
                    print(format_strings[i].format(row[i]), "|", end="")
        if opt == "F":
            f.write( '\n')
        elif opt == "H":
            outputHTML+=((TAG_TD, info),)
            info = []
        elif opt == "C":
            print()

    # Print another dashed line:
    output = "-" * ttl_width
    if opt == "F":
        f.write(output+ '\n')
    elif opt == "H":
        x = create_table(outputHTML)
        website = create_html(head_info, x, cssFileName)
        f.write(website)
        f.close()
    else:
        print(output)




# Inner function for running each query.
# Print the query number, query text and result/table:
def run_query(cursor, query, query_num, opt="C"):
    f = None
    if query != "":
        if opt == "F":
            # Open a html file for writing:
            filename = "/Users/esteebrooks/Documents/DatabaseSystems/FinalProject/Query" + str(query_num)
            f = open(filename, 'w')
            #f.write("Query number:" + str(query_num) + '\n')
            f.write("Query text:\n" + str(query) + '\n')

        elif opt == "H":
            filename = "/Users/esteebrooks/PycharmProjects/FinalWebsite/templates/" + str(query_num) + ".html"
            # change the option to file because it is the same from now on for HTML files:
            f = open(filename, 'w')
            #header_info = "Query number: " + str(query_num) + "<br>Query text:<br>" + str(query) + '\n'
            header_info = "Query text:<br>" + str(query) + '\n'

            cssFileName = str(query_num)

        else:
            print("Query number:", query_num)
            print("Query text:\n", query)

        try:
            result = cursor.execute(query)
            if query.lower().startswith("select"):
                print_table(cursor, header_info, cssFileName, f, opt)

            else:
                # If there is no table, just print the result,
                # either to a file or to the console:
                if opt == "F" or opt == "H":
                    if result:
                        f.write(result)
                    else:
                        f.write("None")
                    f.close()
                else:
                    print(result)

        except mysql.connector.Error as e:
            if opt == "F" or opt == "H":
                f.write("SQL ERROR" + str(e)+'\n')
                f.write('\n')
            else:
                print("SQL ERROR", e)
                print()
        f.close()


# Outer function. Remove comments and split up the querys:
def run_sql_file(fileName, conn, opt="C"):
    conn = mysql.connector.connect(host="localhost", user="root", passwd="Lokshon1!", database="ISGOV3")
    cursor = conn.cursor()

    file = open(fileName)
    sql = file.read()
    # Remove comments:
    noComments = re.sub(r'/\*\n?.*\n?.*\n?\*\/', ' ', sql)
    queries = noComments.split(';')
    count = 1
    for query in queries:
        query = query.strip()
        run_query(cursor, query, count, opt)
        count += 1

    file.close()



# Test the functions using a real file:
#def main():
    #conn = mysql.connector.connect(host="localhost", user="root", passwd="Lokshon1!", database="ISGOV2")
    #run_sql_file("/Users/esteebrooks/Documents/DatabaseSystems/FinalProject/select_government.sql", conn, "H")
    # Run the functions with the 'COMP3563_Spring2021_UnivDB_SQL' public document:
    #conn = mysql.connector.connect(host="localhost",user="root",passwd="Lokshon1!",database="UDB#")
    # run_sql_file("/Users/esteebrooks/Documents/DatabaseSystems/hw6testqueries.sql", conn)
    # conn.close()

    # Run the functions on some of my own queries:
   # conn = mysql.connector.connect(host="localhost", user="root", passwd="Lokshon1!", database="ISGOV2")
    #run_sql_file("/Users/esteebrooks/Documents/DatabaseSystems/rectitation03:05:21.sql", conn, "F")
    #run_sql_file("/Users/esteebrooks/Documents/DatabaseSystems/rectitation03:05:21.sql", conn, "C")


    #conn.close()


#main()

