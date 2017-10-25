from flask import Flask, request, send_file, jsonify
from uuid import uuid4
from os import environ as env, getcwd, system
from os.path import basename, exists
from flask_cors import CORS, cross_origin

WKHTMLTOPDF = env.get('WKHTMLTOPDF', '{}/bin/wkhtmltopdf'.format(getcwd()))

app = Flask(__name__)
CORS(app)



def make_pdf(source=''):
    pdf_file = '{}/pdfs/{}.pdf'.format(getcwd(), str(uuid4()))

    if source.startswith('http'):
        system('%s %s %s' % (WKHTMLTOPDF, source, pdf_file))
        return pdf_file

    source_file = '{}/pdfs/{}.html'.format(getcwd(), str(uuid4()))
    with open(source_file, 'w') as f:
        f.write(source)
    system('%s %s %s' % (WKHTMLTOPDF, source_file, pdf_file))
    return pdf_file

@app.route("/")
def home():
    return """<html>
    <h3>PDF From HTML</h3>
    <form action='/pdf'>
    <input size=100 type='text' name='url' placeholder='Enter a valid URL to get a PDF'/>
    <button>Go</button>
    </form></body></html>"""

@app.route("/pdf", methods=["GET"])
def make_pdf_from_url():
    source = str(request.args.get('url'))
    pdf_file = make_pdf(source)
    return send_file(pdf_file, as_attachment=False)

cross_origin(["www.pawsquad.com", "martinwork.eu.ngrok.io"])
@app.route("/pdf", methods=["POST"])
def make_pdf_from_html():
    source = unicode(request.data, 'utf-8')
    print source
    pdf_file = make_pdf(source)

    return send_file(pdf_file, as_attachment=True)

if __name__=='__main__':
    app.run(debug=True)
