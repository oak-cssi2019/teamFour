from google.appengine.ext import ndb

class PokeSaved(ndb.Model):
    name =  ndb.StringProperty(required=True)
    picture =  ndb.StringProperty(required=True)
    ty1 = ndb.StringProperty(required=True)
    ty2 = ndb.StringProperty(required=True)
