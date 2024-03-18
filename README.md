## PLC Automated Testing
 This project aims to develop PLC Automated Tests for Industrial Automation Applications. The Automated testing utilizes different technologies to accomplish an Automated method, to Test PLC Software.

Automated tests run on a separate device and are written in python using the pytest framework. The Automated tests will cover unit testing, Integration testing and Acceptance testing. Test cases will also include testing of different industrial communication protocols including Modbus, OPC UA, Socket, HTTP and REST


### Test Architecture
![alt text](misc/test_arch.PNG)
- Tests are written and run on a seperate device reffered to as the ```Test Host```
- TheTest Host configures the ```Test Subject``` and then sets different test cases by setting different paramters on the Test Subject
- Tests are written in python with help of the pytest Library
- To communicate with the Test Subject to set paramters and read results, the Test Host uses a vraity of technologies and communitaion cahhles which include Modbus, OPC UA, TCP Sockets and many others

### Prerequists
- TO DO
### Instructions 
- TO DO