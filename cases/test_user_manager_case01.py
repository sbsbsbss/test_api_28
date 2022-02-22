from apis.user_manager_api import UserManagerApi

import unittest

from data.user_manager_data import user_manager_data

class TestUserManagerCase(unittest.TestCase):

    user_id = 139

    @classmethod

    def setUpClass(cls) -> None:
        cls.user = UserManagerApi()

    # 实现添加测试用例
    # @unittest.skip("暂时跳过")
    def test_add_user(self):
        # 1.定义数据
        # 2.调用添加管理员接口
        result = self.user.add_user(user_manager_data['username'],user_manager_data['password'])

        # 获取id值，用来更新账号id
        if result.get('data').get('erron'):
            TestUserManagerCase.user_id = result.get('data').get('erron')

        # 3.进行断言
        self.assertEqual(0,result.get('errno'))

    # 实现编辑测试用例
    # @unittest.skip("暂时跳过")
    def test_edit_user(self):
        result = self.user.edit_user(TestUserManagerCase.user_id,user_manager_data['new_user'],user_manager_data['password'])
        self.assertEqual(0,result.get('errno'))

    # 实现查询测试用例
    # @unittest.skip("暂时跳过")
    def test_get_user(self):
        result = self.user.get_user()
        self.assertEqual(0,result.get('errno'))

    # 实现删除测试用例
    # @unittest.skip("暂时跳过")
    def test_delete_user(self):
        result = self.user.delete_user(TestUserManagerCase.user_id,user_manager_data['new_user'],user_manager_data['password'])
        self.assertEqual(0,result.get('errno'))









