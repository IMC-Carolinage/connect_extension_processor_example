# -*- coding: utf-8 -*-
#
# Copyright (c) 2021, Carolina Giménez Escalante
# All rights reserved.
#
from connect.eaas.extension import (
    Extension,
    ProcessingResponse,
    ValidationResponse,
)
from connect_ext.app.purchase import (
    Purchase,
    Change,
    Cancel,
    Resume,
    Suspend)


class ConnectExtensionProcessorExampleExtension(Extension):

    ACTIVATION_TEMPLATE_NAME = 'Default Activation Template'
    TIER_CONFIG_ACTIVATION_TEMPLATE_NAME = 'Default Activation Template'
    API_ENDPOINT = ''

    def process_asset_purchase_request(self, request):
        self.logger.info(f"Obtained request with id {request['id']}")
        if request['status'] == 'pending':
            ConnectExtensionProcessorExampleExtension.ACTIVATION_TEMPLATE_NAME = self.config['ACTIVATION_TEMPLATE_NAME']
            ConnectExtensionProcessorExampleExtension.API_ENDPOINT = self.config['API_ENDPOINT']
            return Purchase().process_request(request, self.client)
        return ProcessingResponse.done()

    def process_asset_change_request(self, request):
        self.logger.info(f"Obtained request with id {request['id']}")
        if request['status'] == 'pending':
            ConnectExtensionProcessorExampleExtension.ACTIVATION_TEMPLATE_NAME = self.config['ACTIVATION_TEMPLATE_NAME']
            ConnectExtensionProcessorExampleExtension.API_ENDPOINT = self.config['API_ENDPOINT']
            return Change().process_request(request, self.client)
        return ProcessingResponse.done()

    def process_asset_suspend_request(self, request):
        self.logger.info(f"Obtained request with id {request['id']}")
        if request['status'] == 'pending':
            ConnectExtensionProcessorExampleExtension.ACTIVATION_TEMPLATE_NAME = self.config['ACTIVATION_TEMPLATE_NAME']
            ConnectExtensionProcessorExampleExtension.API_ENDPOINT = self.config['API_ENDPOINT']
            return Suspend().process_request(request, self.client)
        return ProcessingResponse.done()

    def process_asset_resume_request(self, request):
        self.logger.info(f"Obtained request with id {request['id']}")
        if request['status'] == 'pending':
            ConnectExtensionProcessorExampleExtension.ACTIVATION_TEMPLATE_NAME = self.config['ACTIVATION_TEMPLATE_NAME']
            ConnectExtensionProcessorExampleExtension.API_ENDPOINT = self.config['API_ENDPOINT']
            return Resume().process_request(request, self.client)
        return ProcessingResponse.done()

    def process_asset_cancel_request(self, request):
        self.logger.info(f"Obtained request with id {request['id']}")
        if request['status'] == 'pending':
            ConnectExtensionProcessorExampleExtension.ACTIVATION_TEMPLATE_NAME = self.config['ACTIVATION_TEMPLATE_NAME']
            ConnectExtensionProcessorExampleExtension.API_ENDPOINT = self.config['API_ENDPOINT']
            return Cancel().process_request(request, self.client)
        return ProcessingResponse.done()

