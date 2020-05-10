from parking import parking_lot_manager
ledger=[]

while True:
	print("SHOPPING MALL PARKING SPACE")


	print("*"*50)
	ch=int(input("Type of vehicle: \n 1.2 wheeler parking \n 2.4 wheeler parking \n 3.remove 2 wheeler \n 4.remove 4 wheeler\n"))


	if ch==1:
		#two_wheeler_slots=int(input("enter slot"))
		#four_wheeler_slots=int(input("enter slot" ))
		vehicle_no=int(input("nehicle no.:"))
		start_time=int(input("enter start time:"))
		end_time=int(input("enter end time:"))
		parking_lot=parking_lot_manager()
		parking_lot_manager.count2wheeler()
		#parking_lot=parking_lot_manager(two_wheeler_slots,four_wheeler_slots,vehicle_no,start_time,end_time)

		#ledger[vehicle_no]=parking_lot_manager
		

	elif ch==2:
		two_wheeler_slots=input("enter slot")
		four_wheeler_slots=input("enter slot" )
		vehicle_no=input("nehicle no.:")
		start_time=input("enter start time:")
		end_time=input("enter end time:")

		parking_lot=parking_lot_manager(two_wheeler_slots,four_wheeler_slots,start_time,end_time,vehicle_no)
		parking_lot=ledger[vehicle_no]
		parking_lot.count2wheeeler(two)
		

	elif ch==3:
		
		vehicle_no=int(input("nehicle no.:"))
		start_time=input("enter start time:")
		end_time=input("enter end time:")

		
		parking_lot=ledger[vehicle_no]
		print(ledger)
		parking_lot.unbook2wheeler(parking_lot)
		parking_lot.two_wheeler_slots()
		print(ledger)

	elif ch==4:
		
		vehicle_no=input("nehicle no.:")
		start_time=input("enter start time:")
		end_time=input("enter end time:")

		
		parking_lot=ledger[vehicle_no]
		parking_lot.unbook4wheeler(parking_lot)
		parking_lot.four_wheeler_slots()
		print(ledger)

	else:
		break		



