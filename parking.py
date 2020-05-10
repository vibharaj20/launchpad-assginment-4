class parking_lot_manager:
	def __init__(self,two_wheeler,four_wheeler,start_time,end_time,vehicle_no):
		self.two_wheeler_slots=two_wheeler_slots
		self.four_wheeler_slots=four_wheeler_slots
		self.start_time=start_time
		self.end_time=end_time
		self.vehicle_no=vehicle_no
		


	def count2wheeler(self,two):

		self.two_wheeler_slots+=two
		print("\n no. of 2 wheeler",two)



	def count4wheeler(self,four):
		self.four_wheeler_slots+=four
		print("\n no. of 4 wheerler",four)

			
	def unbook2wheeler(self,two):
		self.two_wheeler_slots-=two
		print("\n no of 2 wheelers",two)

		
	def unbook4wheeler(self,four):
		self.four_wheeler_slots-=four
		print("\n no of 4 wheeler",four)	

		
