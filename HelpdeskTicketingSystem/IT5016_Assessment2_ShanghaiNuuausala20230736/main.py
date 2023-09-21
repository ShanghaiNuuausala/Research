"""
Help Desk Ticketing System Prototype
Author: Shanghai Nuuausala
20230736

"""

from ticket import Ticket
from helpdesk import Helpdesk

if __name__ == "__main__":
    system = Helpdesk()

# SUBMITTED TICKETS:
    system.submit_ticket("TUPACS", "Tupac", "tupac@myhelpdesk.com", "Monitor screen not displaying output")
    system.submit_ticket("NICKIM", "Nicki", "nicki@myhelpdesk.com", "Network connection issue")
    password_change_ticket = system.submit_ticket("KANYEW", "Kanye", "kanye@myhelpdesk.com", "Password Change")

#DISPLAYING TICKET STATISTICS:
    created, resolved, open_tickets = system.get_ticket_statistics()
    print("Displaying Ticket Statistics")
    print(f"Tickets Created: {created}\nTickets Resolved: {resolved}\nTickets To Solve: {open_tickets}\n")
    print("Printing Tickets:")

#RESOLVED TICKET:
    system.resolve_ticket(password_change_ticket)

#TICKETS PRINTED WITH UPDATED STATISTICS:
    system.display_tickets()
    created, resolved, open_tickets = system.get_ticket_statistics()
    print("Displaying Ticket Statistics")
    print(f"Tickets Created: {created}\nTickets Resolved: {resolved}\nTickets To Solve: {open_tickets}\n")
    print("Printing Tickets:")

#REOPENED TICKET:
    system.reopen_ticket(password_change_ticket)

#TICKETS PRINTED WITH UPDATED STATISTICS:
    system.display_tickets()
    created, resolved, open_tickets = system.get_ticket_statistics()
    print("Displaying Ticket Statistics")
    print(f"Tickets Created: {created}\nTickets Resolved: {resolved}\nTickets To Solve: {open_tickets}\n")
