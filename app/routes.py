from flask import render_template, request, redirect, url_for, flash
from app import app, db
from app.models import Customer, Order, Product, OrderItem


@app.route("/customers")
def list_customers():
    customers = Customer.query.all()
    return render_template("list_customers.html", customers=customers)


@app.route("/customers/add", methods=["GET", "POST"])
def add_customer():
    if request.method == "POST":
        name = request.form["name"]
        email = request.form["email"]
        address = request.form.get("address")
        phone = request.form.get("phone")

        new_customer = Customer(name=name, email=email, address=address, phone=phone)
        db.session.add(new_customer)
        db.session.commit()

        flash("Cliente adicionado com sucesso!")
        return redirect(url_for("list_customers"))

    return render_template("add_customer.html")


@app.route("/customers/edit/<int:id>", methods=["GET", "POST"])
def edit_customer(id):
    customer = Customer.query.get_or_404(id)

    if request.method == "POST":
        customer.name = request.form["name"]
        customer.email = request.form["email"]
        customer.address = request.form.get("address")
        customer.phone = request.form.get("phone")

        db.session.commit()

        flash("Cliente atualizado com sucesso!")
        return redirect(url_for("list_customers"))

    return render_template("edit_customer.html", customer=customer)


@app.route("/customers/delete/<int:id>", methods=["POST"])
def delete_customer(id):
    customer = Customer.query.get_or_404(id)
    db.session.delete(customer)
    db.session.commit()

    flash("Cliente excluído com sucesso!")
    return redirect(url_for("list_customers"))


@app.route("/products")
def list_products():
    products = Product.query.all()
    return render_template("list_products.html", products=products)


@app.route("/products/add", methods=["GET", "POST"])
def add_product():
    if request.method == "POST":
        name = request.form["name"]
        description = request.form.get("description")
        price = request.form["price"]
        stock = request.form["stock"]

        new_product = Product(
            name=name, description=description, price=price, stock=stock
        )
        db.session.add(new_product)
        db.session.commit()

        flash("Produto adicionado com sucesso!")
        return redirect(url_for("list_products"))

    return render_template("add_product.html")


@app.route("/products/edit/<int:id>", methods=["GET", "POST"])
def edit_product(id):
    product = Product.query.get_or_404(id)

    if request.method == "POST":
        product.name = request.form["name"]
        product.description = request.form.get("description")
        product.price = request.form["price"]
        product.stock = request.form["stock"]

        db.session.commit()

        flash("Produto atualizado com sucesso!")
        return redirect(url_for("list_products"))

    return render_template("edit_product.html", product=product)


@app.route("/products/delete/<int:id>", methods=["POST"])
def delete_product(id):
    product = Product.query.get_or_404(id)
    db.session.delete(product)
    db.session.commit()

    flash("Produto excluído com sucesso!")
    return redirect(url_for("list_products"))


@app.route("/orders")
def list_orders():
    orders = Order.query.all()
    return render_template("list_orders.html", orders=orders)


@app.route("/orders/add", methods=["GET", "POST"])
def add_order():
    if request.method == "POST":
        customer_id = request.form["customer_id"]
        status = request.form.get("status", "Pendente")

        new_order = Order(customer_id=customer_id, status=status)
        db.session.add(new_order)
        db.session.commit()

        flash("Pedido adicionado com sucesso!")
        return redirect(url_for("list_orders"))

    customers = Customer.query.all()
    return render_template("add_order.html", customers=customers)


@app.route("/orders/edit/<int:id>", methods=["GET", "POST"])
def edit_order(id):
    order = Order.query.get_or_404(id)

    if request.method == "POST":
        order.status = request.form.get("status", "Pendente")

        db.session.commit()

        flash("Pedido atualizado com sucesso!")
        return redirect(url_for("list_orders"))

    customers = Customer.query.all()
    return render_template("edit_order.html", order=order, customers=customers)


@app.route("/orders/delete/<int:id>", methods=["POST"])
def delete_order(id):
    order = Order.query.get_or_404(id)
    db.session.delete(order)
    db.session.commit()

    flash("Pedido excluído com sucesso!")
    return redirect(url_for("list_orders"))


@app.route("/order_items/add", methods=["GET", "POST"])
def add_order_item():
    if request.method == "POST":
        order_id = request.form["order_id"]
        product_id = request.form["product_id"]
        quantity = request.form["quantity"]
        price = request.form["price"]

        new_item = OrderItem(
            order_id=order_id, product_id=product_id, quantity=quantity, price=price
        )
        db.session.add(new_item)
        db.session.commit()

        flash("Item adicionado ao pedido com sucesso!")
        return redirect(url_for("list_orders"))

    orders = Order.query.all()
    products = Product.query.all()
    return render_template("add_order_item.html", orders=orders, products=products)


@app.route("/order_items/delete/<int:id>", methods=["POST"])
def delete_order_item(id):
    item = OrderItem.query.get_or_404(id)
    db.session.delete(item)
    db.session.commit()

    flash("Item excluído do pedido com sucesso!")
    return redirect(url_for("list_orders"))
