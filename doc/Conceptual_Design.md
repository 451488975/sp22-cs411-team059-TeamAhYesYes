# Conceptual Design

## Entity-Relationsip Diagram
![](https://github-dev.cs.illinois.edu/sp22-cs411/sp22-cs411-team059-TeamAhYesYes/blob/main/doc/img/er.png?raw=true)

## ERD Description

We designed a sample relational schema for keeping track of pet adoption and supply item shopping. 

#### Entities:
- The database stores information about User, Pet, Shop, Supply Item, and Order.
- Users are able to log into member accounts with our website. A user is uniquely identified by their username. Other user attributes are password, first name, last name, email, and phone number.
- A pet is uniquely identified by its pet id. Other pet attributes are breed, age, color, size, and behavior.
- A shop is uniquely identified by its shop id. Other shop attributes are shop name and shop address.
- A supply item is uniquely identified by its item id. Other supply item attributes are type, price, and item name.
- An order is uniquely identified by its order id. Other order attributes are total price and transaction time.

#### Relationships:
- We think that a user can place multiple orders, but an order must be placed by exactly one user. 
- A user may adopt multiple pets, but a pet can have exactly one owner.
- A shop may have multiple pets, but a pet must live in exactly one shop.
- A supply item can be provided from exactly one shop, but a shop may have multiple supply items.
  - This might have some confusion that why one supply item can only be provided from exactly one shop. Take eBay as an example, you can search for one product by its name and get many results from different sellers, but the actual item id they have in their shops should be different. That is why we chose to have an one-to-many relationship between items and shops.
- An order may contain multiple supply items, and a supply item may have multiple orders.


## Logical Design
    Customer(
        customer_id:INT [PK]
        username:VARCHAR(50),
        password:VARCHAR(50),
        email:VARCHAR(100),
        first_name:VARCHAR(50),
        last_name:VARCHAR(50),
        phone_number:VARCHAR(50)
    )

    Shop(
        shop_id:INT [PK],
        shop_name:VARCHAR(50),
        shop_address:VARCHAR(50)
    )

    Pet(
        pet_id:INT [PK],
        shop_id:INT [FK to Shop.shop_id],
        customer_id:VARCHAR(50) [FK to Customer.customer_id],
        color:VARCHAR(50),
        type:VARCHAR(50),
        age:INT,
        breed:VARCHAR(100)
    )

    Item(
        item_id:INT [PK], 
        shop_id:INT [FK to Shop.shop_id], 
        item_name:VARCHAR(50), 
        type:VARCHAR(50),
        price:REAL
    )

    Order(
        order_id:INT [PK], 
        customer_id:VARCHAR [FK to Customer.customer_id],
        total_price:REAL, 
        transaction_time:DATETIME
    )

    Contains(
        item_id:INT [PK] [FK to Item.item_id],
        order_id:INT [PK] [FK to Order.order_id],
        quantity:INT
    )
