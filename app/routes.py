from flask import render_template, request, redirect, url_for
from app import app
from app.models import Recipe, session
from app.forms import RecipeForm
import os

UPLOAD_FOLDER = 'uploads'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

@app.route('/')
def index():
    recipes = session.query(Recipe).all()
    return render_template('index.html', recipes=recipes)

@app.route('/create', methods=['GET', 'POST'])
def create():
    form = RecipeForm()
    if form.validate_on_submit():
        name = form.name.data
        url = form.url.data
        description = form.description.data
        pdf = form.pdf.data
        if pdf:
            filename = pdf.filename
            pdf.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            pdf_path = filename
        else:
            pdf_path = None

        recipe = Recipe(name=name, url=url, description=description, pdf_path=pdf_path)
        session.add(recipe)
        session.commit()
        return redirect(url_for('index'))
    return render_template('create.html', form=form)

@app.route('/add_sample_data')
def add_sample_data():
    recipe1 = Recipe(name='Pizza', url='https://www.example.com/pizza', description='Delicious pizza recipe', pdf_path=None)
    recipe2 = Recipe(name='Pasta', url='https://www.example.com/pasta', description='Simple pasta recipe', pdf_path=None)
    session.add(recipe1)
    session.add(recipe2)
    session.commit()
    return redirect(url_for('index'))

@app.route('/recipe/<int:recipe_id>')
def recipe(recipe_id):
    recipe = session.query(Recipe).get(recipe_id)
    return render_template('recipe.html', recipe=recipe)