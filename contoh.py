"""Custom topology example

Two directly connected switches plus a host for each switch:

   host --- switch --- switch --- host

Adding the 'topos' dict with a key/value pair to generate our newly defined
topology enables one to pass in '--topo=mytopo' from the command line.
"""

from mininet.topo import Topo

class MyTopo( Topo ):
    "Simple topology example."

    def __init__( self ):
        "Create custom topo."

        # Initialize topology
        Topo.__init__( self )

        # Add hosts and switches
	h1 = self.addHost( 'h1', ip='10.0.0.1/24' )
	h2 = self.addHost( 'h2', ip='10.0.0.2/24' )
	h3 = self.addHost( 'h3', ip='10.0.0.3/24' )
	h4 = self.addHost( 'h4', ip='10.0.0.4/24' )
	h5 = self.addHost( 'h5', ip='10.0.0.5/24' )	
	s1 = self.addSwitch( 's1', mac='00:00:00:00:00:00:00:01' )

        # Add links
        self.addLink( s1, h1 )
        self.addLink( s1, h2 )
        self.addLink( s1, h3 )
	self.addLink( s1, h4 )
	self.addLink( s1, h5 )


topos = { 'mytopo': ( lambda: MyTopo() ) }
