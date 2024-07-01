class Train:
    train = [{"train_id": 1, "train_name": "chennai express", "tickets": 10},
             {"train_id": 2, "train_name": "Mumbai express", "tickets": 5}]

    def getTrains(self):
        print("the available trains are:")
        for ele in self.train:
            print(ele)


class Book(Train):
    autoId = 0
    bookedTicket = []

    def ticketBooking(self, name, age, trainId, noOfTickets):
        flag = True
        for ele in self.train:
            if trainId == ele["train_id"] and noOfTickets <= ele["tickets"]:
                self.autoId += 1
                ele["tickets"] -= noOfTickets
                newBookedData = {"user_id": self.autoId,
                                 "user_name": name, "age": str(age), "train_id": trainId, "train_name": ele["train_name"], "no_of_booked_tickets": noOfTickets}
                self.bookedTicket.append(newBookedData)
                flag = False
                print('------------Booked successfully------------')
                return None
        if flag:
            print("The Train-id is invalid.... or No. of Tickets are not available...")

    def ticket_cancel(self, name, user_id):
        for data in self.bookedTicket:
            if data['user_id'] == user_id and data['user_name'] == name:
                trainId = data['train_id']
                no_of_tickets_canceled = data['no_of_booked_tickets']
                self.bookedTicket.remove(data)
                for train_data in self.train:
                    if train_data['train_id'] == trainId:
                        train_data['tickets'] += no_of_tickets_canceled
                        break
                print('--------------ticket successfully canceled-------------')
                break

    def getBookedTicket(self):
        print("the booked tickets are")
        for ele in self.bookedTicket:
            print("----------------------------------")
            print(ele)
            print("----------------------------------")


b = Book()
t = Train()
while True:
    print("1 book\n2 cancel\n3 available tickets\n4 BookedTicket\n5 exit")
    n = int(input())
    if n == 1:
        name = input("enter the name: ")
        age = input("enter the age: ")
        trainId = int(input("enter the Train-id:"))
        noOfTickets = int(input("Enter the number of tickets to book :"))

        b.ticketBooking(name, age, trainId, noOfTickets)
    elif n == 2:
        name = input("enter the name: ")
        user_id = int(input("enter the user-id:"))
        b.ticket_cancel(name, user_id)
    elif n == 3:
        t.getTrains()
    elif n == 4:
        b.getBookedTicket()
    else:
        exit(0)