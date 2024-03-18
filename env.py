from os import getenv

class Env:
    modbus_slave_addr = getenv('PLC_IP_ADDR')
    modbus_slave_port = int(getenv('MODBUS_TCP_PORT'))
    modbus_slave_id = int(getenv('MODBUS_TCP_SLAVE_ID'))