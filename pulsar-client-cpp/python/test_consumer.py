#!/usr/bin/env python
#
# Copyright 2016 Yahoo Inc.
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
#


import pulsar

client = pulsar.Client('pulsar://localhost:6650')
consumer = client.subscribe('persistent://sample/standalone/ns/my-topic', "my-sub")

while True:
    msg = consumer.receive()
    print("Received message '{0}' id='{1}'".format(msg.data(), msg.message_id()))
    consumer.acknowledge(msg)

client.close()
