# Copyright 2020 Jared Hendrickson
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

import unit_test_framework

class APIUnitTestFirewallNATOneToOne(unit_test_framework.APIUnitTest):
    url = "/api/v1/firewall/nat/one_to_one"
    get_payloads = [{}]
    post_payloads = [
        {
            "interface": "wan",
            "src": "any",
            "dst": "wanip",
            "external": "192.168.1.123",
            "natreflection": "enable",
            "descr": "Unit Test",
            "nobinat": True,
            "top": True,
            "disabled": True
        }
    ]
    put_payloads = [
        {
            "id": 0,
            "interface": "lan",
            "src": "!1.1.1.1",
            "dst": "1.2.3.4",
            "external": "4.3.2.1",
            "natreflection": "disable",
            "descr": "Updated Unit Test",
            "disabled": False,
            "nobinat": False,
            "top": False,
            "apply": True
        }
    ]
    delete_payloads = [
        {"id": 0, "apply": true}
    ]

APIUnitTestFirewallNATOneToOne()