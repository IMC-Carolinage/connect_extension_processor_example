# -*- coding: utf-8 -*-
#
# Copyright (c) 2021, Carolina Giménez Escalante
# All rights reserved.
#

from connect_ext.extension import ConnectExtensionProcessorExampleExtension


def test_process_asset_purchase_request(
    sync_client_factory,
    response_factory,
    logger,
):
    config = {'ACTIVATION_TEMPLATE_NAME': '', 'API_ENDPOINT': ''}
    request = {'id': 1, 'status': 'pending', 'params': {}}
    responses = [
        response_factory(count=100),
        response_factory(value=[{'id': 'item-1', 'status': 'pending'}]),
    ]
    client = sync_client_factory(responses)
    ext = ConnectExtensionProcessorExampleExtension(client, logger, config)
    result = ext.process_asset_purchase_request(request)
    assert result.status == 'success'


def test_process_asset_change_request(
    sync_client_factory,
    response_factory,
    logger,
):
    config = {'ACTIVATION_TEMPLATE_NAME': '', 'API_ENDPOINT': ''}
    request = {'id': 1, 'status': 'pending', 'asset': {'items': [{'quantity': 23, 'period': ''}]}}
    responses = [
        response_factory(count=100),
        response_factory(value=[{'id': 'item-1', 'value': 'value1'}]),
    ]
    client = sync_client_factory(responses)
    ext = ConnectExtensionProcessorExampleExtension(client, logger, config)
    result = ext.process_asset_change_request(request)
    assert result.status == 'success'


def test_process_asset_suspend_request(
    sync_client_factory,
    response_factory,
    logger,
):
    config = {'ACTIVATION_TEMPLATE_NAME': '', 'API_ENDPOINT': ''}
    request = {'id': 1, 'status': 'pending', 'asset': {'items': [{'quantity': 23, 'period': 'OneTime'}]}}
    responses = [
        response_factory(count=100),
        response_factory(value=[{'id': 'item-1', 'value': 'value1'}]),
    ]
    client = sync_client_factory(responses)
    ext = ConnectExtensionProcessorExampleExtension(client, logger, config)
    result = ext.process_asset_suspend_request(request)
    assert result.status == 'success'


def test_process_asset_resume_request(
    sync_client_factory,
    response_factory,
    logger,
):
    config = {'ACTIVATION_TEMPLATE_NAME': '', 'API_ENDPOINT': ''}
    request = {'id': 1, 'status': 'pending'}
    responses = [
        response_factory(count=100),
        response_factory(value=[{'id': 'item-1', 'value': 'value1'}]),
    ]
    client = sync_client_factory(responses)
    ext = ConnectExtensionProcessorExampleExtension(client, logger, config)
    result = ext.process_asset_resume_request(request)
    assert result.status == 'success'


def test_process_asset_cancel_request(
    sync_client_factory,
    response_factory,
    logger,
):
    config = {'ACTIVATION_TEMPLATE_NAME': '', 'API_ENDPOINT': ''}
    request = {'id': 1, 'status': 'pending', 'asset': {'items': [{'quantity': 23, 'period': ''}]}}
    responses = [
        response_factory(count=100),
        response_factory(value=[{'id': 'item-1', 'value': 'value1'}]),
    ]
    client = sync_client_factory(responses)
    ext = ConnectExtensionProcessorExampleExtension(client, logger, config)
    result = ext.process_asset_cancel_request(request)
    assert result.status == 'success'
