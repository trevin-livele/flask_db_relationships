#basic.py
#create entries into the tables
from os import name
from models import db,Puppy,Owner,Toy


#creating 2 puppies
rufus = Puppy('Rufus')
fido = Puppy('fido')


# add puppies to db
db.session.add_all([rufus,fido])
db.session.commit()


#check !
print(Puppy.query.all())

rufus = Puppy.query.filter_by(name='Rufus').first()

#create owner object
jose = Owner('jose',rufus.id)



#give rufus some toys
toy1 = Toy('chew toy',rufus.id)
toy2 = Toy('ball',rufus.id)


db.session.add_all([jose,toy1,toy2])
db.session.commit()

#grab rufus after the additions

rufus = Puppy.query.filter_by(name='Rufus').first()
print(rufus)

print(rufus.report_toys())