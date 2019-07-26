# the import section
import webapp2
import jinja2
import os
import json
import urllib2
import ast
# import pokepy

from poke_model import PokeSaved


# this initializes the jinja2 environment
the_jinja_env = jinja2.Environment(
  loader=jinja2.FileSystemLoader(os.path.dirname(__file__)),
  extensions=['jinja2.ext.autoescape'],
  autoescape=True)

# the handler section
class HomeHandler(webapp2.RequestHandler): #homepage "/"
    def get(self):
        home_template = the_jinja_env.get_template('templates/home.html') #pulls in "home.html" template
        # client = pokepy.V2Client()
        # print(client.get_pokemon(14))
        self.response.write(home_template.render()) #serves home.html template back to front-end

class AboutHandler(webapp2.RequestHandler):
    def get(self):
        about_template = the_jinja_env.get_template('templates/about.html')
        self.response.write(about_template.render())

class ResultsHandler(webapp2.RequestHandler):
    def get(self):
        # below are the form results from the form on home.html

        results_Dict = {
          'name': self.request.get('user-first-name'), #stores form input named 'user-first-name' under key 'name' which is the same name as the placeholder on 'results.html'
          'feeling': self.request.get('user-feeling') #stores form input under 'user-feeling' under key 'feeling' which is the same name as the placeholder on 'results.html'
        }
        results_template = the_jinja_env.get_template('templates/results.html')
        self.response.write(results_template.render(results_Dict)) #passes in results_Dict that will fill the placeholders on results.html

class QuizHandler(webapp2.RequestHandler):
    def get(self):
        quiz_template = the_jinja_env.get_template('templates/quiz.html')
        self.response.write(quiz_template.render())
        # raw_input("Who is jesus christ")

class PokemonHandler(webapp2.RequestHandler):
    def get(self):
        pokemon_template = the_jinja_env.get_template('templates/pokemon.html')
        var_dict={

            'savedPoke': ""
        }
        self.response.write(pokemon_template.render(var_dict))
    def post(self):
        p_name = self.request.get('currentPokemonName')
        p_pic = self.request.get('currentPokemonPic')
        p_ty1 = self.request.get('currentPokemonTY1')
        p_ty2 = self.request.get('currentPokemonTY2')
        # stringPoke = str(saved_p)
        # print(p_name)
        # print(p_pic)
        # print(p_ty1)
        # print(p_ty2)

        savedPoke = PokeSaved(name=p_name, picture=p_pic, ty1=p_ty1, ty2=p_ty2).put()


        #result = json.dumps(saved_p)
        #dict = ast.literal_eval(result)
        #myjson = json.loads(urllib2.unquote(dict))
        # print("pokemon saving....")
        #
        # job1 =json.dumps(saved_p)
        #
        #
        # print(job1)




class SavedHandler(webapp2.RequestHandler):
    def get(self):
        poke_saved = PokeSaved.query().fetch()
        saved_template = the_jinja_env.get_template('templates/saved_pokemon.html')
        self.response.write(saved_template.render({'poke_info' : poke_saved}))


# the routes / app configuration section
app = webapp2.WSGIApplication([
  ('/home', HomeHandler),
  ('/about', AboutHandler),
  ('/results', ResultsHandler),
  ('/pokemon', PokemonHandler),
  ('/saved', SavedHandler)
  ], debug=True)







# to spin your server, navigate to your parent folder and run in your terminal:
# dev_appserver.py app.yaml
# then go to http://localhost:8080 in your browser
# to stop your server, in your terminal press  control+C
