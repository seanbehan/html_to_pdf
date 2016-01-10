from flask import Flask, request, send_file, jsonify
from pdfkit import from_string as pdf_from_string, from_url as pdf_from_url
from uuid import uuid4
from os import environ as env, getcwd
from os.path import basename, exists

app = Flask(__name__)

@app.route("/")
def home():
    return """<html><h3>PDF From HTML</h3><form action='/pdf'><input size=100 type='text' name='source' placeholder='Enter a valid URL to get a PDF'/><button onclick='this.innerHTML=Submitted'>Go</button></form></body></html>"""

@app.route("/pdf", methods=["GET"])
def make_pdf_from_url():
    pdf_file = '{}/pdfs/{}.pdf'.format(getcwd(), str(uuid4()))
    source = str(request.args.get('url'))

    try:
        pdf_from_url(source, pdf_file)
    except:
        return "We were unable to make a PDF from this url."

    return send_file(pdf_file, as_attachment=False)

@app.route("/pdf", methods=["POST"])
def make_pdf_from_html():
    pdf_file = '{}/pdfs/{}.pdf'.format(getcwd(), str(uuid4()))

    try:
        pdf_from_string(unicode(request.data, 'utf-8'), pdf_file)
    except:
        pass

    if exists(pdf_file):
        return send_file(pdf_file, as_attachment=True)

    return "We were unable to make a PDF for you."

if __name__=='__main__':
    app.run(debug=True)
