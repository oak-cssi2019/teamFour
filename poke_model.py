from google.appengine.ext import ndb

class PokeSaved(ndb.Model):
    pokemon_id =  ndb.StringProperty(required=True)
    pokemon_picture =  ndb.StringProperty(required=True)

    pokemon_speed =  ndb.StringProperty(required=True)
    pokemon_speed_value =  ndb.IntegerProperty(required=True)

    pokemon_sd =  ndb.StringProperty(required=True)
    pokemon_sd_value =  ndb.IntegerProperty(required=True)

    pokemon_sa =  ndb.StringProperty(required=True)
    pokemon_sa_value =  ndb.IntegerProperty(required=True)

    pokemon_hp =  ndb.StringProperty(required=True)
