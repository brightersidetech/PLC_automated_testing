import logging
from pyModbusTCP.client import ModbusClient

modbus_tcp_master = ModbusClient()

logger = logging.getLogger('MODBUS_TCP_TESTER')

# Test Reading valid single holding register
def test_read_holding_register():
    success = False
    logger.info('Reading Modbus Slave Holding register')
    data = modbus_tcp_master.read_holding_registers(0, 1)
    if data:
        logger.info(f'Read data: {str(data)}')
        success = True
    assert(success)

#Test Readig Multiple valid holding registers
def test_read_holding_registers():
    success = False
    logger.info('Reading Multiple Modbus Slave Holding registers')
    data = modbus_tcp_master.read_holding_registers(0, 4)
    if data:
        logger.info(f'Read data: {str(data)}')
        success = True
    assert(success)

# reading Invalid holding register
def test_read_invalid_holding_register():
    success = False
    logger.info('Reading Invalid Modbus Slave Holding register')
    data = modbus_tcp_master.read_holding_registers(0, 4)
    if not data:
        success = True
    assert(success)   
