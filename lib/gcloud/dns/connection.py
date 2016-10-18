# Copyright 2015 Google Inc. All rights reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

"""Create / interact with gcloud dns connections."""

from gcloud import connection as base_connection


class Connection(base_connection.JSONConnection):
    """A connection to Google Cloud DNS via the JSON REST API."""

    API_BASE_URL = 'https://www.googleapis.com'
    """The base of the API call URL."""

    API_VERSION = 'v1'
    """The version of the API, used in building the API call's URL."""

    API_URL_TEMPLATE = '{api_base_url}/dns/{api_version}{path}'
    """A template for the URL of a particular API call."""

    SCOPE = ('https://www.googleapis.com/auth/ndev.clouddns.readwrite',)
    """The scopes required for authenticating as a Cloud DNS consumer."""
