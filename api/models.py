from django.db import models

class Product(models.Model):
    productName = models.CharField(max_length=255)
    productId = models.CharField(max_length=50, unique=True)
    productPrice = models.DecimalField(max_digits=10, decimal_places=2)
    productDes = models.TextField(blank=True, null=True)
    productRating = models.FloatField()
    productDisCount = models.CharField(max_length=10, blank=True, null=True)
    productHave = models.BooleanField()
    productBrand = models.CharField(max_length=255)
    productImage = models.ImageField(upload_to='product_images/')
    productDlb = models.FileField(upload_to='product_files/')
    productCategory = models.CharField(max_length=255)
    productNote = models.CharField(max_length=255, blank=True, null=True)

    def __str__(self):
        return self.productName

class Order(models.Model):
    customerName = models.CharField(max_length=255)
    customerAddress = models.TextField()
    totalPrice = models.DecimalField(max_digits=10, decimal_places=2)
    approved = models.BooleanField(default=False)
    orderDate = models.DateTimeField(auto_now_add=True)
    products = models.ManyToManyField(Product, through='OrderItem')

    def __str__(self):
        return f'Order {self.id} by {self.customerName}'

class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField()

    def __str__(self):
        return f'{self.quantity} of {self.product.productName} in Order {self.order.id}'
