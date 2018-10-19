from flask import request, jsonify
from flask.views import MethodView
from app.models.sales_model import SalesModel
from app.config.data_valid import DataValidation

class SalesController(MethodView):
    
    allSales = SalesModel.getAllSales()

    def get(self, sale_id=None):
        if sale_id == None:
            return jsonify(SalesModel.getAllSales()), 200
        else:
            return SalesModel.getAllSales(sale_id)


    def post(self):
        postData = request.get_json()

        postValues = DataValidation.validateSale(postData['quantity'], postData['price'], postData['product'], postData['salesAddedDate'])
        
        if isinstance(postValues, bool):
            dataObject = {
                "sale_id": len(self.allSales) + 1,
                "product": postData['product'],
                "quantity": postData['quantity'],
                "price": postData['price'],
                "salesAddedDate": postData['salesAddedDate'],
            }
            return SalesModel.createSales(dataObject)
        else:
            return postValues
        
