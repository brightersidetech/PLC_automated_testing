from opcua import Client
from env import Env
import logging
import pytest

__all__ = [
    'use_opcua_client'
]

logger = logging.getLogger('OPCUA_CLIENT')


@pytest.fixture(scope='session', autouse=True)
def use_opcua_client():
    url = "opc.tcp://" + Env.modbus_slave_addr + ":" + str(Env.opcua_port)
    success = True
    # Connect to the OPC UA server
    logger.info(f'Connecting to OPC UA Server at {Env.modbus_slave_addr}:{Env.opcua_port}')
    try:
        opcua_client = Client(url)
        opcua_client.connect()
        logger.info('Connected to OPC UA Server')
    except Exception as err:
        success = False
        logger.info(f'Could not connect to OPC UA Server at {Env.modbus_slave_addr}:{Env.opcua_port}')
    
    assert(success)
    yield opcua_client
    # Cleaning up
    logger.info(f'Disconnecting from OPC UA Server at {Env.modbus_slave_addr}:{Env.opcua_port}')
    opcua_client.disconnect()