import pymelsec  # 连接 PLC
import modbus_tk

client = modbus_tk.
plc = pymelsec.Type3E
plc.connect("192.168.0.10", port=8193)

# 读取地址的值
value = plc.read("D100")

# 关闭连接
plc.disconnect()

print(value)

