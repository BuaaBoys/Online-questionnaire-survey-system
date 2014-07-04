from xml.dom.minidom import Document
from xml.etree.ElementTree import ElementTree


class Question():
    qtype = ''
    content = ''
    items = []

    def __init__(self, t, c, i):
        self.qtype = t
        self.content = c
        self.items = i

    def __unicode__(self):
        return self.content

    def __str__(self):
        return self.content


class Questions():
    qid = ''
    questionList = []

    def __init__(self, qs=[], qid=''):
        self.qid = qid
        for q in qs:
            self.addQuestion(q)

    def addQuestion(self, question):
        self.questionList.append(question)

    def read(self):
        tree = ElementTree()
        tree.parse('./data/' + str(self.qid) + '.xml')
        root = tree.getroot()
        count = root.get('count')
        if count > 0:
            nodes = root.getchildren()
            for node in nodes:
                c = node.find('question').text
                t = []
                items = node.findall('item')
                for item in items:
                    t.append(item.text)
                q = Question(node.tag, c, t)
                print q.qtype, q.content, q.items
                self.addQuestion(q)

    def write(self):
        doc = Document()
        root = doc.createElement('content')
        root.setAttribute('id', self.qid)
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

        fileName = r'./data/' + 'new' + self.qid + '.xml'
        print fileName
        f = open(fileName, 'w')

        try:
            f.write(doc.toprettyxml(indent='   '))

        except Exception, e:
            f.close()
            print e
        f.close()
