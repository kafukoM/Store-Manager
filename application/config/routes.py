from app.controllers.control_product import ProductsController
from app.controllers.control_sales import SalesController

class Routes:
    

    @staticmethod
    def fetchRoutes(app):
        """
        static method for fetching all routes
        """
        
        #products endpoints
        app.add_url_rule('/api/v1/products/', view_func=ProductsController.as_view('getProducts'), methods=['GET'], strict_slashes=False)
        app.add_url_rule('/api/v1/products/<int:product_id>', view_func=ProductsController.as_view('getSingleProduct'), methods=['GET'], strict_slashes=False)
        app.add_url_rule('/api/v1/products/', view_func=ProductsController.as_view('createProduct'), methods=['POST'], strict_slashes=False)

        #sales endpoints
        app.add_url_rule('/api/v1/sales/', view_func=SalesController.as_view('getSales'), methods=['GET'], strict_slashes=False)
        app.add_url_rule('/api/v1/sales/<int:sale_id>', view_func=SalesController.as_view('getSingleSale'), methods=['GET'], strict_slashes=False)
        app.add_url_rule('/api/v1/sales/', view_func=SalesController.as_view('createSale'), methods=['POST'], strict_slashes=False)   
