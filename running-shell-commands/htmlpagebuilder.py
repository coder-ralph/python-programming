import os
from scriptheader import myheader

myheader("page builder")

# open then write or append contents to file
try:

    pagename = input("enter a name for your page:")
    file1 = open(pagename + ".html", "w")

    file1.write("""
    
    <html>
    <head>
    <title>test</title>
    </head>
    <body>
    can you see this?
    </body>
    </html>
    
    """)

except ValueError as ve:
    print(ve)