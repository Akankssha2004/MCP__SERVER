
from fastmcp import FastMCP

mcp = FastMCP(
    "Amazon E-commerce",
    stateless_http=True
)


@mcp.tool
def search_products():
    """Returns the available Amazon products."""
    return [
        "Mobiles",
        "Laptops",
        "Headphones",
        "SmartWatches",
        "SmartBands"
    ]


@mcp.tool
def get_offers():
    """Returns the product offer details."""
    return {
        "Mobiles": "10%",
        "Laptops": "35%",
        "Headphones": "12%"
    }


@mcp.tool
def order_status():
    """Returns the delivery status."""
    return "The product is delivered."


@mcp.tool
def payment():
    """Returns the payment status."""
    return "Payment completed."


if __name__ == "__main__":
    mcp.run(
        transport="http",
        host="0.0.0.0",
        port=5001
    )
