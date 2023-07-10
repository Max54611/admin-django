# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models

class Section(models.Model):
    section_id = models.IntegerField(primary_key=True)
    section_name = models.CharField(max_length=255, blank=True, null=True)
    def __str__(self):
        return self.section_name
    class Meta:
        managed = False
        db_table = 'section'


class SectionSequence(models.Model):
    next_val = models.BigIntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'section_sequence'

class Category(models.Model):
    category_id = models.IntegerField(primary_key=True)
    category_name = models.CharField(max_length=255, blank=True, null=True)
    image_url = models.CharField(max_length=255, blank=True, null=True)
    section_section = models.ForeignKey('Section', models.DO_NOTHING, blank=True, null=True)
    def __str__(self):
        return self.category_name
    class Meta:
        managed = False
        db_table = 'category'


class CategorySequence(models.Model):
    next_val = models.BigIntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'category_sequence'

class OrderItem(models.Model):
    order_item_id = models.IntegerField(primary_key=True)
    image_url = models.CharField(max_length=255, blank=True, null=True)
    order_date = models.DateTimeField(blank=True, null=True)
    product_id = models.IntegerField(blank=True, null=True)
    product_name = models.CharField(max_length=255, blank=True, null=True)
    quantity = models.IntegerField(blank=True, null=True)
    total_price = models.IntegerField(blank=True, null=True)
    user_user = models.ForeignKey('User', models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'order_item'


class OrderItemSeq(models.Model):
    next_val = models.BigIntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'order_item_seq'


class Product(models.Model):
    product_id = models.IntegerField(primary_key=True)
    description = models.CharField(max_length=1000, blank=True, null=True)
    image_url = models.CharField(max_length=255, blank=True, null=True)
    marked_price = models.IntegerField(blank=True, null=True)
    product_name = models.CharField(max_length=255, blank=True, null=True)
    review_count = models.IntegerField(blank=True, null=True)
    selling_price = models.IntegerField(blank=True, null=True)
    total_rating = models.IntegerField(blank=True, null=True)
    category_category = models.ForeignKey(Category, models.DO_NOTHING, blank=True, null=True)
    def __str__(self):
        return self.product_name
    class Meta:
        managed = False
        db_table = 'product'


class ProductSequence(models.Model):
    next_val = models.BigIntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'product_sequence'


class Review(models.Model):
    review_id = models.IntegerField(primary_key=True)
    created_at = models.DateTimeField(blank=True, null=True)
    rating = models.IntegerField(blank=True, null=True)
    text = models.CharField(max_length=255, blank=True, null=True)
    user_id = models.IntegerField(blank=True, null=True)
    user_name = models.CharField(max_length=255, blank=True, null=True)
    product_product = models.ForeignKey(Product, models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'review'


class ReviewSequence(models.Model):
    next_val = models.BigIntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'review_sequence'


class User(models.Model):
    user_id = models.IntegerField(primary_key=True)
    email = models.CharField(max_length=255, blank=True, null=True)
    password = models.CharField(max_length=255, blank=True, null=True)
    user_name = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'user'


class UserSeq(models.Model):
    next_val = models.BigIntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'user_seq'
