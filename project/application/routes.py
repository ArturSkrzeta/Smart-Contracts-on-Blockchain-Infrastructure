from flask import render_template, url_for, redirect, request
from application import app, db
from application.models import Block
from application.forms import BlockForm
import hashlib
from datetime import datetime

@app.route('/', methods=['GET', 'POST'])
def index():

    form = BlockForm()
    contracts_list = []

    blocks = Block.query.all()

    for block in blocks:
        contracts_list.append(block.contract)

    if form.contract.data in contracts_list:

        return render_template('index.html', blocks=blocks, form=form)

    if form.contract.data:

        _time = datetime.today().strftime('%Y-%m-%d-%H:%M:%S')
        _contract = form.contract.data
        _previous_hash = Block.query.all()[-1].contracts_so_far_hashed
        _contracts_so_far = _previous_hash + _contract
        _contracts_so_far_hashed = hashlib.sha256(_contracts_so_far.encode()).hexdigest()

        new = Block(time=_time, previous_hash=_previous_hash, contract=_contract, contracts_so_far_hashed=_contracts_so_far_hashed)

        db.session.add(new)
        db.session.commit()

        return redirect(url_for('index'))

    return render_template('index.html', blocks=blocks, form=form)


# Block(time=datetime.today().strftime('%Y-%m-%d-%H:%M:%S'), previous_hash="Open Contract", contract="Contract0001", contracts_so_far_hashed=hashlib.sha256("Contract0001".encode()).hexdigest())
