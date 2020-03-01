#!/usr/bin/python
#coding: utf-8
def index(req):
	req.content_type="text/html"
	req.write("""<!DOCTYPE html>
	<html lang="fr">
		<head>
		<title>Département R&amp;T de l'IUT de Villetaneuse</title>
		<meta charset="utf-8">
		<meta name="author" content="Adjutor Aimeric">
 		<link rel="stylesheet" type="text/css" href="STYLE.CSS">
		</head>
		<body>""")
	req.write("""<h1 id="Contact">Contact</h1>""")
	if (req.form["nom"]==""):
		req.write("Erreur : nom manquant!")
	if (req.form["question"]==""):
		req.write("Erreur : question manquante!")
	else:
		req.write("Merci " + req.form["nom"] + "! Votre message a bien été envoyé.")
		f= open("/home/student/905/11802407/public_html/M1106/question.txt","a")
		f.write(req.form["nom"] + ";" + req.form["statut"] + ";" + req.form["question"] + ";")
		f.close
	req.write("<a href=""http://localhost/~11802407/M1106/dut.html""><br/>Retour à l'acceuil</a>")

	req.write("""</body>
	</html>""")
