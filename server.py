from wsgiref.simple_server import make_server
from urllib.parse import parse_qs


def form(env):
    return ['hi'.encode('UTF-8')]

route = {'form': form}


def battle_start(env, resp_start):
    resp_start('200 OK', [('Content-Type', 'text/html')])
    result = [b'']

    path = env.get('PATH_INFO', '/')[1:]
    parts = path.split('/')

    if len(parts) > 0 and parts[0]:
        fn = route.get(parts[0])
        if fn is not None:
            result = fn(env)
    else:
        with open('index.html', 'r') as file_html:
            with open('css/style.css', 'r') as file_css:
                style = file_css.read()
                result = [(file_html.read() % (style, )).encode('UTF-8')]
    return result


if __name__ == '__main__':
    s = make_server('', 8080, battle_start)
    s.serve_forever()
    s.shutdown()
