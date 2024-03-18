import logging
from pyModbusTCP.client import ModbusClient

modbus_tcp_master = ModbusClient()

logger = logging.getLogger('MODBUS_TCP_MASTER')

def test_read_holding_register():
    success = False
    logger.info('Reading Modbus Slave Holding register')
    data = modbus_tcp_master.read_holding_registers(20, 1)
    if data:
        logger.info(f'Read: {str(data)}')
        success = True
    assert(success)