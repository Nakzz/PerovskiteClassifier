from pymol.cgo import *
from pymol import cmd
from pymol import stored
from chempy import cpv
import os
import csv
import numpy as np
import pandas as pd

def process(
        cifName,
origin='pk1',
cutoff=10,
filename=None,
selection='all',
state=0,
property_name='p.dist',
coordinates=0,
decimals=3,
sort=1,
quiet=1):

    try:
        # if(cifName==):
        print(cifName)
        selection = '(%s)'%selection
        cutoff = abs(float(cutoff))
        filename = str(filename)
        state = abs(int(state))
        if (not int(state)):
            state=cmd.get_state()
        cmd.set('state', state) # distance by state
        property_name = str(property_name)
        decimals = abs(int(decimals))
        sort = int(sort)
        coordinates=bool(int(coordinates))
        quiet=bool(int(quiet))
    except:
        print('distancetoatom: aborting - input error!')
        return False

    cmd.reinitialize()
    cmd.reset()
    cmd.load("C:/Temp/uw-cmg/Spring2019/perovskiteClassifier/COM/cif_merge_organic/"+cifName + ".cif" )

    centerofmass = cmd.centerofmass()
    print(centerofmass)

    ([minX, minY, minZ], [maxX, maxY, maxZ]) = cmd.get_extent(selection="("+cifName+")")

    print([minX, minY, minZ], [maxX, maxY, maxZ])

    cmd.pseudoatom( pos=centerofmass)

    cmd.hide(selection="hydro")
    cmd.select(name= "atoms", selection="visible")

    cmd.pseudoatom(pos=centerofmass)

    distance = cmd.distance( "/pseudo01/PSDO/P/PSD`1/PS1", "/atoms",)

    print(distance)

    # temporary name for pseudoatom
    tempname = cmd.get_unused_name('temp_name')
    tempsel = cmd.get_unused_name('temp_sel')

    ori = centerofmass;

    # origin
    cmd.pseudoatom(object=tempname, resi=1, pos=ori)

    # select atoms within cutoff
    cmd.select(tempsel, '(%s around %f) and (%s) and state %d and not H.' % (tempname, cutoff, selection, state))
    cmd.delete(tempname)

    # atom list
    stored.temp = []
    cmd.iterate(tempsel, 'stored.temp.append([model, segi, chain, resn, resi, name, alt])')

    largestDistance =0;
    distance_list = []
    for atom in stored.temp:
        atom_name = ('/%s/%s/%s/%s`%s/%s`%s'%(atom[0], atom[1], atom[2], atom[3], atom[4], atom[5], atom[6]))
        atom_symbol = ('%s'%( atom[5]))
        atom_xyz = [round(x, decimals) for x in cmd.get_atom_coords(atom_name)]
        atom_dist = round(cpv.distance(ori, atom_xyz), decimals)

        if(atom_dist > largestDistance):
            distance_list = [atom_symbol,atom_xyz[0],atom_xyz[1],atom_xyz[2], atom_dist]
            largestDistance = atom_dist
            print('%s %s' % (atom[5], atom_dist))

    # print(cmd.get(name="0001", selection="0001"))

    print("")


    print('rAeff is %s being a %s atom'%(distance_list[4], distance_list[0]))
    return [cifName,distance_list[4], distance_list[0]]


def yourFunction( arg1, arg2 ):
    '''
DESCRIPTION

    Brief description what this function does goes here
    '''
    #
    # Your code goes here
    #
    print ("Hello, PyMOLers")
    print( "You passed in %s and %s" % (arg1, arg2))
    print ("I will return them to you in a list.  Here you go.")
    return (arg1, arg2)

def processAll():
    organicDirname = 'C:/Temp/uw-cmg/Spring2019/perovskiteClassifier/COM/cif_merge_organic'
    comDistanceAtom = []

    for filename in (os.listdir(organicDirname)):
        file = organicDirname + '/' + filename
        # cmd.load("C:/Temp/uw-cmg/Spring2019/cif_merge_organic/"+ filename)
        fileNum = filename[0:4]

        skip = ["0757", "0876"];

        if(fileNum not in skip):
            comDistanceAtom.append(process(fileNum))




    for x in comDistanceAtom:
        print(x)



    a= np.array(comDistanceAtom)

    # print(a)

    # np.savetxt("rAff.csv", a, delimiter=",")
    pd.DataFrame(a).to_csv("./rAff.csv")
    print ("End")



cmd.extend( "processAll", processAll);

cmd.extend ("processCOM", process)




# cd C:\Temp\uw-cmg\Summer2018\perovskiteClassifier\COM
# run drawBoundingBox.py
# load 0001.cif
# drawBoundingBox 0001, r=0.33, g=0.80
#
#
#
# #get center of mass
# centerofmass
#
# #create market at location
# pseudoatom com,  pos=[   1.996,   3.092,   1.834]
#
#
# #get edges
# ([minX, minY, minZ],[maxX, maxY, maxZ]) = cmd.get_extent(selection="(0001)")
#
# #create market at min edge
# pseudoatom minEdge,  pos=[-0.6372281908988953, 1.3493894338607788, 0.556567907333374]
#
# #create market at max edge
# pseudoatom minEdge,  pos=[4.362415790557861, 5.122246265411377, 4.327941417694092]
#
# run distancetoatom.py
#
# # input param is the COM and returns a list with all the atoms distance.
# distancetoatom [2.373,2.451,3.272]
#
#
# # draws line between /com selection and the last element
# distance  /com, /0001///`0/F13`
#
# #python api for distance
# dst = cmd.distance ('temp', '/com', '/0001///`0/F13`')
#
#
#
#
# //IDEA
# iterate through each of the atoms in the compound
# find the magnitude of vector from COM to ATOM position
#
#
#
# # lists index of all the selections
# list = cmd.index(selection="(all)")
