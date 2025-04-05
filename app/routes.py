from flask import render_template, request, redirect, url_for, send_from_directory
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
            recipe = Recipe(name=name, url=url, description=description, pdf_path=None)
            session.add(recipe)
            session.commit()
            recipe_id = recipe.id
            recipe_folder = os.path.join(app.config['UPLOAD_FOLDER'], str(recipe_id))
            if not os.path.exists(recipe_folder):
                os.makedirs(recipe_folder)

            file_path = os.path.join(recipe_folder, filename)
            
            # Check for duplicate filenames
            base, ext = os.path.splitext(filename)
            counter = 1
            while os.path.exists(file_path):
                filename = f"{base}_new{counter}{ext}"
                file_path = os.path.join(recipe_folder, filename)
                counter += 1
            
            pdf.save(file_path)
            pdf_path = os.path.join(str(recipe_id), filename)
        else:
            pdf_path = None

        recipe = session.query(Recipe).get(recipe_id)
        recipe.pdf_path = pdf_path
        session.commit()
        return redirect(url_for('index'))
        return redirect(url_for('index'))
    return render_template('create.html', form=form)

@app.route('/recipe/<int:recipe_id>')
def recipe(recipe_id):
    recipe = session.query(Recipe).get(recipe_id)
    file_path = None
    if recipe and recipe.pdf_path:
        file_path = os.path.join(app.config['UPLOAD_FOLDER'], recipe.pdf_path)
    return render_template('recipe.html', recipe=recipe, file_path=file_path)

@app.route('/uploads/<path:filename>')
def download_file(filename):
    return send_from_directory('/home/stepan/Nextcloud/programovani/recepty-db/' + app.config['UPLOAD_FOLDER'], filename)