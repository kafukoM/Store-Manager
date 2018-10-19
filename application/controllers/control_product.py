from flask import request, jsonify
from flask.views import MethodView
from app.models.product_model import ProductModel
from app.config.data_valid import DataValidation

class ProductsController(MethodView):
    """
    Products controller that inherits the method view
    """
    
    allProducts = ProductModel.getProductsData()

    def get(self, product_id = None):
        """
        gets all 
        """
        if(product_id == None):
            return jsonify(ProductModel.getProductsData()), 200

        else:
            return ProductModel.getProductsData(product_id)
            
            
    def post(self):
        postData = request.get_json()

        postValues = DataValidation.validateProduct(postData['quantity'], postData['minQuantity'], postData['product'], postData['productDateAdded'])

        if isinstance(postValues, bool):
            dataObject = {
                "product_id": len(self.allProducts) + 1,
                "product": postData['product'],
                "quantity": postData['quantity'],
                "minQuantity": postData['minQuantity'],
                "productDateAdded": postData['productDateAdded'],
            }
            return ProductModel.createProduct(dataObject)

        else:
            return postValues
        
