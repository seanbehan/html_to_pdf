## HTML2PDF

This service will turn HTML into a PDF. There are two ways to generate a PDF.

- You can send a GET request to ./pdf?url=http://example.com/path-to/resource.
- You can send a POST request to ./pdf --data "<html>Hello World!</html>"

In both cases you will receive the PDF file in the response.

## Deploy to Heroku

## Installing wkhtmltopdf
This app requires the wkhtmltopdf binary. A binary is packaged with the app for deployment
to Heroku. If you're on a different platform you can download a binary of wkhtmltopdf from here
http://wkhtmltopdf.org/downloads.html. Plop it into the bin directory and set the
WKHTMLTOPDF_EXEC=./bin/the-bin-for-your-platform.
