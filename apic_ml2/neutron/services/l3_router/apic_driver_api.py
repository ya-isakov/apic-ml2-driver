# Copyright (c) 2016 Cisco Systems Inc.
# All Rights Reserved.
#
#    Licensed under the Apache License, Version 2.0 (the "License"); you may
#    not use this file except in compliance with the License. You may obtain
#    a copy of the License at
#
#         http://www.apache.org/licenses/LICENSE-2.0
#
#    Unless required by applicable law or agreed to in writing, software
#    distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
#    WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
#    License for the specific language governing permissions and limitations
#    under the License.


class FipContext(object):
    """Floating IP context

    Contains the current floating IP, as well
    as its associated port
    """
    def __init__(self, floatingip, original=None, port_id_list=[]):
        self.original = original
        self.current = floatingip
        self.port_id_list = port_id_list


class ApicL3DriverBase(object):
    """APIC L3 driver abstract base class

       This is the APIC driver interface for L3 plugins. The purpose of
       this class is to define the APIC-specific API calls used by either
       the Neutron or Group Based Policy workflow as a result of a Layer 3
       API call.  This allows the driver to be used by other Layer 3 service
       plugins (e.g. the Cisco Router Service Plugin).
       """
    def update_router_postcommit(self, context, router):
        pass

    def delete_router_precommit(self, context, router_id):
        pass

    def add_router_interface_postcommit(self, context, router_id,
                                        interface_info):
        pass

    def remove_router_interface_precommit(self, context, router_id,
                                          interface_info):
        pass

    def create_floatingip_precommit(self, context, fip_context):
        pass

    def create_floatingip_postcommit(self, context, fip_context):
        pass

    def update_floatingip_precommit(self, context, id, fip_context):
        pass

    def update_floatingip_postcommit(self, context, id, fip_context):
        pass

    def delete_floatingip_precommit(self, context, id, fip_context):
        pass

    def delete_floatingip_postcommit(self, context, id, fip_context):
        pass
