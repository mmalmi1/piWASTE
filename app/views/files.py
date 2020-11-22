from flask import Blueprint, render_template, url_for, request, redirect, Response, send_file, abort, make_response, current_app
from app import db
import os


mod = Blueprint('files', __name__)

@mod.route('/files/', methods=['GET'])
def file_hint():
  """
  Just a quick hint for finding files
  """
  return "You are on the right track. Files are hidden somewhere close"

@mod.route('/files/<path:dir_name>', methods=['GET'])
def files(dir_name):
  """
  Company confidential files view
  """

  head_of_path, tail_of_path = os.path.split(current_app.instance_path)

  abs_path = os.path.join(head_of_path, dir_name)

  if not os.path.exists(abs_path):
      return "You are on the right track. Files are hidden somewhere close"

  if os.path.isfile(abs_path):
      return send_file(abs_path)

  files = os.listdir(abs_path)
  resp = make_response(render_template('files.html', files=files))
  return resp
