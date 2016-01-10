from os import environ as env, getcwd
from pdfkit import from_string as pdf_from_string, from_url as pdf_from_url, configuration as pdfkit_config

pdf_config = pdfkit_config(wkhtmltopdf=env.get('WKHTMLTOPDF_EXEC', '{}/bin/wkhtmltopdf-amd64'.format(getcwd())))

data = unicode(open('sample.html').read(), 'utf-8')
print pdf_from_string(data, 'test.pdf', configuration=pdf_config)
