from starcluster.clustersetup import ClusterSetup

class init_mount_source(ClusterSetup):
     def __init__(self, empara):
          self.empara = empara 
     def run(self, nodes, master, user, user_shell, volumes):
          nodes[0].ssh.execute('sudo mkdir /home/data')
          #for node in nodes:
          #     node.ssh.execute('sudo mkdir /home/data')
