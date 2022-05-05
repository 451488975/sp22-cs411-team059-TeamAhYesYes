# Pet Shop Project
## Project Summary
Our project will be a web application for the Pet Shop. In this web app, users will be able to browse different pets according to their taste of type, breed, color, size, etc. There will be a detailed information page about the pets we have in the shop when users found their likes. Other than pets themselves, we also intend to include content for pet supplies, foods, toys, to make our shop a one-stop destination for all people who love pets in the Urbana-Champaign area.

## Description
This project aims to use the most authentic and reliable data to establish their own web pages for pet stores in the Urbana-Champaign area, to make these pet stores more attractive. We will combine the traditional retail industry with data to help stores build unique brands and ultimately increase the sales of pet stores. 

For the production of this website page, we will combine the knowledge learned in CS411 to build a database of pet information. And make it have the functions of adding, deleting, modifying, and querying data. For this database, we will also make a corresponding front-end to facilitate users to interact with our data. Our project will combine other knowledge beyond this class to enable our website to have a search function, more specific classification function. In general, this project will be a concentrated reflection of what we have learned in the CS411 class about database correspondence, and we will add our special ideas to make this project more practical and innovative.

## Usefulness
In our research, we found several pet shops in Champaign, Illinois. But they do not have much useful information on their website. Take [Sailfin Pet Shop](http://www.sailfin.com/) as an example, they only have photos of a few pets they have in the shop, and their website seems out-of-date about the information on their pets as well.

Take another shop [Pet Supplies Plus](https://www.petsuppliesplus.com/store/il/champaign/185-champaign/185) as an example, they have a very detailed page about merchandise like pet supplies, food, toys they have in the store, and the online shopping system they have is also very complete. However, they do not have any information about the pet, although they said they have pets in-store on the about page.

Therefore, we will address both issues and combine both functions into our web application, so users will have this one-stop shopping experience in our shop.

## Realness
Our data will be a dataset that contains a bunch of pets and also a dataset that contains tons of pet-related merchandise. The dataset will get from similar pet shops or dataset websites like "Kaggle", "Google Dataset Search" combined with some randomly generated data.

Some dataset we currently found that would fit our database are these two from Kaggle: [Shelter Animal Outcomes](https://www.kaggle.com/c/shelter-animal-outcomes/data), [PetFinder.my Adoption Prediction](https://www.kaggle.com/c/petfinder-adoption-prediction/data). They may not contain all the information we need, but we will fill blank attribute like pet's behaviors by randomly giving them values. And we will continue our research on datasets that fit best with our need. 

## Functionality
In this project, the website includes several features for users' pet business services. For the most part, our datasets are from free and open-source dataset websites such as "Kaggle", "Google Dataset Search", "Data.Gov" etc. In some cases, some sensitive data cannot be exposed to the public. Therefore, randomly generated data are needed. 

Administrators have permission to manage the database of websites and keep track of store inventory and pets. For example, administrators will be able to insert, delete, query, and update inventories in the pet suppliers database and pets for adoption. Customers will be able to get the ideal result by inputting their keywords.

#### About Page
The about page has an overview of our pet shop, which is well-represented throughout our website. Moreover, this page incorporates a brand logo and elements from it throughout the site. The detailed information about the Pet Shop and staff will be stored in the database.

#### Pet Finder
Pet Finder is a searchable database and interactive function for nearly all pet shelters to find pets available for adoption. Users are allowed to search out what type of cats they like according to different options such as breed, age, size, color, coat length, behavior, etc. Age will be stored as INTEGER type; breed, size, color, coat length, and behavior will be stored as VARCHAR type. 

#### Pet Supplies
For this function, users can purchase and browse some pet supplies we offer. The Pet Supplies database, for instance, includes pet food, toys, and litter. Also, the detail page contains the price and picture for each product.

#### Special Events
"Special Events" is a fancy creative function that can bring good cheer, a sense of purpose, and unexpected surprise to customers in our pet shop. The system will automatically generate a "mysterious box" for customers who do not have particular preferences. The mysterious box will be based on some factors like page views of pets, the recent history of the particular customer. 

## UI
Pet Finder
![](https://github-dev.cs.illinois.edu/sp22-cs411/sp22-cs411-team059-TeamAhYesYes/blob/main/doc/img/front.png?raw=true)

Special Events
![](https://github-dev.cs.illinois.edu/sp22-cs411/sp22-cs411-team059-TeamAhYesYes/blob/main/doc/img/mystery.png?raw=true)

Product Information
![](https://github-dev.cs.illinois.edu/sp22-cs411/sp22-cs411-team059-TeamAhYesYes/blob/main/doc/img/product.png?raw=true)

## Project Work Distribution
River Liu & Siyuan Zhao: Pet Finder & Special Events

Zexiang Chen & Sean Zhang: Pet Supplies & Front Page & About Page
