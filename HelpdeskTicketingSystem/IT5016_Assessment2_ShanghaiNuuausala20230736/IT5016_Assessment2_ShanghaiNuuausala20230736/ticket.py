class Ticket:
    ticket_counter = 0 #STATIC COUNTER FOR ASSIGNING TICKET NUMBER AT 0

    def __init__(self, staff_id, ticket_creator, contact_email, description):
        self.ticket_number = Ticket.ticket_counter + 2001
        self.staff_id = staff_id
        self.ticket_creator = ticket_creator
        self.contact_email = contact_email
        self.description = description
        self.response = "Not Yet Provided"
        self.status = "Open"
        Ticket.ticket_counter += 1

#RESPONDING TO TICKETS
    def respond(self, response):
        self.response = response

#RESOLVING PASSWORD CHANGE WITH RULE:
    def resolve_password_change(self):
        if "Password Change" in self.description:
            new_password = self.staff_id[:2] + self.ticket_creator[:3]
            self.response = f"New password generated: {new_password}"
            self.status = "Closed"

#REOPENING A TICKET:
    def reopen_ticket(self):
        if self.status == "Closed":
            self.status = "Reopened"


#STR METHOD TO DEFINE A TICKET REPRESENTATION WHEN PRINTED:
    def __str__(self):
            return f"Ticket Number: {self.ticket_number}\n" \
               f"Staff ID: {self.staff_id}\n" \
               f"Ticket Creator: {self.ticket_creator}\n" \
               f"Email Address: {self.contact_email}\n" \
               f"Description of Issue: {self.description}\n" \
               f"Response: {self.response}\n" \
               f"Ticket Status: {self.status}"