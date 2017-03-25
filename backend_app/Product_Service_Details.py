from backend_app import Utils
from models import Product
from models import User
from models import ProductTxn

class Seller_Service_Class:

    def add_the_product(self, product_dict):
        cdt = Utils.currentdatetime()
        product_name = product_dict["product_name"]
        category = product_dict["category"]
        subcategory = product_dict["subcategory"]
        description = product_dict["description"]
        user_id = product_dict["user_id"]
        min_price = product_dict["min_price"]
        price = product_dict["price"]
        created_at = product_dict["cdt"]
        product = Product()
        return Product.save(product)

    def get_product_for_user_id(self,user_dict):
        user_id = user_dict["user_id"]
        return Product.get_product(user_id)

    def get_sold_products_history(self,user_dict):
        user_id = user_dict["user_id"]
        if Product.status == 1:
            return Product.get_product(user_id)

    def get_bought_products_history(self,buyer_dict):
        buyer_id = buyer_dict["buyer_id"]
        return ProductTxn.get_product_Txn(buyer_id)

    def search_all_active_products(self):
        return Product.get_all_active_products()

    def search_by_category(self):
        return Product.get_products_by_criteria(product_name= None,category=None,subcategory=None,description=None,min_price=None,price=None)

    def active_users(self):
        return User.get_all_active_users()

    def add_an_user(self,user_dict):
        user_name = user_dict["user_name"]
        category = user_dict["category"]
        location = user_dict["location"]
        contact_id = user_dict["contact_id"]
        cdt = Utils.currentdatetime()
        created_at = user_dict["cdt"]
        user = User()
        return User.save(user)















