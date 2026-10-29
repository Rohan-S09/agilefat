from flask import Flask, request, jsonify, render_template_string

app = Flask(__name__)

def calculate_total(price, quantity, discount_percent=0):
    if price < 0 or quantity < 0 or not (0 <= discount_percent <= 100):
        raise ValueError("Invalid input values")
    subtotal = price * quantity
    discount_amount = subtotal * (discount_percent / 100.0)
    return subtotal - discount_amount

# Simple interactive HTML UI served directly from python
HTML_FORM = """
<!DOCTYPE html>
<html>
<head>
    <title>Shopping Bill Calculator</title>
    <style>
        body { font-family: Arial, sans-serif; margin: 50px; background-color: #f4f4f9; }
        .card { background: white; padding: 30px; border-radius: 8px; box-shadow: 0 4px 8px rgba(0,0,0,0.1); max-width: 400px; }
        input { width: 95%; padding: 10px; margin: 10px 0; border: 1px solid #ccc; border-radius: 4px; }
        button { width: 100%; padding: 10px; background-color: #28a745; color: white; border: none; border-radius: 4px; cursor: pointer; font-size: 16px; }
        .result { margin-top: 20px; font-weight: bold; color: #333; font-size: 18px; }
    </style>
</head>
<body>
    <div class="card">
        <h2>🛍️ Shopping Bill Calculator</h2>
        <form method="POST" action="/calculate">
            <label>Item Price ($):</label>
            <input type="number" step="0.01" name="price" required min="0">
            <label>Quantity:</label>
            <input type="number" name="quantity" required min="0">
            <label>Discount (%):</label>
            <input type="number" step="0.1" name="discount" value="0" min="0" max="100">
            <button type="submit">Calculate Bill</button>
        </form>
        {% if total is not none %}
        <div class="result">Discounted Total Bill: ${{ "%.2f"|format(total) }}</div>
        {% endif %}
        {% if error %}
        <div class="result" style="color: red;">Error: {{ error }}</div>
        {% endif %}
    </div>
</body>
</html>
"""

@app.route('/', methods=['GET'])
def home():
    return render_template_string(HTML_FORM, total=None)

@app.route('/calculate', methods=['POST'])
def calculate():
    try:
        price = float(request.form.get('price', 0))
        quantity = int(request.form.get('quantity', 0))
        discount = float(request.form.get('discount', 0))
        total = calculate_total(price, quantity, discount)
        return render_template_string(HTML_FORM, total=total)
    except Exception as e:
        return render_template_string(HTML_FORM, total=None, error=str(e))

if __name__ == "__main__":
    # The application runs on port 8000 inside the container
    app.run(host="0.0.0.0", port=8000)
