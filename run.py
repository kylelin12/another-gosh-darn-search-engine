from flask import Flask, render_template, session, redirect, url_for, request, flash

run = Flask(__name__)

@run.route('/')
def route_root():
    return render_template('home.html')

@run.route('/about')
def route_about():
    return render_template('about.html')

@run.route('/getresults')
def route_getresults():
    search_type = request.form["search-dest"]
    search = request.form["search-term"]
    ret = []
    if search_type == 'google':
        ret = google.search(search)
    if search_type == 'tastedive':
        ret = tastedive.search(search)
    if search_type == 'youtube':
        ret = youtube.search(search)
    if search_type == 'news':
        ret = news.search(search)
    return redirect( url_for(route_results) , result = ret, search_type = search_type)

@run.route('/results')
def route_results():
    if search_type == 'google':
        return render_template('google.html', result = result)
    if search_type == 'tastedive':
        return render_template('tastedive.html', result = result)
    if search_type == 'youtube':
        return render_template('youtube.html', result = result)
    if search_type == 'news':
        return render_template('news.html', result = result)

if __name__ == "__main__":
    run.debug = True
    run.run()
