#from app import app, lm
#from app import socketio
from flask import request, redirect, render_template, url_for, flash
from flask.ext.wtf import Form
from wtforms import StringField
from wtforms.validators import DataRequired
import os
from flask import Flask

class TextForm(Form):
    """Login form to access writing and settings pages"""

    input_text = StringField('input_text', validators=[DataRequired()])
    



app = Flask(__name__)
app.secret_key="pict"
APP_ROOT = os.path.dirname(os.path.abspath(__file__))   # refers to application_top
APP_STATIC = os.path.join(APP_ROOT, 'static')

@app.route('/home',methods=['GET'])
def home_post():
	form=TextForm(csrf_enabled=False)
	return render_template('home.html',form=form)

@app.route('/home',methods=['POST'])
def checker():
	form=TextForm(csrf_enabled=False)
	text=form.input_text.data
	repeated_sentences=0
	text=text.split(". ")
	#text=list(text)
	print text
	files=['file1.txt','file2.txt','file3.txt']
	for x in files:
		print x
		with open(os.path.join(APP_STATIC, x)) as file1:
			file11=file1.read()
			file11=file11.split(". ")
		
			
			print file11
			for line1 in file11:
				line1=line1.replace(".\n","")
				line1=line1.replace(".","")
				line1=line1.replace("\n","")
				line1=line1.lower()
				for line2 in text:
				    line2=line2.replace(".\n","")
				    line2=line2.replace(".","")
				    line2=line2.replace("\n","")
				    line2=line2.lower()
				    if line1==line2:
					print line2+ " is repeated"
					repeated_sentences+=1
					print repeated_sentences
	if repeated_sentences==0:
		flash("Text not plagiarised",category="success")
	else:
		print "Text is plagiarised.\nApproximate plagiarism percentage: ",(float(repeated_sentences)/len(text))*100
		flash_text="Text is plagiarised.\nApproximate plagiarism percentage: "+ str((float(repeated_sentences)/len(text))*100)
		flash(flash_text,category="success")
	return render_template('home.html',form=form)

		
if __name__ == '__main__':
	app.run(debug = True)

