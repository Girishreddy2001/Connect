from pyvis.network import Network

from .models import adj_list,User 
from . import db

class visual:
	def __init__(self):
		nodes = User.query.all()
		edges = adj_list.query.all()
		net = Network(height='100%', width='100%')
		net.repulsion()

		for i in nodes:
			net.add_node(i.id,label=i.first_name,title=i.skill)

		for i in edges:
			net.add_edge(i.user_id,i.friend)

		net.show('nx.html')
