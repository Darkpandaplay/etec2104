import cherrypy
import mako.template
import os.path

PYPATH = os.path.dirname(__file__)

class App:
    @cherrypy.expose
    def index(self):
        s = mako.template.Template(filename=f"{PYPATH}/../html/home.html")
        return s.render()

    @cherrypy.expose
    def test(self):
        t = mako.template.Template(filename=f"{PYPATH}/../html/test.html")
        return t.render(foobar=42)
    
    @cherrypy.expose
    def posts(self):
        l = mako.template.Template(filename=f"{PYPATH}/../html/posts.html")
        return l.render(foobar=100)

app = App()
cherrypy.quickstart(app)