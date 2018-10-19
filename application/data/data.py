class Data:
    
    @staticmethod
    def allProducts():
        return [
            {
                "product_id": 1,
                "name": "Trousers",
                "quantity": 500,
                "minQuantity": 250,
                "productDateAdded": "20:30 03-Jan-2018"
            },
            {
                "product_id": 2, 
                "name": "Shirt",
                "quantity": 1000,
                "minQuantity": 150,
                "productDateAdded": "20:30 03-Feb-2018"
            },
            {
                "product_id": 3, 
                "name": "Shoes",
                "quantity": 200,
                "minQuantity": 20,
                "productDateAdded": "20:30 03-Mar-2018"
            },
            {
                "product_id": 4, 
                "name": "Jackets",
                "quantity": 100,
                "minQuantity": 75,
                "productDateAdded": "20:30 03-Apr-2018"
            }
        ]


    @staticmethod
    def allSales():
        return [
            {
                "sale_id": 1,
                "name": "Trousers",
                "quantity": 50,
                "price": 10,
                "salesAddedDate": "20:30 02-Jan-2018"
            },
            {
                "sale_id": 2,
                "name": "Shirts",
                "quantity": 20,
                "price": 20,
                "salesAddedDate": "20:30 02-Feb-2018"
            },
            {
                "sale_id": 3,
                "name": "Shoes",
                "quantity": 10,
                "price": 50,
                "salesAddedDate": "20:30 02-Mar-2018"
            },
            {
                "sale_id": 4,
                "name": "Jackets",
                "quantity": 20,
                "price": 70,
                "salesAddedDate": "20:30 02-Apr-2018"
            }
        ]
