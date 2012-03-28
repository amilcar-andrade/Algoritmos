def pivote(x):
	if len(x) <= 1:
		return x
	izq = []
	derecha = []
	final =[]
	for i in range(0,len(a)):
		if i< len(a)/2:
			izq.append(a[i])
		else:
			derecha.append(a[i])
		        
	if 
	 	len(derecha) > 0:
		pivot = derecha[0]
		i=0
		j=0
			for w in range(1,len(derecha)):
    			if pivot > derecha[w]:
        			i = i+1
        			j = j+1
        			derecha[i], derecha[j] = derecha[j], derecha[i]
    			else:
        			j=j+1
					derecha.insert(i+1,pivot)
					del derecha[0]
	else:
		pivot = izq[0]
		i=0
		j=0
			for w in range(1,len(izq)):
	    		if pivot > izq[w]:
	        		i = i+1
	        		j = j+1
	        		izq[i], izq[j] = izq[j], izq[i]
	    		else:
	        		j=j+1
					izq.insert(i+1,pivot)
					del izq[0]
	
	final = izq + derecha
	return final
		
		


