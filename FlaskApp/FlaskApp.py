#from flask import Flask, flash, redirect, render_template, request, session, abort
#app = Flask(__name__)

from flask import Flask, request, send_from_directory
# set the project root directory as the static folder, you can set others.
from os import getcwd

pages_subdir = "pages/"
images_subdir = "images/"
index_file_name = "TopicIndex.html"

app = Flask(__name__) #, static_url_path='')

@app.route('/')
def root():
    return send_from_directory(getcwd(), index_file_name)

@app.route('/'+pages_subdir+"<string:city_name_prefix>")
def transmit_city_data(city_name_prefix):
	return send_from_directory(getcwd()+'/'+pages_subdir, city_name_prefix+".html")

@app.route('/'+pages_subdir+images_subdir+"<string:image_file_name_prefix>")
def transmit_image(image_file_name_prefix):
	return send_from_directory(getcwd()+'/'+pages_subdir+images_subdir, image_file_name_prefix+".png")

if __name__ == "__main__":
	app.run()
