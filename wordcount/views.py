from django.http import HttpResponse		
from django.shortcuts import render	 		#need to use this to pass html files at output
import operator

def homepage(request):
	#return HttpResponse('Hello User')
	#return render(request,'home.html',{'hithere':'This is me'})			#can also pass a dictionary in render function
	return render(request,'home.html')
	
def count(request):
	fulltext1 = request.GET['fulltext']
	#print (fulltext1)
	wordlist = fulltext1.split()
	
	worddictionary = {}
	
	for word in wordlist:
		if word in worddictionary:
			#Increase
			worddictionary[word] += 1
		else:
			#Add to the worddictionary
			worddictionary[word] = 1
	
	sortedwords=sorted(worddictionary.items(),key=operator.itemgetter(1),reverse=True)
	
	return render(request,'count.html',{'fulltextdict':fulltext1,'count':len(wordlist),'sortedwords':sortedwords})

def about(request):
	return render(request,'about.html')

def eggs(request):
	return HttpResponse('<h1>Eggs are Great</h1>')