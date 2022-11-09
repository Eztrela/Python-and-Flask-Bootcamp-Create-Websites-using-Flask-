from basic import db,Puppy


# CREATE ALL THE TABLES Model --> Db Table
db.create_all()

sam = Puppy('sammy',3)
frank = Puppy('Frankie',4)

# None
# None
print(sam.id)
print(frank.id)

# NEXT 3 LINES ARE THE SAME
db.session.add_all([sam,frank])

# db.session.add(sam)
# db.session.add(frank)

db.session.commit()

print(sam.id)
print(frank.id)
