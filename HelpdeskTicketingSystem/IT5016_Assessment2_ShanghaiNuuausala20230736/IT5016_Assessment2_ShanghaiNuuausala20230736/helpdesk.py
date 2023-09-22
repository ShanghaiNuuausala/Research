from ticket import Ticket

class Helpdesk:
    def __init__(self):
        self.tickets = []
      
#SUBMIT TICKET
    def submit_ticket(self, staff_id, ticket_creator, contact_email, description):
        ticket = Ticket(staff_id, ticket_creator, contact_email, description)
        self.tickets.append(ticket)
        return ticket

#RESOLVE TICKET
    def resolve_ticket(self, ticket):
        ticket.resolve_password_change()

#REOPEN TICKET
    def reopen_ticket(self, ticket):
        ticket.reopen_ticket()
        ticket.status == "Reopened"

#DISPLAY TICKET       
    def display_tickets(self):
        for ticket in self.tickets:
            print(ticket)
            print()

#TICKET STATISTICS
    def get_ticket_statistics(self):
        created = len(self.tickets)
        resolved = sum(1 for ticket in self.tickets if ticket.status == "Closed")
        open_tickets = sum(1 for ticket in self.tickets if ticket.status == "Open")
        return created, resolved, open_tickets