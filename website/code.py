

class AdjNode:
	def __init__(self,data):
		self.data = data
		self.next = None

class Graph1:
	def __init__(self,nodes,edges):
		# net = Network(height='100%',width='100%')
		self.graph = [None]*(len(nodes)+1)
		self.nodes = nodes
		for edge in edges:
			self.add_adjedge(edge.user_id,edge.friend)
			
        

	def add_adjedge(self,src,dest):
		node = AdjNode(dest)
		node.next = self.graph[src]
		self.graph[src] = node

		node = AdjNode(src)
		node.next = self.graph[dest]
		self.graph[dest] = node
    
	def level_1(self,vertex):
		temp = self.graph[vertex]
		level1_lst=[]
		while temp:
			if temp:
				level1_lst.append(temp.data)
				temp = temp.next
		return level1_lst

	def level_2(self,vertex):
		lst=[]
		level1_lst = self.level_1(vertex)
		
		for i in level1_lst:
			
			temp = self.graph[i]
			while temp:
				
					lst.append(temp.data)
					temp = temp.next
		lst = set(lst)
		lst.remove(vertex)
		return list(lst.difference(set(level1_lst)))
	
	def jacc_similarity(self,n,lst):
		fin_list=[]
		s1 = set(self.nodes[n-1].skill)	
		for i in lst:
			s2 = set(self.nodes[i-1].skill)
			fin_list.append( [i,float(len(s1.intersection(s2)) / len(s1.union(s2)))])
		return fin_list

	def display(self):
		for i in range(len(self.graph)):
			print("Adjacency list of vertex {}\n head".format(i), end="")
			temp = self.graph[i]
			while temp:
				if temp:
					print(" -> {}".format(temp.data), end="")
					temp = temp.next
			print(" \n")  
	
    


