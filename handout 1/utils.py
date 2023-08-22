import json
def extract_route(string):
    new_string = string.split('\n')[0].split(' ')[1]
    new_string = new_string.replace('/', '',1)
    return new_string

def read_file(path):
    file = open(path,"rb")
    return file.read()

def load_template(template):
    file = open("templates/"+ str(template), "r")
    return str(file.read())


def load_data(jso):
    with open(f'data/{jso}') as file:
        return json.loads(file.read())
        
def anota_json(params):
    with open("data/notes.json", "r+") as file:
        file_data = json.load(file)
        file_data.append(params)
        file.seek(0)
        json.dump(file_data, file, indent = 4)

def build_response(body = "", code = 200, reason = "OK", headers = ''):
    status_line = f'HTTP/1.1 {code} {reason}\n'
    response = f'{status_line}{headers}\n{body}'
    print("aqui --> ", response)
    return response.encode()