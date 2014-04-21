#!/usr/bin/env python
# vim: set fileencoding=utf-8 :
# @author: Manuel Guenther <Manuel.Guenther@idiap.ch>
# @date: Mon Jul 22 19:56:11 CEST 2013
#
# Copyright (C) 2011-2013 Idiap Research Institute, Martigny, Switzerland
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, version 3 of the License.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.

import os

def atnt_database_directory(atnt_user_directory = None):
  """Checks, where the AT&T database is located and downloads it on need."""
  if atnt_user_directory:
    # a user directory is specified
    atnt_default_directory = atnt_user_directory
  elif 'ATNT_DATABASE_DIRECTORY' in os.environ:
    # the environment variable is set
    atnt_default_directory = os.environ['ATNT_DATABASE_DIRECTORY']
  else:
    atnt_default_directory = 'Database'

  # Check if the database is already in the specified directory
  if os.path.isdir(atnt_default_directory) and set(['s%d'%s for s in range(1,41)]).issubset(os.listdir(atnt_default_directory)):
    return atnt_default_directory

  # ... download the database ...

  # create directory
  if not os.path.exists(atnt_default_directory):
    os.mkdir(atnt_default_directory)

  # setup
  import urllib2, tempfile
  db_url = 'http://www.cl.cam.ac.uk/Research/DTG/attarchive/pub/data/att_faces.zip'
  import logging
  logger = logging.getLogger('bob')
  logger.warn("Downloading the AT&T database from '%s' to '%s' ..." % (db_url, atnt_default_directory))

  # download
  url = urllib2.urlopen(db_url)
  local_zip_file = tempfile.mkstemp(prefix='atnt_db_', suffix='.zip')[1]
  dfile = open(local_zip_file, 'w')
  dfile.write(url.read())
  dfile.close()

  # unzip
  import zipfile
  zip = zipfile.ZipFile(local_zip_file)
  zip.extractall(atnt_default_directory)
  zip.close()

  # remove temporary zip file
  os.remove(local_zip_file)

  return atnt_default_directory


