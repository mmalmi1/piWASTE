from flask import Blueprint, render_template, url_for, request, redirect, Response, send_file, abort, make_response, current_app
from app import db
import os


mod = Blueprint('files', __name__)

@mod.route('/files/<path:dir_name>', methods=['GET'])
def files(dir_name):
  """
  Company confidential files view
  """

  head_of_path, tail_of_path = os.path.split(current_app.instance_path)

  abs_path = os.path.join(head_of_path, dir_name)
  if str(dir_name) != "docs":
    return "Empty"

  if os.path.isfile(abs_path):
      return send_file(abs_path)

  files = os.listdir(abs_path)
  resp = make_response(render_template('files.html', files=files))
  return resp
