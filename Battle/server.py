from urllib.parse import parse_qs
from wsgiref.simple_server import make_server

from Battle import BattleField


def form(env):
    c = int(env.get('CONTENT_LENGTH', '0'))
    data = env['wsgi.input'].read(c)
    data = parse_qs(data)

    armies_number_ = int(data.get(b'arm_num')[0])
    strategy_ = str(data.get(b'strat')[0])
    strategy_ = strategy_[2:-1]
    squads_number_ = int(data.get(b'squad')[0])
    soldiers = int(data.get(b'sold')[0])
    vehicles = int(data.get(b'vehic')[0])

    with open('result.html', 'r') as file_html:
        with open('css/style.css', 'r') as file_css:
            style = file_css.read()
            if 5 <= soldiers + vehicles <= 10:
                battle = BattleField.BattleField(armies_number=armies_number_,
                                                 strategy=strategy_,
                                                 squads_number=squads_number_,
                                                 soldiers_number=soldiers,
                                                 vehicles_number=vehicles)

                a = 'Win army: ' + str(battle.start())
                result = [(file_html.read() %
                           (style, a,)).encode('UTF-8')]
            else:
                result = [(file_html.read() %
                           (style, 'Incorrect number of units.',)).encode('UTF-8')]
    return result

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
