from flask import Flask, render_template, request, jsonify
import json
from flask import Blueprint
from werkzeug.datastructures import ImmutableMultiDict 

views = Blueprint(__name__,"views")
def find_paths_to_name(data, name, path=''):
    print("path finder is called")
    paths = []
    if isinstance(data, dict):
        for key, value in data.items():
            new_path = f"{path}.{key}" if path else key
            if isinstance(value, (dict, list)):
                paths.extend(find_paths_to_name(value, name, new_path))
            elif value == name:
                paths.append(new_path)
    elif isinstance(data, list):
        for i, item in enumerate(data):
            if isinstance(item, dict) or isinstance(item, list):
                paths.extend(find_paths_to_name(item, name, f"{path}[{i}]"))
            elif item == name:
                paths.append(f"{path}[{i}]")
    return paths




@views.route("/", methods =["GET","POST"])
def index():
    paths=''
    name_to_find=''
    parsed_data={}
    if request.method =="POST":
        json_data = request.form['jsonData']
        key = request.form['key']
        name_to_find=key
        # Debugging: Print the received JSON data
        print("Received JSON data:", json_data)
        print("Received key data:", name_to_find)
        # Check if JSON data is empty
        if not json_data.strip():
            #data=json.loads(json_data)
            print("JSON data is empty")
            return render_template("index.html", msg="JSON data is empty")
        elif not name_to_find.strip():
            return render_template("index.html",keymsg="Please enter key to find")

        try:
            # Parse the JSON data
            parsed_data = json.loads(json_data)
            # Debugging: Print the parsed JSON data
            print("Parsed JSON data:", parsed_data)

            paths = find_paths_to_name(parsed_data, name_to_find)
            print(type(paths))
            if paths:
                result = f"All possible paths for:<b> {name_to_find}</b>:\n"
                for path in paths:
                    result += path + "\n"
                result=result.replace('\n','<p>')
                print(type(result))
            else:
                result = f"<b>{name_to_find}</b> not found in the JSON data."

            
            #return jsonify({'status': 'success', 'message': 'JSON is valid.'})
            return render_template("index.html",msg="JSON is valid",paths=result)
            
            # Continue processing the parsed JSON data...
            
        except json.JSONDecodeError as e:
            # Handle JSON parsing errors
            print("Error decoding JSON:", e)
            #return jsonify({'status': 'error', 'message': f'JSON is not valid: {str(e)}'})
            return render_template("index.html",msg="JSON is not valid")
    return render_template('index.html')    

@views.route('/personal')
def personal():
    return render_template('index1.html')