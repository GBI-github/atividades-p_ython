import cgi

form = cgi.FieldStorage()
nome = form.getvalue('nome')

print("Content-Type: text/html")
print()
print("<html>")
print("<head>")
print("    <title>Exemplo de Integração HTML, CSS e Python</title>")
print("    <link rel='stylesheet' type='text/css' href='style.css'>")
print("</head>")
print("<body>")
print("    <div class='container'>")
print("        <h1>Integração HTML, CSS e Python</h1>")
print("        <p>Ola, " + nome + "!</p>")
print("    </div>")
print("</body>")
print("</html>")