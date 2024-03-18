from pyModbusTCP.client import ModbusClient
import pytest
import logging
from env import Env

__all__ = [
    'use_modbus_tcp_master'
]

# Set logger
logger = logging.getLogger('MODBUS_MASTER')

# Fixture to create modbus TCP Client and prepare
@pytest.fixture(scope='session', autouse=True)
def use_modbus_tcp_master():
    logger.info('Creating Modbus TCP Master')
    modbus_tcp_master = ModbusClient(host=Env.modbus_slave_addr,
                                     port=Env.modbus_slave_port,
                                     unit_id=Env.modbus_slave_id,
                                     auto_open=False,
                                     auto_close=False)
    # Connect to modbus slave
    logger.info(f'Connecting to Modbus Slave at {Env.modbus_slave_addr}:{Env.modbus_slave_port}')
    conn = modbus_tcp_master.open()
    assert(conn)
    yield modbus_tcp_master
    # Cleaning up
    logger.info(f'Closing Connection to Modbus Slave at {Env.modbus_slave_addr}:{Env.modbus_slave_port}')
    modbus_tcp_master.close()

