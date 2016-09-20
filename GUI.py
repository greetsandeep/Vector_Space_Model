from Tkinter import *
from new_inverted import ultraCategories
from main import *
from nltk.tokenize import RegexpTokenizer

tokenizer = RegexpTokenizer('\w+|\$[\d\.]+|\S+')

query = ""

def show_entry_fields():
	global query
	query = (e1.get())
	process_query()


def process_query():
	#tokenize
	_query = re.sub('[^\x00-\x7F]','',decode_unicode_references(query))
	_query = tokenizer.tokenize(str(_query))
	_query = [x.strip('-.?/') for x in _query]  
	_query = filter(None,_query)

	#normalize
	_query = normalizer(_query)


root = Tk()

topFrame = Frame(root)
topFrame.pack(side = TOP)

root.wm_title("Vector Space Model")

intro = Label(topFrame,text="IR ASSIGNMENT # 1\n Vector Space Model",bg="grey",fg="black")
intro.pack(fill=X)

Label(topFrame, text="Query").pack(side = LEFT)
e1 = Entry(topFrame)
e1.pack(side = RIGHT)

midFrame = Frame(root)
midFrame.pack(side=TOP)

def sel():
   selection = ultraCategories[int(str(var.get()))]
   print selection

var = IntVar()
for i in xrange(len(ultraCategories)):
	i = Radiobutton(midFrame,text=ultraCategories[i],variable=var,value=i,command=sel)
	i.pack(side = LEFT)

bottomFrame = Frame(root)

bottomFrame.pack(side=TOP)
searchButton = Button(bottomFrame,text='Submit', command=show_entry_fields)
searchButton.pack(side = TOP)

root.mainloop()
