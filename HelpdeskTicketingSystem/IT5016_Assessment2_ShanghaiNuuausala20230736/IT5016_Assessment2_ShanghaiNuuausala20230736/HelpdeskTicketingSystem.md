# This prototype of a Help Desk Ticketing System is defined in 3 seperate files which consists of two classes, Ticket and HelpDesk, and a main function that demonstrates their usage.


## Ticket Class:

### The Ticket Class serves as a representation of individual support tickets and possesses the following attributes:

1. ticketNumber: A unique number for each ticket.
2. staffID: The ID of the Help Desk staff member.
3. ticketCreator: The name of the person submitting the ticket.
4. contactEmail: The email address of the person submitting the ticket.
5. description: A description of the of the issue or request.
6. response: A responnse to the ticket (default response "Not Yet Provided")
7. status: The ticket status (default status "Open")


The __str__ method is defined to provide a string representation of a ticket when it is printed.


## HelpDesk Class:

### The HelpDesk Class represents the support of the Help Desk and possesses the following class-level attributes:

1. ticketNumber: A class-level variable that is used to assign automatically unique ticket numbers.

The class has the following methods:

1. submitTicket: This method creates a new Ticket object that assigns the method to a ticket number, and adds it to the tickets list. If the ticket description contains "Password Change" it will automatically provide a response and update the ticket statistics.
2. respondToTicket: This method allows staff members to respond to a ticket by providing a response. It also handles the change of a ticket's status between being "Open" and "Closed" while updating the tickets statistics accordingly.
3. displayTicket: This method displays the ticket information based of its ticket number.
4. displayStatistics: This method displays statistics about the number of tickets submitted, closed tickets, and tickets to be solved.

## Main Function:

In the main function, an Instance of the Help Desk Class is created.

Three tickets are submitted using the submitTicket method, each containing different issue descriptions.
The statistics are displayed using the displayStatistics method.

Two tickets are resolved using the respondToTicket method and includes appropriate responses.
Individual tickets are displayed using the displayTicket method.

One ticket is reopened using the respondToTicket method.

Individual tickets are displayed using the displayTicket method.

Ticket statistics are displayed again to reflect the changes.