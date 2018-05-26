#!/usr/bin/python3
"""
This is the test base module test cases
"""
import sys
import os
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square
import unittest
import json
from io import StringIO
import pep8


class TestBase(unittest.TestCase):
    """
    Here we are creating a TestBase class that has its test cases

    Importing the unittest along with the test cases
    """

    def setup(self):

        """
        Sets up test cases also redirecting stdout
        """
        sys.stdout = StringIO()

    def teardown(self):

        """
        Tears down and cleans up tests after run
        """
        sys.stdout = sys.__stdout__

    def test_pep8_model(self):

        """
        This checks model for pep8
        """
        p8 = pep8.StyleGuide(quiet=True)
        p = p8.check_files(['models/base.py'])
        self.assertEqual(p.total_errors, 0, "fix pep8")

    def test_pep8_test(self):

        """
        This checks the test cases for pep8
        """
        p8 = pep8.StyleGuide(quiet=True)
        p = p8.check_files(['tests/test_models/test_base.py'])
        self.assertEqual(p.total_errors, 0, "fix pep8")

    def test_docstring(self):

        """
        Checking for if docstring
        """
        self.assertIsNotNone(Base.__doc__)

    def test_00_documentation(self):

        """
        Checking to see if there is valid document and if present
        """
        self.assertTrue(hasattr(Base, "__init__"))
        self.assertTrue(Base.__init__.__doc__)
        self.assertTrue(hasattr(Base, "create"))
        self.assertTrue(Base.create.__doc__)
        self.assertTrue(hasattr(Base, "to_json_string"))
        self.assertTrue(Base.to_json_string.__doc__)
        self.assertTrue(hasattr(Base, "from_json_string"))
        self.assertTrue(Base.from_json_string.__doc__)
        self.assertTrue(hasattr(Base, "save_to_file"))
        self.assertTrue(Base.save_to_file.__doc__)
        self.assertTrue(hasattr(Base, "load_from_file"))
        self.assertTrue(Base.load_from_file.__doc__)

    def test_0_id(self):

        """
        Checking if an id method was passed
        """
        Base._Base__nb_objects = 0
        b1 = Base()
        b2 = Base()
        b3 = Base()
        b4 = Base(12)
        b5 = Base()
        self.assertEqual(b1.id, 1)
        self.assertEqual(b2.id, 2)
        self.assertEqual(b3.id, 3)
        self.assertEqual(b4.id, 12)
        self.assertEqual(b5.id, 4)

    def test_1_id(self):

        """
        Checking for an expected result of 1 id
        """
        Base._Base__nb_objects = 0
        base = Base()
        self.assertEqual(base.id, 1)

    def test_2_id(self):

        """
        Checking to see if random args passed could be a pass or fail
        """

        Base._Base__nb__objects = 0
        t1 = Base(22)
        self.assertEqual(t1.id, 22)
        t2 = Base(-33)
        self.assertEqual(t2.id, -33)
        t3 = Base()
        self.assertEqual(t3.id, 1)

    def test_3_est_nb(self):

        """
        Checking to see if the number of objects is private
        """
        b1 = Base(33)
        with self.assertRaises(AttributeError):
            print(b1.nb_objects)
        with self.assertRaises(AttributeError):
            print(b1.__nb_objects)

    def test_4_dictionary(self):

        """
        Checking to see if our dictinary is functional
        """
        r1 = Rectangle(10, 7, 2, 8, 1)
        d1 = r1.to_dictionary()
        j = {'x': 2, 'id': 1, 'y': 8, 'height': 7, 'width': 10}
        jd = Base.to_json_string([d1])
        self.assertEqual(d1, j)
        self.assertEqual(type(d1), dict)
        self.assertEqual(type(jd), str)

    def test_6_from_json_string(self):

        """
        Checking to see if imported json is functional
        """
        string = '[{"id": 9, "width": 10, "height": 11, "x": 12, "y": 13}, \
{"id": 10, "width": 12, "height": 14, "x": 16, "y": 18}]'
        js = Base.from_json_string(s)
        self.assertTrue(type(js) is list)
        self.assertEqual(len(js), 2)

    def test_7_from_json_string_if_empty(self):

        """
        Checking to see if json string input can test empty or None pass
        """
        self.assertEqual(Base.from_json_string(""), [])
        self.assertEqual(Base.from_json_string(None), [])

    def test_10_rectangle(self):
        """
        Checking to see if rectangle was created
        """

        r1 = Rectangle(4, 5, 6)
        r1_d = R1.to_dictionary()
        r2_d2 Rectangle.create(**r1_dict)
        self.assertNotEqual(r1, r2_d2)

    def test_11_square(self):
        """
        Checking to see if square was created
        """
        s1 = Square(44, 55, 66, 77)
        s1_d = S1.to_dictionary()
        s2_d2 = Rectangle.create(**s1_d)
        self.assertNotEqual(s1, s2_d2)

    def test_12_file_rectangle(self):

        """
        Checking to see if saved files load from rectangle
        """
        r1 = Rectangle(33, 34, 35, 26)
        r2 = Rectangle(202, 2)
        save_r1 = [r1, r2]
        Rectangle.save_to_file(save_r1)
        load_r = Rectangle.load_from_file()
        self.assertNotEqual(save_r1, load_r)

    def test_13_file_square(self):
        """
        Checking to see if the saved files load from square
        """

        s1 = Square(22)
        s2 = Square(44, 44, 55, 66)
        save_s1 = [s1, s2]
        Square.save_to_file(save_s1)
        load_s = Square.load_from_file()
        self.assertNotEqual(save_s1, load_s)
