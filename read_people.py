import pickle

with open('/home/itachi3/Documents/Research/codes/torch/openface_modified/demos/people.p', 'rb') as myfile:
    my_list = pickle.load(myfile)

print "People detected are:"
for name in my_list:
    print name;
    print '\n'
myfile.close()
