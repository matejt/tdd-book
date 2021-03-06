import random
from fabric.contrib.files import append, exists
from fabric.api import cd, env, local, run

REPO_URL = 'https://github.com/matejt/tdd-book.git'


def _get_latest_source():
    if exists('.git'):
        run('git fetch')
    else:
        run(f'git clone {REPO_URL} .')
    current_commit = local("git log -n 1 --format=%H, capture=True")
    run(f'git reset --hard {current_commit}')


def _update_and_activate_virtualenv():
    if not exists('venv/bin/pip'):
        run(f'virtualenv venv')
    run('. ./venv/bin/activate')
    run('pip install -r requirements.txt')


def _create_or_update_dotenv():
    append('.env', 'DJANGO_DEBUG_FALSE=y')
    append('.env', f'SITENAME={env.sitename}')
    append('.env', f'HOSTNAME={env.hostname}')
    current_content = run('cat .env')
    if 'DJANGO_SECRET_KEY' not in current_content:
        new_secret = ''.join(random.SystemRandom().choices('abcdefghijklmnopqrstuvwxyz0123456789', k=50))
        append('.env', f'DJANGO_SECRET_KEY={new_secret}')


def _update_static_files():
    run('python manage.py collectstatic --noinput')


def _update_database():
    run('python manage.py migrate --noinput')


def deploy():
    site_folder = f'/home/{env.user}/sites/{env.host}'
    run(f'mkdir -p {site_folder}')
    with cd(site_folder):
        _get_latest_source()
        _update_and_activate_virtualenv()
        _create_or_update_dotenv()
        _update_static_files()
        _update_database()
