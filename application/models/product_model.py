import json 
from flask import Flask, make_response, jsonify,abort,request 

products_list = []

class ProductModel():
        
        
        def getProductsData():
            if len(products_list) is 0:
                return 'There are no products at the moment'
            else:
                return make_response(jsonify(products_list)),200
        
        
        def fetch_one_product(productId):
            product = utils.search_product(products_list, productId)
            if product is None:
                abort(404)
            else:
                return make_response(jsonify(product)),200
        
        
        def create_product(data):
            
            if len(products_list) == 0:
                productId = 1     
                products_list.append({'product_id' : productId,'Product Name': data.get('name'), 'Product Price':data.get('price')})
                      
            else:
                last_dict = products_list[len(products_list)-1]
                id = int(last_dict['product_id'])
                new_id = id + 1 
                products_list.append({'product_id' : new_id, 'Product Name': data.get('name')})
            
            return make_response(jsonify(products_list)),201
