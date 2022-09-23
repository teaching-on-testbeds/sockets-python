"""This topology has four VMs on a LAN. Also, the `pcmanfm` file explorer and the Leafpad text editor is installed.

To use this topology, follow the instructions at: [Programming with Python Sockets](https://teaching-on-testbeds.github.io/sockets-python/)

"""

# Import the Portal object.
import geni.portal as portal
# Import the ProtoGENI library.
import geni.rspec.pg as rspec
# Emulab specific extensions.
import geni.rspec.emulab as emulab

# Create a portal context, needed to defined parameters
pc = portal.Context()

# Create a Request object to start building the RSpec.
request = pc.makeRequestRSpec()

# Set up first host - romeo
node_romeo = request.XenVM("romeo")
node_romeo.addService(rspec.Execute(shell="bash", command="/usr/bin/sudo /usr/bin/apt update; /usr/bin/sudo /usr/bin/apt -y install pcmanfm python3 leafpad"))
node_romeo.startVNC()
node_romeo.routable_control_ip = True

# Give romeo some friends
node_juliet = request.XenVM("juliet")
node_juliet.addService(rspec.Execute(shell="bash", command="/usr/bin/sudo /usr/bin/apt update; /usr/bin/sudo /usr/bin/apt -y install pcmanfm python3 leafpad"))
node_juliet.startVNC()
node_juliet.routable_control_ip = True

node_hamlet = request.XenVM("hamlet")
node_hamlet.addService(rspec.Execute(shell="bash", command="/usr/bin/sudo /usr/bin/apt update; /usr/bin/sudo /usr/bin/apt -y install pcmanfm python3 leafpad"))
node_hamlet.startVNC()
node_hamlet.routable_control_ip = True

node_ophelia = request.XenVM("ophelia")
node_ophelia.addService(rspec.Execute(shell="bash", command="/usr/bin/sudo /usr/bin/apt update; /usr/bin/sudo /usr/bin/apt -y install pcmanfm python3 leafpad"))
node_ophelia.startVNC()
node_ophelia.routable_control_ip = True

# Set up a network link
lan = request.LAN()
lan.best_effort = True

iface_romeo = node_romeo.addInterface("eth1")
iface_romeo.addAddress(rspec.IPv4Address("10.10.0.100", "255.255.255.0"))
lan.addInterface(iface_romeo)

iface_juliet= node_juliet.addInterface("eth1")
iface_juliet.addAddress(rspec.IPv4Address("10.10.0.101", "255.255.255.0"))
lan.addInterface(iface_juliet)

iface_hamlet = node_hamlet.addInterface("eth1")
iface_hamlet.addAddress(rspec.IPv4Address("10.10.0.102", "255.255.255.0"))
lan.addInterface(iface_hamlet)

iface_ophelia = node_ophelia.addInterface("eth1")
iface_ophelia.addAddress(rspec.IPv4Address("10.10.0.103", "255.255.255.0"))
lan.addInterface(iface_ophelia)

# Print the RSpec to the enclosing page.
pc.printRequestRSpec(request)
