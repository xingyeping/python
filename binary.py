import struct
import ctypes
import binascii

#class Profile(struct.Struct):
#	_fields_ = [
#		('vnic_group_id', struct.BitField(8)),
#		('profile_id', struct.BitField(8)),
#		('l4_dst_port', struct.BitField(16)),
#		('l4_is_tcp', struct.BitField(1)),
#	]


#s = Profile()
#s.vnic_group_id = 3

#packed = s.pack()
class A(ctypes.Structure):
	_fields_ = [("a", ctypes.c_uint32, 1),
				("b", ctypes.c_uint32, 3),
				("c", ctypes.c_uint32, 4),
				("d", ctypes.c_uint32, 4),
				("e", ctypes.c_uint32, 20),
				("f", ctypes.c_uint32, 3)
	]

class Header(ctypes.Structure):
	_fields_ = [
		("type", ctypes.c_uint32),
		("len", ctypes.c_uint32)
	]

s = A()
s.a = 1
s.b = 2
s.c = 4
s.d = 5
s.e = 111
s.f = 4

h = Header()
h.type = 1
h.len = 8


print (binascii.hexlify(s))

s3 = binascii.hexlify(s)
s4 = binascii.a2b_hex(s3)
print (s4)
binary_data = struct.pack('16s', s3)
print(binary_data)
file = "jnet_profile_data.c"

h1 = binascii.hexlify(h)
h2 = binascii.a2b_hex(h1)


with open(file,"wb") as f:
	#for x in s4:
	#	a = struct.pack('B', x)
	#	print (a)
	#	f.write(a)
	f.write(h)
	f.write(s)
	f.write(s)
	f.write(s)
	f.write(s)

'''
f = open(file, "wb")
f.write(h)
#f.seek(0, 2)
f.write(s)
f.close()
'''
