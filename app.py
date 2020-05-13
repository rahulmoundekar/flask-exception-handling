from flask import Flask, render_template, request, redirect, flash

app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
@app.route('/index', methods=['GET', 'POST'])
def my_method():
    try:
        print(1 / 0)
        return render_template("index.html")
    except Exception as e:
        return render_template('500.html'), 500


@app.errorhandler(404)
def not_found_error(error):
    return render_template('404.html'), 404


@app.errorhandler(500)
def internal_server_error(error):
    app.logger.error('Server Error: %s', error)
    return render_template('500.html'), 500


@app.errorhandler(Exception)
def unhandled_exception(e):
    app.logger.error('Unhandled Exception: %s', e)
    return render_template('500.html'), 500


# run always put in last statement or put after all @app.route
if __name__ == '__main__':
    app.run(host='localhost')
