# -*- coding: utf-8 -*-
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from database_setup import Category, Base, CategoryItem, User

engine = create_engine('sqlite:///itemcatalog.db')
# Bind the engine to the metadata of the Base class so that the
# declaratives can be accessed through a DBSession instance
Base.metadata.bind = engine

DBSession = sessionmaker(bind=engine)
# A DBSession() instance establishes all conversations with the database
# and represents a "staging zone" for all the objects loaded into the
# database session object. Any change made against the objects in the
# session won't be persisted into the database until you call
# session.commit(). If you're not happy about the changes, you can
# revert all of them back to the last commit by calling
# session.rollback()
session = DBSession()

#Create demo user
user1 = User(name= "Mawhiba", email= "princess-meme1@hotmail.com")
session.add(user1)
session.commit()


# Category
category1 = Category(user_id=1, name="Vegetables and Legumes")

session.add(category1)
session.commit()

categoryItem1 = CategoryItem(user_id=1, name="Broccoli", description="One of broccoli biggest advantages is its nutrient content. It is loaded with a wide array of vitamins, minerals, fiber and other bioactive compounds.", category=category1)

session.add(categoryItem1)
session.commit()


categoryItem2 = CategoryItem(user_id=1, name="Spinach", description="Spinach is a superfood. It is loaded with tons of nutrients in a low-calorie package. Dark, leafy greens like spinach are important for skin, hair, and bone health. They also provide protein, iron, vitamins, and minerals.", category=category1)

session.add(categoryItem2)
session.commit()

categoryItem3 = CategoryItem(user_id=1, name="Potato", description="Potatoes are edible tubers, available worldwide and all year long. They are relatively cheap to grow, rich in nutrients, and they can make a delicious treat.", category=category1)

session.add(categoryItem3)
session.commit()


category2 = Category(user_id=1, name="Fruit")

session.add(category2)
session.commit()


categoryItem4 = CategoryItem(user_id=1, name="Apple", description="A study on the benefits of apples shows that drinking apple juice could keep Alzheimer away and fight the effects of aging on the brain.", category=category2)

session.add(categoryItem4)
session.commit()

categoryItem5 = CategoryItem(user_id=1, name="Peache", description="According to a study from Texas A&M, stone fruit like peaches, plums, and nectarines have been shown to ward off obesity-related diseases such as diabetes, metabolic syndrome, and cardiovascular disease.", category=category2)

session.add(categoryItem5)
session.commit()


categoryItem6 = CategoryItem(user_id=1, name="Orange", description="Oranges are low in calories and full of nutrients, they promote clear, healthy, skin and can help to lower our risk for many diseases as part of an overall healthy and varied diet.", category=category2)

session.add(categoryItem6)
session.commit()


category3 = Category(user_id=1, name="Grain (cereal) foods")

session.add(category2)
session.commit()


categoryItem7 = CategoryItem(user_id=1, name="Breads", description="White bread is fortified with calcium and four medium slices per day would provide over 30% of the recommended daily intake of calcium which we need every day to maintain healthy bones and teeth.", category=category3)

session.add(categoryItem7)
session.commit()

categoryItem8 = CategoryItem(user_id=1, name="Breakfast Cereals", description="The benefits of eating nutritious cereal for breakfast go beyond staying full and avoiding obesity.", category=category3)

session.add(categoryItem8)
session.commit()


categoryItem9 = CategoryItem(user_id=1, name="Pasta", description="Pasta is a perfect foundation for healthy, nutritious and satisfying meals: pasta is generally eaten with nutrient-dense food partners, such as fiber-filled vegetables and beans, heart healthy fish and monounsaturated oils, antioxidant-rich tomato sauce and protein-packed cheeses, poultry and lean meats.", category=category3)

session.add(categoryItem9)
session.commit()



print "added menu items!"
