from django.test import TestCase

# Create your tests here.
from django.test import TestCase, Client

from .models import Student

class StudentTestCase(TestCase):
    def setUp(self):
        Student.objects.create(
            name='关茂柠',
            sex=1,
            email='1812711281@qq.com',
            profession='计算机科学与技术',
            qq='1852',
            phone='365124',
        )

    def test_create_and_sex_show(self):
        student = Student.objects.create(
            name='huyang',
            sex=1,
            email='1812526281@qq.com',
            profession='程序员',
            qq='5689',
            phone='25687',
        )
        self.assertEqual(student.sex_show, '男', '性别字段内容和展示不一致！')

    def test_filter(self):
        student = Student.objects.create(
            name='huyang',
            sex=1,
            email='1812526281@qq.com',
            profession='程序员',
            qq='5689',
            phone='25687',
        )
        name = '关茂柠'
        students = Student.objects.filter(name=name)
        self.assertEqual(students.count(), 1, '应该只存在一个名称为{}的记录！'.format(name))

    def test_get_index(self):
        # 测试首页的可用性
        client = Client()
        response = client.get('/')
        self.assertEqual(response.status_code, 200, 'status code must be 200!')

    def test_post_student(self):
        client = Client()
        data = dict(
            name = 'test_for_post',
            sex=1,
            email='333@dd.com',
            profession='程序员',
            qq='22222',
            phone='15889667325',
        )
        response = client.post('/', data)
        self.assertEqual(response.status_code, 302, 'status code must be 302!')

        response = client.get('/')
        self.assertTrue(b'test_for_post' in response.content, 'response content must contain `test_for_post`')