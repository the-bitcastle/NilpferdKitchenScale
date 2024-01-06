#Stub python Code for handling Weight Notificiations
#using python module bleak

from bleak import BleakClient

SCALE_CHARACTERISTIC = "0000ffb2-0000-1000-8000-00805f9b34fb"

def notification_handler(characteristic: BleakGATTCharacteristic, data: bytearray):

    print(f"Value: {data}, Len: {len(data)}")
    val_ascii = binascii.hexlify(data).decode('ascii')
    print (f"ASCII: {val_ascii}")
    val_startcode = val_ascii[:2]
    val_bytecount = val_ascii[2:4]
    val_status = val_ascii[4:6]
    val_unit = val_ascii[6:8]
    val_data = val_ascii[8:14]
    val_int = int(val_data, 16)
    val_display_float= val_int * 0.001
    

    print (f"Status: {val_status}, Unit:{val_unit}, Data:{val_data} --> {val_int} Display:{val_display_float} ")
