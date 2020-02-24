#!/usr/bin/env python3
import cgi
form=cgi.FieldStorage()
u_name=form.getvalue("name")
html = """
  <html lang="en"> 
    <body>
    <p>
      Hello, %s!
      </p>
    </body>
</html>
""" % u_name
print(html)