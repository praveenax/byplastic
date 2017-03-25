from backend_app import db
from backend_app import app

import sys
import traceback


class User(db.Model):
    __tablename__ = 'plastic_user'
    id = db.Column(db.Integer, primary_key=True)
    user_name = db.Column(db.String(255))
    category = db.Column(db.String(255))
    location = db.Column(db.String(255))
    status = db.Column(db.Integer)
    contact_id = db.Column(db.String(255))
    created_at = db.Column(db.TIMESTAMP)
    modified_at = db.Column(db.TIMESTAMP)

    def __init__(self, user_name, category, location, status, contact_id, created_at, modified_at):
        self.user_name = user_name
        self.category = category
        self.location = location
        self.status = status
        self.contact_id = contact_id
        self.created_at = created_at
        self.modified_at = modified_at

    @staticmethod
    def save(user):
        try:
            db.session.add(user)
            #db.session.commit()
            db.session.flush()
        except:
            exc_type, exc_value, exc_traceback = sys.exc_info()
            lines = traceback.format_exception(exc_type, exc_value, exc_traceback)
            app.logger.error("Error saving user object to db. {0}".format(lines))

    @staticmethod
    def get_all_active_users():
        try:
            user = User.query.filter_by(status=1).all()
            return user
        except:
            exc_type, exc_value, exc_traceback = sys.exc_info()
            lines = traceback.format_exception(exc_type, exc_value, exc_traceback)
            app.logger.error("Error getting users {0}".format(lines))
            return None

    @staticmethod
    def get_user(id):
        try:
            return User.query.filter_by(id=id).first()
        except:
            exc_type, exc_value, exc_traceback = sys.exc_info()
            lines = traceback.format_exception(exc_type, exc_value, exc_traceback)
            app.logger.error("Error getting user object for user {0} {1}".format(id, lines))
            return None


class Product(db.Model):

    __tablename__ = 'plastic_product'
    id = db.Column(db.Integer, primary_key=True)
    product_name = db.Column(db.String(255))
    category = db.Column(db.String(255))
    subcategory = db.Column(db.String(255))
    description = db.Column(db.String(1024))
    user_id = db.Column(db.Integer)
    min_price = db.Column(db.Decimal(10, 3))
    price = db.Column(db.Decimal(10, 3))
    is_auctionable = db.Column(db.Boolean)
    status = db.Column(db.Integer)
    created_at = db.Column(db.TIMESTAMP)
    modified_at = db.Column(db.TIMESTAMP)

    def __init__(self, product_name, category, subcategory, description, user_id, min_price, price, is_auctionable, status, created_at, modified_at):
        self.product_name = product_name
        self.category = category
        self.subcategory = subcategory
        self.description = description
        self.user_id = user_id
        self.min_price = min_price
        self.price = price
        self.is_auctionable = is_auctionable
        self.status = status
        self.created_at = created_at
        self.modified_at = modified_at

    @staticmethod
    def save(product):
        try:
            db.session.add(product)
            #db.session.commit()
            db.session.flush()
        except:
            exc_type, exc_value, exc_traceback = sys.exc_info()
            lines = traceback.format_exception(exc_type, exc_value, exc_traceback)
            app.logger.error("Error saving product object to db. {0}".format(lines))

    @staticmethod
    def get_all_active_products():
        try:
            product = Product.query.filter_by(status=1).all()
            return product
        except:
            exc_type, exc_value, exc_traceback = sys.exc_info()
            lines = traceback.format_exception(exc_type, exc_value, exc_traceback)
            app.logger.error("Error getting products {0}".format(lines))
            return None

    @staticmethod
    def get_product(id):
        try:
            return Product.query.filter_by(id=id).first()
        except:
            exc_type, exc_value, exc_traceback = sys.exc_info()
            lines = traceback.format_exception(exc_type, exc_value, exc_traceback)
            app.logger.error("Error getting product object for product {0} {1}".format(id, lines))
            return None


class ProductTxn(db.Model):
    __tablename__ = 'plastic_product_txn'
    id = db.Column(db.Integer, primary_key=True)
    product_id = db.Column(db.Integer)
    buyer_id = db.Column(db.Integer)
    seller_id = db.Column(db.Integer)

    def __init__(self, product_id, buyer_id, seller_id):
        self.product_id = product_id
        self.buyer_id = buyer_id
        self.seller_id = seller_id

    @staticmethod
    def save(product_txn):
        try:
            db.session.add(product_txn)
            #db.session.commit()
            db.session.flush()
        except:
            exc_type, exc_value, exc_traceback = sys.exc_info()
            lines = traceback.format_exception(exc_type, exc_value, exc_traceback)
            app.logger.error("Error saving product txn object to db. {0}".format(lines))

    @staticmethod
    def get_product_txn(id):
        try:
            return ProductTxn.query.filter_by(id=id).first()
        except:
            exc_type, exc_value, exc_traceback = sys.exc_info()
            lines = traceback.format_exception(exc_type, exc_value, exc_traceback)
            app.logger.error("Error getting product txn object for product txn id {0} {1}".format(id, lines))
            return None
