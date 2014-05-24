from flask import Flask, request, url_for, redirect
from flask import render_template
from forms import EqualeForm
import math
import logging      
from logging import FileHandler


app = Flask(__name__)
app.secret_key = 's3cr3t'
file_handler = FileHandler("debug.log","a")                                                                                             
file_handler.setLevel(logging.WARNING)
app.logger.addHandler(file_handler)


@app.route('/')
def index():
	return render_template('index.html')

@app.route('/equale', methods = ['GET', 'POST'])
def equale():
	form = EqualeForm()
	if form.validate_on_submit():
		a = str(form.number_a_field.data)
		b = str(form.number_b_field.data)
		c = str(form.basic_field.data)
		if c == '1':
			answer = math.log(int(b)) / math.log(int(a))
			decree = "log(%s)%s\n x = %s" % (a, b, answer)
		
		#return redirect('/equale' + '?number_a_field=' + str(form.number_a_field.data) + '?b_number_field=' + str(form.number_b_field.data) + '?basic_field=' + str(form.basic_field.data))
		return render_template('index.html', form=form, a=a, b=b, c=c, answer=answer, decree=decree)
	return render_template('index.html', form=form)

@app.route('/result/')
def result():
	return render_template('result.html')


@app.route('/example')
def example():
	return render_template('example.html')

if __name__ == '__main__':
	app.run(port=8023, use_reloader=True)
	app.debug = True
