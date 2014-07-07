from xml.dom.minidom import Document
from xml.etree import ElementTree

class Question():

	def __init__(self, d, t, c, i):
		self.qid = d
		self.qtype = t
		self.content = c
		self.items = i

	def __unicode__(self):
		return self.content

	def __str__(self):
		return self.content

class Questions():

	def __init__(self, qs=[], qid=''):
		self.qid = qid
		self.questionList = qs

	def clean(self):
		self.qid=''
		self.questionList = []

	def addQuestion(self, question):
		self.questionList.append(question)

	def read(self, string):
		t = ElementTree.fromstring(string)
		tree = ElementTree.ElementTree(t)
		root = tree.getroot()
		self.count = int(root.get('count'))
		if self.count > 0:
			nodes = root.getchildren()
			index = 0
			for node in nodes:
				index += 1
				c = node.find('question').text
				t = []
				items = node.findall('item')
				for item in items:
					t.append(item.text)
				q = Question(index,node.tag,c,t)
				self.addQuestion(q)

	def build(self):
		doc = Document()
		root = doc.createElement('content')
		root.setAttribute('count', str(len(self.questionList)))
		doc.appendChild(root)

		index = 0
		for q in self.questionList:
			index += 1
			qnode = doc.createElement(q.qtype)
			qnode.setAttribute('id', str(index))
			que = doc.createElement('question')
			queText = doc.createTextNode(q.content)
			que.appendChild(queText)
			qnode.appendChild(que)

			ind = 0
			for item in q.items:
				ind += 1
				itemNode = doc.createElement('item')
				itemNode.setAttribute('id', str(ind))
				itemNode.appendChild(doc.createTextNode(item))
				qnode.appendChild(itemNode)
			root.appendChild(qnode)

		return doc.toprettyxml(indent='    ')
