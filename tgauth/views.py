import json
import logging

from django.conf import settings
from django.contrib import auth
from django.core.urlresolvers import reverse
from django.http import HttpResponseNotFound, HttpResponseNotAllowed
from django.http import JsonResponse
from django.shortcuts import redirect
from django.views.decorators.csrf import csrf_exempt

from tgauth.auth import signer
from surfers.models import LatestPoint

logger = logging.getLogger(__name__)


@csrf_exempt
def botapi(request, token):
    if token != settings.TGAUTH_TOKEN:
        return HttpResponseNotFound()
    if request.method == 'POST':

        update = json.loads(request.body.decode(request.encoding or 'utf-8'))

        if 'message' in update:

            msg = update['message']

            if 'from' not in msg:
                logger.error("Got message from without 'from': %s", msg)
                return JsonResponse({
                    'method': 'sendMessage',
                    'chat_id': msg['chat']['id'],
                    'text': 'Что-то пошло не так, боту пришло сообщение из группы.',
                })

            if msg.get('text', '')[:1] == '/':
                cmd = msg['text']
                if cmd in COMMANDS:
                    try:
                        return COMMANDS[cmd](request, msg)
                    except:
                        logger.error("Can't process command %s:",
                                     msg['text'], exc_info=True)
                        return JsonResponse({
                            'method': 'sendMessage',
                            'chat_id': msg['chat']['id'],
                            'text': 'Something went wrong during %s command.' % cmd,
                        })
                else:
                    return JsonResponse({
                        'method': 'sendMessage',
                        'chat_id': msg['chat']['id'],
                        'text': 'No such command',
                    })
            elif 'location' in msg:
                return update_location(msg)

        else:
            logger.error("Unsupported update: %s", update)
    else:
        return HttpResponseNotAllowed()


def update_location(msg):

    user = auth.get_user_model().objects.get(msg['from']['username'])

    try:
        lp = LatestPoint.objects.get(user=user)
    except LatestPoint.DoesNotExists:
        lp = LatestPoint(user=user)

    l = msg['location']
    lp.point = 'POINT(%s %s)' % (l['longitude'], l['latitude'])
    lp.save()

    return JsonResponse({
        'method': 'sendMessage',
        'chat_id': msg['chat']['id'],
        'text': 'Ваше местоположение обновлено!',
    })


def start_cmd(request, msg):

    user_info = msg['from']

    if msg['chat']['type'] != 'private':
        return JsonResponse({
            'method': 'sendMessage',
            'chat_id': msg['chat']['id'],
            'text': 'Эта команда должна быть отправлена личным сообщением, '
                    'а не публично в группе.',
        })

    user, created = auth.get_user_model().objects.get_or_create(
        username=user_info['username']
    )

    reply = []

    if created:

        user.first_name = user_info['first_name']
        user.last_name = user_info.get('last_name')

        password = auth.get_user_model().objects.make_random_password()
        user.set_password(password)

        user.save()

        reply.append("Добро пожаловать в Sunsurfers Map! :pray:")
        reply.append("Для тебя создан новый аккаунт:")
        reply.append("Логин - %s" % user.username)
        reply.append("Пароль - %s" % password)
        reply.append("")

        return JsonResponse({
            'method': 'sendMessage',
            'chat_id': msg['chat']['id'],
            'text': '\n'.join(reply),
        })

    return JsonResponse({
        'method': 'sendMessage',
        'chat_id': msg['chat']['id'],
        'text': 'Какие люди! :-) Привет, @%s!' % user.username,
    })


def login_cmd(request, msg):

    user_info = msg['from']

    if msg['chat']['type'] != 'private':
        return JsonResponse({
            'method': 'sendMessage',
            'chat_id': msg['chat']['id'],
            'text': 'Эта команда должна быть отправлена личным сообщением, '
                    'а не публично в группе.',
        })

    user = auth.get_user_model().objects.get(username=user_info['username'])

    reply = []
    reply.append("Ссылка для входа на сайт (действует 10 минут):")
    reply.append("https://{domain}{url}".format(
        domain=settings.TGAUTH_DOMAIN,
        url=reverse(
            "login", args=(signer.sign(user.username),)
        )
    ))

    return JsonResponse({
        'method': 'sendMessage',
        'chat_id': msg['chat']['id'],
        'text': '\n'.join(reply),
    })


COMMANDS = {
    '/login': login_cmd,
    '/start': start_cmd,
}


def login(request, token):
    auth.login(request, auth.authenticate(token=token))
    return redirect('/')
