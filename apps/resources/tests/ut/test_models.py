from django.test import TestCase
from apps.resources import models

# Test Case class # Test<model-name>model
class TestTagModel(TestCase):
    def setUp(self) -> None:
        self.tag_name = 'Python'
        self.tag = models.Tag(name=self.tag_name)
        
    # unit test 1 # test_<logic-name>
    def test_create_tag_object_successful(self):
        # chk if object created is of instance tag
        self.assertIsInstance(self.tag, models.Tag)
        
    # unit test 2 
    def test_dunder_str(self):
        # str(self.tag) or self.tag.__str__()
        self.assertEqual(str(self.tag), self.tag_name)
        
class TestCategoryModel(TestCase):
    def setUp(self) -> None:
        self.cat_name = 'Python11'
        self.cat = models.Category(cat=self.cat_name)
    
    # unit test 1
    def test_cat_obj_created(self):
        self.assertIsInstance(self.cat,models.Category)
        
    # unit test 2
    def test_dunder_str(self):
        self.assertEqual(str(self.cat), self.cat_name)
        
    # unit test 3
    # def test_verbose_is_set(self):
    #     #name = "Categories"
    #     #self.assertEqual(name, self.Category._meta.verbose_name_plural)
    #     assert self.category._meta.verbose_name_plural=='Categories'
    
    #unit test 3
    def test_verbose_name_plural(self):
        #self.assertEqual('Categories',self.cat._meta.verbose_name_plural)
        name='Categories' #in verbose of category model
        self.assertEqual(name,self.cat._meta.verbose_name_plural)