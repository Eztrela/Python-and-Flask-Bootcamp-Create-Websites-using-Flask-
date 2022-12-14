#CREATE ENTRIES INTO THE TABLES!

from models import db,Puppy,Owner,Toy

rufus = Puppy('Rufus')
fido = Puppy('Fido')

# ADD PUPPIES TO DB
db.session.add_all([rufus,fido])
db.session.commit()

print(Puppy.query.all())

rufus = Puppy.query.filter_by(name='Rufus').first()

# CREATE OWNER OBJECT
jose = Owner('Jose',rufus.id)

#GIVE RUFUS SOME TOYS

toy1 = Toy('Chew Toy',rufus.id)
toy2 = Toy('Ball',rufus.id)

db.session.add_all([jose,toy1,toy2])
db.session.commit()


# GRAB RUFUS AFTER THOSE ADDITIONS
rufus = Puppy.query.filter_by(name='Rufus').first()
print(rufus)

rufus.report_toys()