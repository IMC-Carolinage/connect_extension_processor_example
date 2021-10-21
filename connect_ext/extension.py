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


class Connect_extension_processor_exampleExtension(Extension):

    def process_asset_purchase_request(self, request):
        self.logger.info(f"Obtained request with id {request['id']}")
        return ProcessingResponse.done()

    def process_asset_change_request(self, request):
        self.logger.info(f"Obtained request with id {request['id']}")
        return ProcessingResponse.done()

    def process_asset_suspend_request(self, request):
        self.logger.info(f"Obtained request with id {request['id']}")
        return ProcessingResponse.done()

    def process_asset_resume_request(self, request):
        self.logger.info(f"Obtained request with id {request['id']}")
        return ProcessingResponse.done()

    def process_asset_cancel_request(self, request):
        self.logger.info(f"Obtained request with id {request['id']}")
        return ProcessingResponse.done()

    def process_asset_adjustment_request(self, request):
        self.logger.info(f"Obtained request with id {request['id']}")
        return ProcessingResponse.done()

    def validate_asset_purchase_request(self, request):
        self.logger.info(f"Obtained request with id {request['id']}")
        return ValidationResponse.done(request)

    def validate_asset_change_request(self, request):
        self.logger.info(f"Obtained request with id {request['id']}")
        return ValidationResponse.done(request)

    