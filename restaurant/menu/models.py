from django.db import models

# Create your models here.
class MenuItem(models.Model):
    title = models.CharField(max_length=200, unique=True)
    price = models.FloatField(default=0.00)

    def __str__(self):
        return f'title={self.title}; price={self.price}'
    
    def get_absolute_url(self):
        return '/menu'
    
    def available(self):
        return all(X.enough for X in self.reciperequirement_set.all())
    

class Ingredient(models.Model):
    name = models.CharField(max_length=200, unique=True)
    quantity = models.FloatField(default=0)
    unit = models.CharField(max_length=200)
    price_per_unit = models.FloatField(default=0)

    def __str__(self):
        return f"""
        name={self.name};
        quantity={self.quantity};
        unit={self.unit};
        unit_price={self.price_per_unit}
        """
    
    def get_absolute_url(self):
        return '/ingredients'
    
class RecipeRequirement(models.Model):
    menu_item = models.ForeignKey(MenuItem, on_delete=models.CASCADE)
    ingredient = models.ForeignKey(Ingredient, on_delete=models.CASCADE)
    quantity = models.FloatField(default=0)

    def __str__(self):
        return f'menu_item=[{self.menu_item.__str__()}]; ingredient={self.ingredient}'

    def enough(self):
        return self.quantity <= self.ingredient.quantity
    
    def get_absolute_url(self):
     return '/menu'
    

class Purchase(models.Model):
    menu_item = models.ForeignKey(MenuItem, on_delete=models.CASCADE)
    timestamp = models.DateField(auto_now_add=True)

    def __str__(self):
        return f'menu_item=[{self.menu_item.__str__()}]; time={self.timesstamp}'
    
    def get_absolute_url(self):
        return '/purchases'
