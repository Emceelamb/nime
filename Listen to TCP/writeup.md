# Listening to a TCP handshake

For this project I wanted to push myself in thinking about data in non traditional ways while thinking about data capture and real-time data visualization. In addition I wanted to challenge myself in making non-screen based data art. While selecting a source of data I thought about the means of data collection particularly deep packet inspection in countries hostile to internet freedoms. To pursue this I wanted to analyze my own network traffick. 

While performing network analysis on myself I was stumped on how to find any meaning with something as low level as a packet. I found that with the world (thankfully) moving towards a more secure future with SSL the packet data themselves did not reveal too much. With more analysis I was intrigued with the TCP protocol itself, particularly the TCP handshake.

When computers connect via TCP they must perform a three-way handshake in order to communicate. The first computer will send a SYNC packet to the other to initialize then the second computer will reply with a SYNC-ACK packet and finally the first computer will acknowledge the reply with a ACK packet completing the handshake. I think there is something quite human about this connnection and decided that this was something I wanted to visualize.

I haven't been doing physical computing or much fabrication in a while, so I decided that would be my medium. I wanted to work with sound because that felt detached from the internet, but also not quite because the internet can trace its history to telegraph and morse code. 

I chose solenoids as my tool because of their binary nature, as well as their speed. Internet traffick moves at tremendous speeds so I had to choose a medium that could support those speeds. Originally I wanted to make something more musical but I didn't have time to find affordable instruments so I fabricated my own woodblock and tin drum. I wanted to use different materials to create different sounds to highlight the differences between the request and response packets.

From a technical level I am using and Open-WRT router and iptables to forward traffick from my laptop to a  Raspberry Pi. On the Raspberry Pi I am using tshark to sniff the traffick coming through my computer and filtering for TCP packets. Finally I parse through the captured packets and trigger the solenoids depending on the type of data packet.

What is interesting about the project is that it sonifies in real time the data being sent. Computers can be quite chatty when left idling. I have heard that Amazon Echoes speak to their servers every 15 seconds or so. So it would be interesting to analyze that traffick. 

I also think that it could be an interesting teaching tool to visualize computer networking concepts. In an ideal world the sounds would be quite predictible in a 1-2-1 kind of pattern. However because of packet loss and latency this is not the case.


