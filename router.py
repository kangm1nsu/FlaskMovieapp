from flask import Flask
from flask.templating import render_template
import movie_api as ma
import weather as wa

app = Flask(__name__)

@app.route("/")
def index():
    
      return render_template( "index.html", movies= ma.callMovieApi(), weather = wa.callWeather())

      
if __name__ == "__main__":
    app.run(debug=True)