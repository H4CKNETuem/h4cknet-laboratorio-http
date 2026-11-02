"""AURORACORP V3 — INTENTIONALLY VULNERABLE LOCAL TRAINING APP.
No real employee data; no public deployment. Authorization flaw confined to /api/profile.
"""
import hashlib
import os
from functools import wraps
from flask import Flask, jsonify, redirect, render_template, request, session, url_for

app = Flask(__name__)
app.secret_key = os.environ.get('LAB_SESSION_SECRET', 'dev-ONLY-not-production')
app.config.update(SESSION_COOKIE_HTTPONLY=True, SESSION_COOKIE_SAMESITE='Lax')

FIRST = ['Alex','Marta','David','Lucía','Inés','Sergio','Laura','Pablo','Elena','Hugo','Irene','Nora','Raúl','Clara','Diego','Eva','Daniel','Alba','Javier','Ana']
LAST = ['Moreno','Díaz','López','Vidal','Castro','Ruiz','Santos','Martín','Ramos','Gil']
DEPARTMENTS = ['Soporte','Operaciones','Finanzas','Legal','Producto','Infraestructura','Logística','Atención al cliente','RRHH','Marketing']
FLAG = 'H4CKNET{AURORA_200_IDOR_SHA256_ADMIN}'

def digest(value):
    return hashlib.sha256(value.encode('utf-8')).hexdigest()

# Exactly 200 preloaded fictitious personnel IDs: 100..299.
# No public signup; employee accounts are preloaded only.
USERS = {}
for uid in range(100, 300):
    n = uid - 100
    name = FIRST[n % len(FIRST)]
    surname = LAST[(n // len(FIRST) + n % len(LAST)) % len(LAST)]
    username = f'{name.lower().replace("ú", "u").replace("í", "i")}{uid}'
    password = f'Aurora-{uid}-local!'  # synthetic; never real credentials
    USERS[uid] = dict(username=username, name=f'{name} {surname}', department=DEPARTMENTS[n % len(DEPARTMENTS)],
                      role='Empleado', email=f'{username}@auroracorp.test', password_hash=digest(password))
# Publicly leaked account is a story entry point, not the goal.
USERS[101].update(username='alex', name='Alex Moreno', password_hash=digest('bienvenido1'))
# Admin in a high ID, not the next account (to encourage investigation, not blind guessing).
USERS[299].update(username='n.salazar', name='Nuria Salazar', department='Dirección', role='Administrador',
                  password_hash=digest('aurora2026!'))


def who():
    return USERS.get(session.get('uid'))

def login_required(fn):
    @wraps(fn)
    def wrapper(*a, **kw):
        if not who():
            if request.path.startswith('/api/'):
                return jsonify(error='Debes iniciar sesión.'), 401
            return redirect(url_for('login'))
        return fn(*a, **kw)
    return wrapper

@app.after_request
def headers(res):
    res.headers['Cache-Control'] = 'no-store'
    res.headers['X-Content-Type-Options'] = 'nosniff'
    return res

@app.route('/')
def home():
    return redirect(url_for('workspace')) if who() else redirect(url_for('login'))

@app.route('/login', methods=['GET', 'POST'])
def login():
    error = None
    if request.method == 'POST':
        username = request.form.get('username', '').strip().lower()
        password = request.form.get('password', '')
        found = next(((uid, u) for uid, u in USERS.items()
                      if u['username'] == username and u['password_hash'] == digest(password)), None)
        if found:
            session.clear()
            session['uid'] = found[0]
            return redirect(url_for('workspace'))
        error = 'Credenciales incorrectas.'
    return render_template('login.html', me=who(), error=error, page='login')

@app.route('/logout', methods=['POST'])
def logout():
    session.clear()
    return redirect(url_for('home'))

@app.route('/workspace')
@login_required
def workspace():
    return render_template('workspace.html', me=who(), page='workspace')

@app.route('/documentos')
@login_required
def documents():
    return render_template('docs.html', me=who(), page='documentos')


@app.route('/novedades')
@login_required
def news():
    return render_template('news.html', me=who(), page='novedades')

@app.route('/soporte')
@login_required
def support():
    return render_template('support.html', me=who(), page='soporte')

@app.route('/perfil')
@login_required
def profile():
    return render_template('profile.html', me=who(), uid=session['uid'], page='perfil')

@app.route('/api/profile', methods=['POST'])
@login_required
def api_profile():
    payload = request.get_json(silent=True)
    if not isinstance(payload, dict) or type(payload.get('user_id')) is not int:
        return jsonify(error='Se requiere JSON con user_id entero.'), 400
    uid = payload['user_id']
    u = USERS.get(uid)
    if not u:
        return jsonify(error='Expediente inexistente.'), 404
    # VULNERABILITY: authN is checked, but authZ for target uid is not!
    # Hash exposure is intentional, exclusively for an isolated offline lab.
    return jsonify(id=uid, username=u['username'], name=u['name'], email=u['email'],
                   department=u['department'], role=u['role'], password_hash=u['password_hash'], hash_type='sha256')

@app.route('/archivo-direccion')
@login_required
def vault():
    if who()['role'] != 'Administrador':
        return render_template('restricted.html', me=who(), page='archivo'), 403
    return render_template('vault.html', me=who(), page='archivo', flag=FLAG)

@app.errorhandler(404)
def notfound(exc):
    return render_template('notfound.html', me=who()), 404
