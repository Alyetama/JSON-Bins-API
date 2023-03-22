#!/usr/bin/env python
# coding: utf-8

import argparse
import json
import secrets
import sqlite3
import string

from flask import Flask, jsonify, request

app = Flask(__name__)

alphabet = string.ascii_letters + string.digits + '-_'


def generate_id(length=12):
    return ''.join(secrets.choice(alphabet) for i in range(length))


@app.route('/bins', methods=['POST'])
def create_bin():
    data = request.get_json()
    if data is None or 'name' not in data or 'json' not in data:
        return jsonify({'error': 'Invalid request'}), 400
    bin_id = generate_id()
    conn = sqlite3.connect('bins.db')
    c = conn.cursor()
    c.execute('INSERT INTO bins (id, name, json) VALUES (?, ?, ?)',
              (bin_id, data['name'], json.dumps(data['json'])))
    conn.commit()
    conn.close()
    return jsonify({'id': bin_id}), 201


@app.route('/bins/<bin_id>', methods=['GET'])
def get_bin(bin_id):
    conn = sqlite3.connect('bins.db')
    c = conn.cursor()
    c.execute('SELECT json FROM bins WHERE id = ?', (bin_id, ))
    result = c.fetchone()
    if result is None:
        return jsonify({'error': 'Bin not found'}), 404
    conn.close()
    return result[0]


@app.route('/bins/<bin_id>', methods=['PUT'])
def update_bin(bin_id):
    data = request.get_json()
    if data is None or 'json' not in data:
        return jsonify({'error': 'Invalid request'}), 400
    conn = sqlite3.connect('bins.db')
    c = conn.cursor()
    c.execute('UPDATE bins SET json = ? WHERE id = ?',
              (json.dumps(data['json']), bin_id))
    conn.commit()
    conn.close()
    return '', 204


@app.route('/bins/<bin_id>', methods=['DELETE'])
def delete_bin(bin_id):
    conn = sqlite3.connect('bins.db')
    c = conn.cursor()
    c.execute('DELETE FROM bins WHERE id = ?', (bin_id, ))
    conn.commit()
    conn.close()
    return '', 204


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='JSON Bins API')
    parser.add_argument('-H',
                        '--host',
                        default='localhost',
                        help='The server host')
    parser.add_argument('-p',
                        '--port',
                        type=int,
                        default=5000,
                        help='The server port')
    args = parser.parse_args()
    conn = sqlite3.connect('bins.db')
    c = conn.cursor()
    c.execute(
        'CREATE TABLE IF NOT EXISTS bins (id TEXT PRIMARY KEY, name TEXT NOT NULL, json TEXT NOT NULL)'
    )
    conn.close()
    app.run(debug=True, host=args.host, port=args.port)
