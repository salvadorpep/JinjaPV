#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os
import jinja2
import webapp2


template_dir = os.path.join(os.path.dirname(__file__), "templates")
jinja_env = jinja2.Environment(loader=jinja2.FileSystemLoader(template_dir), autoescape=True)


class User():
    def __init__(self, name, lname, city, age, id):
        self.name = name
        self.lname = lname
        self.city = city
        self.age = age
        self.id = id

class BaseHandler(webapp2.RequestHandler):

    def write(self, *a, **kw):
        return self.response.out.write(*a, **kw)

    def render_str(self, template, **params):
        t = jinja_env.get_template(template)
        return t.render(params)

    def render(self, template, **kw):
        return self.write(self.render_str(template, **kw))

    def render_template(self, view_filename, params=None):
        # if params is None:
        #     params = {}
        template = jinja_env.get_template(view_filename)
        return self.response.out.write(template.render(params))


class MainHandler(BaseHandler):
    def get(self):
        params = {}
        return self.render_template("index.html", params=params)

class ProgramacioHandler(BaseHandler):
    def get(self):
        params = {}
        return self.render_template("programacio.html", params=params)

class EntradesHandler(BaseHandler):
    def get(self):
        params = {}
        return self.render_template("entrades.html", params=params)

class EspaiHandler(BaseHandler):
    def get(self):
        params = {}
        return self.render_template("espai.html", params=params)

class DadesHandler(BaseHandler):
    def get(self):
        params = {}
        return self.render_template("dades.html", params=params)

class AmicsHandler(BaseHandler):
    def get(self):
        params = {}
        return self.render_template("amics.html", params=params)

app = webapp2.WSGIApplication([
    webapp2.Route('/index', MainHandler),
    webapp2.Route("/programacio", ProgramacioHandler),
    webapp2.Route('/entrades', EntradesHandler),
    webapp2.Route('/espai', EspaiHandler),
    webapp2.Route("/dades", DadesHandler),
    webapp2.Route('/amics', AmicsHandler),
], debug=True)
