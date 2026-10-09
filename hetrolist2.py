hetro=["Alice",12,"Binod",23,96,20,"Swara",45,"Crawl",98,"Raju"]
highest=max(x for x in hetro if isinstance(x,(int,float)))
ind=hetro.index(highest)
p1,p2=hetro[:ind],hetro[ind:]
print("List 1 : ",p1)
print("List 2 : ",p2)