from utils import load_data, load_template, anota_json, build_response
import urllib.parse

def index(request):
    # A string de request sempre começa com o tipo da requisição (ex: GET, POST)
    print("OLHA ISSO")
    if request.startswith('POST'):
        print("ENTROU ENTROU ENTROU")
        request = request.replace('\r', '')  # Remove caracteres indesejados
        # Cabeçalho e corpo estão sempre separados por duas quebras de linha
        partes = request.split('\n\n')
        corpo = partes[1]
        params = {}
        # Preencha o dicionário params com as informações do corpo da requisição
        # O dicionário conterá dois valores, o título e a descrição.
        # Posteriormente pode ser interessante criar uma função que recebe a
        # requisição e devolve os parâmetros para desacoplar esta lógica.
        # Dica: use o método split da string e a função unquote_plus
        for chave_valor in corpo.split('&'):
            cv = urllib.parse.unquote_plus(chave_valor)
            if "titulo" in chave_valor:
                params["titulo"] = chave_valor[7:]
            if "detalhes" in chave_valor:
                params['detalhes'] = chave_valor[9:]
        anota_json(params)
        return build_response(code = 303, reason = 'See Other', headers = 'Location: /')

    # O RESTO DO CÓDIGO DA FUNÇÃO index CONTINUA DAQUI PARA BAIXO...

    note_template = load_template('components/note.html')
    notes_li = [
        note_template.format(title = dados['titulo'], details = dados['detalhes'])
        for dados in load_data('notes.json')
    ]
    notes = '\n'.join(notes_li)
    body = load_template('index.html').format(notes = notes)
    return build_response(body=body)