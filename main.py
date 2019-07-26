# the import section
import webapp2
import jinja2
import os
# import pokepy




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
          'q1': self.request.get('q1'),
          'q1correct': "Gen 1",
          'q2': self.request.get('q2'),
          'q2correct': "Black and White",
          'q3': self.request.get('q3'),
          'q3correct': "88",
          'q4': self.request.get('q4'),
          'q4correct': "Mew",
          'q5': self.request.get('q5'),
          'q5correct': "Bulbasaur",
          'q6': self.request.get('q6'),
          'q6correct': "Satoshi",
          'q7': self.request.get('q7'),
          'q7correct': "19",
          'q8': self.request.get('q8'),
          'q8correct': "Dialga",
          'q9': self.request.get('q9'),
          'q9correct': "Generation 2",
          'q10': self.request.get('q10'),
          'q10correct': "Max",
          'q11': self.request.get('q11'),
          'q11correct': "Dusknior"

           #stores form input named 'user-first-name' under key 'name' which is the same name as the placeholder on 'results.html'
          # 'feeling': self.request.get('user-feeling') #stores form input under 'user-feeling' under key 'feeling' which is the same name as the placeholder on 'results.html'
        }
        print(results_Dict)
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
        self.response.write(pokemon_template.render())
# the routes / app configuration section
app = webapp2.WSGIApplication([
  ('/home', HomeHandler),
  ('/about', AboutHandler),
  ('/results', ResultsHandler),
  ('/quiz',QuizHandler),
  ('/pokemon', PokemonHandler)
  ], debug=True)







# to spin your server, navigate to your parent folder and run in your terminal:
# dev_appserver.py app.yaml
# then go to http://localhost:8080 in your browser
# to stop your server, in your terminal press  control+C
