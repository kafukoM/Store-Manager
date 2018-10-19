import json 
from flask import Flask, make_response, jsonify,abort,request 

 
sale_order_records = []

class SalesModel():

         
        def getAllSales():
            if len(sale_order_records) is 0:
                return 'There are no sale_order_records records at the moment'
            else:    
                return make_response(jsonify(sale_order_records)),200

           
        def fetch_one_sale(saleId):
            sale = utils.search_sale(sale_order_records, saleId)
            if sale is None:
                abort(404)
            else:
                return make_response(jsonify(sale)),200
         
        def createSales(data):
            
            if len(sale_order_records) == 0:
                saleId = 1     
                sale_order_records.append({'saleId' : saleId,'Product Name': data.get('product_name'), 'Product Category': data.get('product_category'),'Product Quantity':data.get('product_quantity'),'total_cost':data.get('total_cost')})
                      
            else:
                last_dict = sale_order_records[len(sale_order_records)-1]
                id = int(last_dict['saleId'])
                new_id = id + 1 
                sale_order_records.append({'saleId' : new_id, 'Product Name': data.get('product_name'), 'Product Category': data.get('product_category'),'Product Quantity':data.get('product_quantity'),"total_cost":data.get('total_cost') })
            
            return make_response(jsonify(sale_order_records)),201
            
