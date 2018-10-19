from flask import jsonify

class DataValidation():
    
    @staticmethod
    def product_int_values(quantity, minQuantity):
        if isinstance(quantity, int) and isinstance(minQuantity, int):
            return True
        else:
            return False

    @staticmethod
    def product_str_values(product, description, productDateAdded):
        if isinstance(product, str) and isinstance(description, str) and isinstance(productDateAdded, str):
            return True
        else:
            return False

    @staticmethod
    def product_empty(quantity, minQuantity, product, description, productDateAdded):
        if quantity != "" and minQuantity != "" and product != "" and description != "" and productDateAdded != "":
            return True
        else:
            return False

    @staticmethod
    def validateProduct(quantity, minQuantity, product, description, productDateAdded):
        if DataValidation.product_empty(quantity, minQuantity, product, description, productDateAdded):
            if DataValidation.product_str_values(product, description, productDateAdded):
                if DataValidation.product_int_values(quantity, minQuantity):
                    return True
                else:
                    return jsonify({"status":"Bad Request", "message": "quanity and minQuantity fields should be integers"}), 400
            else:
                return jsonify({"status":"Bad Request", "message": "product, description, and productDateAdded fields should be strings"}), 400
        else:
            return jsonify({"status":"Bad Request", "message": "No field should be empty"}), 400
    
    
    
    
    
    @staticmethod
    def sales_int_values(quantity, price):
        if isinstance(quantity, int) and isinstance(price, int):
            return True
        else:
            return False

    @staticmethod
    def sales_str_values(product, salesDateAdded):
        if isinstance(product, str) and isinstance(salesDateAdded, str):
            return True
        else:
            return False

    @staticmethod
    def sales_empty(quantity, price, product, salesDateAdded):
        if quantity != "" and price != "" and product != "" and salesDateAdded != "":
            return True
        else:
            return False

    @staticmethod
    def validateSale(quantity, price, product, salesDateAdded):
        if DataValidation.sales_empty(quantity, price, product, salesDateAdded):
            if DataValidation.sales_str_values(product, salesDateAdded):
                if DataValidation.sales_int_values(quantity, price):
                    return True
                else:
                    return jsonify({"status":"Bad Request", "message": "quanity and price fields should be integers"}), 400
            else:
                return jsonify({"status":"Bad Request", "message": "product, and salesDateAdded fields should be strings"}), 400
        else:
            return jsonify({"status":"Bad Request", "message": "No field should be empty"}), 400
