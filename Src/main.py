import cherrypy
import mako.template
import os.path

PYPATH = os.path.dirname(__file__)

class App:
    @cherrypy.expose
    def index(self):
        s = mako.template.Template(filename=f"{PYPATH}/../html/home.html")
        return s.render(Name="Matthew")

    @cherrypy.expose
    def test(self):
        t = mako.template.Template(filename=f"{PYPATH}/../html/test.html")
        return t.render(foobar=42)
    
    @cherrypy.expose
    def posts(self):
        l = mako.template.Template(filename=f"{PYPATH}/../html/posts.html")
        return l.render()
    
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