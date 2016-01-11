## HTML TO PDF

This webapp turns HTML into a PDF. There are two ways to generate a PDF.

- You can send a GET request to ./pdf?url=http://example.com
- You can send a POST request to ./pdf with the request body being the HTML you'd like to turn into a PDF.

This example uses the HTTPie Python command line tool. https://github.com/jkbrzt/httpie

```
http get localhost:5000/pdf?url=http://example.com

http post localhost:5000/pdf @sample.html
```

In both cases you will receive a PDF in the response.

## Deploy to Heroku

[![Deploy to Heroku](https://www.herokucdn.com/deploy/button.png)](https://heroku.com/deploy)

## Installing wkhtmltopdf

http://wkhtmltopdf.org/downloads.html

This app requires the wkhtmltopdf binary. If you install this app on Heroku, using the Heroku deploy button above, the `app.json`
will install the necessary buildpacks.

If you're running it somewhere else, you will have to install `wkhtmltopdf` and set the environment variable `WKHTMLTOPDF`. It has to point to the path of the binary.

For instance if you are on OSX and installing the wkhtmltopdf `.pkg`, it's probably at `/usr/local/bin/wkhtmltopdf`. You would then boot up a development server like so...

```
WKHTMLTOPDF=/usr/local/bin/wkhtmltopdf python app.py
```

## Demo

There is a demo available at http://htmltopdfdemo.herokuapp.com
