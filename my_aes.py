'''ho    '''
class AES:
	state=0
	
	full_key=[]                
	Sbox =  (0x63, 0x7c, 0x77, 0x7b, 0xf2, 0x6b, 0x6f, 0xc5, 0x30, 0x01, 0x67,
	            0x2b, 0xfe, 0xd7, 0xab, 0x76, 0xca, 0x82, 0xc9, 0x7d, 0xfa, 0x59,
	            0x47, 0xf0, 0xad, 0xd4, 0xa2, 0xaf, 0x9c, 0xa4, 0x72, 0xc0, 0xb7,
	            0xfd, 0x93, 0x26, 0x36, 0x3f, 0xf7, 0xcc, 0x34, 0xa5, 0xe5, 0xf1,
	            0x71, 0xd8, 0x31, 0x15, 0x04, 0xc7, 0x23, 0xc3, 0x18, 0x96, 0x05,
	            0x9a, 0x07, 0x12, 0x80, 0xe2, 0xeb, 0x27, 0xb2, 0x75, 0x09, 0x83,
	            0x2c, 0x1a, 0x1b, 0x6e, 0x5a, 0xa0, 0x52, 0x3b, 0xd6, 0xb3, 0x29,
	            0xe3, 0x2f, 0x84, 0x53, 0xd1, 0x00, 0xed, 0x20, 0xfc, 0xb1, 0x5b,
	            0x6a, 0xcb, 0xbe, 0x39, 0x4a, 0x4c, 0x58, 0xcf, 0xd0, 0xef, 0xaa,
	            0xfb, 0x43, 0x4d, 0x33, 0x85, 0x45, 0xf9, 0x02, 0x7f, 0x50, 0x3c,
	            0x9f, 0xa8, 0x51, 0xa3, 0x40, 0x8f, 0x92, 0x9d, 0x38, 0xf5, 0xbc,
	            0xb6, 0xda, 0x21, 0x10, 0xff, 0xf3, 0xd2, 0xcd, 0x0c, 0x13, 0xec,
	            0x5f, 0x97, 0x44, 0x17, 0xc4, 0xa7, 0x7e, 0x3d, 0x64, 0x5d, 0x19,
	            0x73, 0x60, 0x81, 0x4f, 0xdc, 0x22, 0x2a, 0x90, 0x88, 0x46, 0xee,
	            0xb8, 0x14, 0xde, 0x5e, 0x0b, 0xdb, 0xe0, 0x32, 0x3a, 0x0a, 0x49,
	            0x06, 0x24, 0x5c, 0xc2, 0xd3, 0xac, 0x62, 0x91, 0x95, 0xe4, 0x79,
	            0xe7, 0xc8, 0x37, 0x6d, 0x8d, 0xd5, 0x4e, 0xa9, 0x6c, 0x56, 0xf4,
	            0xea, 0x65, 0x7a, 0xae, 0x08, 0xba, 0x78, 0x25, 0x2e, 0x1c, 0xa6,
	            0xb4, 0xc6, 0xe8, 0xdd, 0x74, 0x1f, 0x4b, 0xbd, 0x8b, 0x8a, 0x70,
	            0x3e, 0xb5, 0x66, 0x48, 0x03, 0xf6, 0x0e, 0x61, 0x35, 0x57, 0xb9,
	            0x86, 0xc1, 0x1d, 0x9e, 0xe1, 0xf8, 0x98, 0x11, 0x69, 0xd9, 0x8e,
	            0x94, 0x9b, 0x1e, 0x87, 0xe9, 0xce, 0x55, 0x28, 0xdf, 0x8c, 0xa1,
	            0x89, 0x0d, 0xbf, 0xe6, 0x42, 0x68, 0x41, 0x99, 0x2d, 0x0f, 0xb0, 0x54, 0xbb, 0x16)
	rcon=[0x01,0x02,0x04,0x08,0x10,0x20,0x40,0x80,0x1b,0x36]
	def keyEx(self,key):
		self.full_key.append(key)
		for key_index in range(10):
			last_col=[]
			for j in range(4):
				last_col.append(self.full_key[key_index][3][j])
			last_col[0],last_col[1],last_col[2],last_col[3]=last_col[1],last_col[2],last_col[3],last_col[0]	
			for j in range(4):
				last_col[j]=self.Sbox[last_col[j]]
			prev_col=[]
			working_col=[]
			temp_exp_key=[]
			for i in range(4):
				prev_col.append(self.full_key[key_index][0][i])
			working_col.append(last_col[0]^prev_col[0]^self.rcon[key_index])
			for i in range(3):
				working_col.append(last_col[i+1]^prev_col[i+1])
			temp_exp_key.append(working_col)
			for i in range(3):
				prev_col=[]
				last_col=working_col
				working_col=[]
				for j in range(4):
					prev_col.append(self.full_key[key_index][i+1][j])
				for j in range(4):
					working_col.append(prev_col[j]^last_col[j])
				temp_exp_key.append(working_col)
			self.full_key.append(temp_exp_key)
		print "The expanded key is as below:: "
		for index in range(11):
			print str(index)+" :  ",
			for i in range(4):
				for j in range(4):
					print hex(self.full_key[index][i][j])[2:],
			print"\n"
	def keyWhitening(self):
		for i in range(4):
			for j in range(4):
				self.state[i][j]^=self.full_key[0][i][j]
		
	%this is shift row		
	def shiftRow(self):
		self.state[0][1],self.state[1][1],self.state[2][1],self.state[3][1]=self.state[1][1],self.state[2][1],self.state[3][1],self.state[0][1]
		self.state[0][2],self.state[1][2],self.state[2][2],self.state[3][2]=self.state[2][2],self.state[3][2],self.state[0][2],self.state[1][2]
		self.state[0][3],self.state[1][3],self.state[2][3],self.state[3][3]=self.state[3][3],self.state[0][3],self.state[1][3],self.state[2][3]		
	def subByte(self):
		for i in range(4):
			for j in range(4):
				self.state[i][j]=self.Sbox[self.state[i][j]]
	def vecMulGF(self,column,j):
		if(j==0):
			if(column[0]&0x80==0x80 and column[1]&0x80==0x80):
				val=column[1]
				value=((2*column[0] ^ 0x1b) ^ (2*column[1] ^ 0x1b ^ val) ^ column[2] ^ column[3])%256		
			elif(column[0]&0x80==0x80 and column[1]&0x80==0x00):
				val=column[1]
				value=((2*column[0] ^ 0x1b) ^ (2*column[1] ^ val) ^ column[2] ^ column[3])%256
			elif(column[0]&0x80==0x00 and column[1]&0x80==0x80):
				val=column[1]
				value=(2*column[0] ^ (2*column[1] ^ 0x1b ^ val) ^ column[2] ^ column[3])%256
			elif(column[0]&0x80==0x00 and column[1]&0x80==0x00):
				val=column[1]
				value=(2*column[0] ^ (2*column[1] ^ val) ^ column[2] ^ column[3])%256
			return value
		if(j==1):
			if(column[1]&0x80==0x80 and column[2]&0x80==0x80):
				val=column[2]
				value=((2*column[1] ^ 0x1b) ^ (2*column[2] ^ 0x1b ^ val) ^ column[0] ^ column[3])%256		
			elif(column[1]&0x80==0x80 and column[2]&0x80==0x00):
				val=column[2]
				value=((2*column[1] ^ 0x1b) ^ (2*column[2] ^ val) ^ column[0] ^ column[3])%256
			elif(column[1]&0x80==0x00 and column[2]&0x80==0x80):
				val=column[2]
				value=(2*column[1] ^ (2*column[2] ^ 0x1b ^ val) ^ column[0] ^ column[3])%256
			elif(column[1]&0x80==0x00 and column[2]&0x80==0x00):
				val=column[2]
				value=(2*column[1] ^ (2*column[2] ^ val) ^ column[0] ^ column[3])%256
			return value
		if(j==2):
			if(column[2]&0x80==0x80 and column[3]&0x80==0x80):
				val=column[3]
				value=((2*column[2]^ 0x1b) ^ (2*column[3] ^ 0x1b ^ val) ^ column[0] ^ column[1])%256		
			elif(column[2]&0x80==0x80 and column[3]&0x80==0x00):
				val=column[3]
				value=((2*column[2] ^ 0x1b) ^ (2*column[3] ^ val) ^ column[0] ^ column[1])%256
			elif(column[2]&0x80==0x00 and column[3]&0x80==0x80):
				val=column[3]
				value=(2*column[2] ^ (2*column[3] ^ 0x1b ^ val) ^ column[0] ^ column[1])%256
			elif(column[2]&0x80==0x00 and column[3]&0x80==0x00):
				val=column[3]
				value=(2*column[2] ^ (2*column[3] ^ val) ^ column[0] ^ column[1])%256
			return value
		if(j==3):		
			if(column[3]&0x80==0x80 and column[0]&0x80==0x80):
				val=column[0]
				value=((0x1b^2*column[3]) ^ (0x1b^2*column[0] ^ val) ^ column[1] ^ column[2])%256
			elif(column[3]&0x80==0x80 and column[0]&0x80==0x00):
				val=column[0]
				value=((2*column[3]^0x1b) ^ (2*column[0] ^ val) ^ column[1] ^ column[2])%256
			elif(column[3]&0x80==0x00 and column[0]&0x80==0x80):
				val=column[0]
				value=(2*column[3] ^ (2*column[0]^0x1b^ val) ^ column[1] ^ column[2])%256
			elif(column[3]&0x80==0x00 and column[0]&0x80==0x00):
				val=column[0]
				value=(2*column[3] ^ (2*column[0] ^ val) ^ column[1] ^ column[2])%256	
			return value
				    		
	def mixColumn(self):
		for i in range(4):
			temp=[]
			for j in range(4):
				a=self.vecMulGF(self.state[i],j)
				temp.append(a)
			self.state[i]=temp
	
	def addRoundKey(self,key_index):
		for i in range(4):
			for j in range(4):
				self.state[i][j]^=self.full_key[key_index][i][j]
	def display(self):
		for i in range(4):			
			for j in range(4):
				print hex(self.state[j][i])[2:],
			print "\n"	

		
	def encrypt(self,state,key):
		self.state=state
		self.keyEx(key)
		self.keyWhitening()
		for i in range(9):
			print "\nI AM IN %d STEP::"%(i+1)
			self.subByte()
			self.shiftRow()
			self.mixColumn()
			print "\nAfte MixColumn: "
			self.display()
			self.addRoundKey(i+1)
		self.subByte()
		self.shiftRow()			
		self.addRoundKey(10)
		return self.state

# creating a    encrypt..
enc=AES()
state=[[0x54,0x77,0x6f,0x20],[0x4f,0x6e,0x65,0x20],[0x4e,0x69,0x6e,0x65],[0x20,0x54,0x77,0x6f]]
key=[[0x54,0x68,0x61,0x74],[0x73,0x20,0x6d,0x79],[0x20,0x4b,0x75,0x6e],[0x67,0x20,0x46,0x75]]
#performing encryption
ct=enc.encrypt(state,key)
#printing the ciphertext
for i in range(4):			
	for j in range(4):
		print hex(ct[j][i])[2:],
	print "\n"
