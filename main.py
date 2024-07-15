from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session
from database import engine, Base, get_db
from pydantic import BaseModel
from scraper import scrape_products_by_category
import models

# Create all the table
Base.metadata.create_all(bind=engine)

app = FastAPI()

class ProductCreate(BaseModel):
    name: str
    category: str
    price: int

# Routes
@app.get("/")
def read_root():
    return {"message": "Hello World"}

@app.get("/products/")
def get_products(db: Session = Depends(get_db)):
    try:
        products = db.query(models.Product).all()
        return products
    finally:
        return {"message": "Not found products"}
''''
@app.post("/products/")
def create_product(product: ProductCreate, db: Session = Depends(get_db)):
    db_product = models.Product(name=product.name, category=product.category, price=product.price)
    db.add(db_product)
    db.commit()
    db.refresh(db_product)

    return db_product
'''

@app.post("/scrape/")
def scrape_and_store_products(db: Session = Depends(get_db)):
    categories = ['juegos', 'lactancia', 'alimentacion', 'paseo', 'hogar-y-ajuar', 'cunas', 'bano']
    for category in categories:
        scraped_products = scrape_products_by_category(category)

        for product_data in scraped_products:
            db_product = models.product(**product_data)
            db.add(db_product)

    db.commit()
    return {"message": "Productos scraped and stored successfully"}