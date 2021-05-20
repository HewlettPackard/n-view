# (C) Copyright 2019 Hewlett Packard Enterprise Development LP.

# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at

#  http://www.apache.org/licenses/LICENSE-2.0

# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

# __author__ = "@netwookie"
# __credits__ = ["Rick Kauffman"]
# __license__ = "Apache2.0"
# __version__ = "1.0.0"
# __maintainer__ = "Rick Kauffman"
# __email__ = "rick.a.kauffman@hpe.com"

from mongoengine import signals

from application import db

class System(db.Document):
    name = db.StringField(db_field="n", required=True)
    version = db.StringField(db_field="v", required=True)
    serial = db.StringField(db_field="s", required=True)
    role = db.StringField(db_field="r", required=True)
    nics = db.StringField(db_field="ni", required=True)
    model = db.StringField(db_field="m", required=True)
    usable = db.StringField(db_field="ua", required=True)
    used = db.StringField(db_field="u", required=True)
