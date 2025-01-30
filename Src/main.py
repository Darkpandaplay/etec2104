import cherrypy
import mako.template
import mako.lookup
import os.path
import random
import quotes
import datetime

PYPATH = os.path.dirname(__file__)
lookup = mako.lookup.TemplateLookup(
    directories=[os.path.dirname(__file__)]
)
names = ["Alice","Bob","Carol","Dave"]

class App:
    @cherrypy.expose
    def quote(self):
        q = random.choice(quotes.quotations)
        t = lookup.get_template("quotes.html")
        return t.render(quote=q)

    @cherrypy.expose
    def index(self):
        n = random.choice(names)
        s = mako.template.Template(filename=f"{PYPATH}/../html/home.html")
        return s.render(Name=n)

    @cherrypy.expose
    def test(self):
        t = mako.template.Template(filename=f"{PYPATH}/../html/test.html")
        return t.render()
    
    @cherrypy.expose
    def posts(self):
        time = []
        view = []
        while (len(time)<15):
            x = datetime.timedelta(minutes=random.randrange(8000))
            hoursago = int( x.seconds / 3600 )
            minutesago = round( (x.seconds - hoursago*3600)/60 )
            time.append( f"{x.days} days, {hoursago} hours, and {minutesago} minutes ago" )
            view.append(random.randint(1,1000000))
        l = mako.template.Template(filename=f"{PYPATH}/../html/posts.html")
        return l.render(times=time,views=view)
    
    @cherrypy.expose
    def signup(self):
        e = mako.template.Template(filename=f"{PYPATH}/../Html/signup.html")
        return e.render(foobar=102)


srcdir = os.path.abspath(os.path.dirname(__file__))
app = App()
cherrypy.quickstart(
    app,
    '/',
    {
        "/Html": {
            "tools.staticdir.on": True,
            "tools.staticdir.dir": f"{srcdir}/../Html"
        }
    }
)