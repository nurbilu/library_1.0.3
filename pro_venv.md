# Change terminal : 
    use the "cmd" interpreter to run "virtual environment"  

# Create Virtual Environment :
   pip install virtualenv
   python -m virtualenv env
   env\scripts\activate
   deactivate
# Create Requirements:
   pip freeze > Requirements.txt

# Install if u clone it from git : 
   pip install -r Requirements.txt

# Install flask moudle : 
    pip install flask 

# Choose Interpreter Path :
    choose the path that have ('env':venv) in it
    
# Run Program: 
    if run by py file_name.py == can add in entry point : app.run(debug=True , port = "some 1K integer)
    or
    if run by flask run (if file_name == app) :write instead flask run --debug --port "sone 1K integer" 