from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from django.core.files.uploadedfile import SimpleUploadedFile
from .models import Product, ProductVariant

class ProductTests(APITestCase):
    def setUp(self):
        self.product_data = {
            'name': 'Test Product',
            'image': None,  # We'll upload the image in the test
        }
        self.product_url = reverse('product-list-create')
        self.product_detail_url = lambda pk: reverse('product-detail', args=[pk])

    def test_create_product(self):
        # Test creating a product without an image
        response = self.client.post(self.product_url, self.product_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Product.objects.count(), 1)
        self.assertEqual(Product.objects.get().name, 'Test Product')

    def test_create_product_with_image(self):
        # Create a test image
        image = SimpleUploadedFile("test_image.jpg", b'\x00\x01\x02', content_type="image/jpeg")
        self.product_data['image'] = image
        
        # Test creating a product with an image
        response = self.client.post(self.product_url, self.product_data, format='multipart')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Product.objects.count(), 1)
        self.assertTrue(Product.objects.get().image)

    def test_list_products(self):
        # Create products
        Product.objects.create(name='Product 1')
        Product.objects.create(name='Product 2')
        response = self.client.get(self.product_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 2)

    def test_retrieve_product(self):
        product = Product.objects.create(name='Product 3')
        response = self.client.get(self.product_detail_url(product.pk))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['name'], 'Product 3')

    def test_update_product(self):
        product = Product.objects.create(name='Product 4')
        update_data = {'name': 'Updated Product 4'}
        response = self.client.put(self.product_detail_url(product.pk), update_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(Product.objects.get().name, 'Updated Product 4')

    def test_delete_product(self):
        product = Product.objects.create(name='Product 5')
        response = self.client.delete(self.product_detail_url(product.pk))
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Product.objects.count(), 0)


class ProductVariantTests(APITestCase):
    def setUp(self):
        self.product = Product.objects.create(name='Test Product')
        self.variant_data = {
            'sku': 'SKU123',
            'name': 'Variant 1',
            'price': '19.99',
            'details': 'Details of product variant',
            'product': self.product.id,  # Use the product ID
        }
        self.variant_url = reverse('variant-list-create')
        self.variant_detail_url = lambda pk: reverse('variant-detail', args=[pk])

    def test_create_product_variant(self):
        # Test creating a product variant
        response = self.client.post(self.variant_url, self.variant_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(ProductVariant.objects.count(), 1)
        self.assertEqual(ProductVariant.objects.get().sku, 'SKU123')

    def test_list_product_variants(self):
        ProductVariant.objects.create(**self.variant_data)
        response = self.client.get(self.variant_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)

    def test_retrieve_product_variant(self):
        variant = ProductVariant.objects.create(**self.variant_data)
        response = self.client.get(self.variant_detail_url(variant.pk))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['sku'], 'SKU123')

    def test_update_product_variant(self):
        variant = ProductVariant.objects.create(
            sku='SKU124',
            name='Variant 2',
            price='29.99',
            details='Details of product variant',
            product=self.product
        )
        update_data = {
            'name': 'Updated Variant 2',
            'product': self.product.id,  # Use product ID
        }
        response = self.client.put(self.variant_detail_url(variant.pk), update_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(ProductVariant.objects.get().name, 'Updated Variant 2')

    def test_delete_product_variant(self):
        variant = ProductVariant.objects.create(**self.variant_data)
        response = self.client.delete(self.variant_detail_url(variant.pk))
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(ProductVariant.objects.count(), 0)
