from app import app, db

@app.shell_context_processor
def make_shell_context():
    return {'db': db}

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8081, debug=True)
    app.config['TEMPLATES_AUTO_RELOAD'] = True