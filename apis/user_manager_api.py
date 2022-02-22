from apis.base import Base
from loguru import logger
import unittest
# 实现用户的增删改查
from setting import LOGIN_INFO

class UserManagerApi(Base):

    def __init__(self):
        self.add_path = "/admin/admin/create"
        self.edit_path = "/admin/admin/update"
        self.del_path = "/admin/admin/delete"
        self.get_path = "/admin/admin/list?page=1&limit=20&sort=add_time&order=desc"

    # 新增管理员:
    def add_user(self,username,password,**kwargs):
        user_url = self.get_url(self.add_path)
        user_data = {'username':username,'password':password}
        if kwargs:
            user_data.update(**kwargs)
            logger.info("新增管理员请求体为:{}".format(user_data))
        return self.post(user_url,user_data)

    # 编辑管理员:
    def edit_user(self,user_id,username,password,**kwargs):
        user_url = self.get_url(self.edit_path)
        user_data = {'id':user_id,'username':username,'password':password}
        if kwargs:
            user_data.update(**kwargs)
            logger.info("编辑管理员请求体为:{}".format(user_data))
        return self.post(user_url,user_data)

    # 删除管理员:
    def delete_user(self,user_id,username,password,**kwargs):
        user_url = self.get_url(self.del_path)
        user_data = {'id':user_id,'username':username,'password':password}
        if kwargs:
            user_data.update(**kwargs)
            logger.info("删除管理员请求体为:{}".format(user_data))
        return self.post(user_url,user_data)

    # 查询管理员:
    def get_user(self):
        user_url = self.get_url(self.get_path)
        return self.get(user_url)


