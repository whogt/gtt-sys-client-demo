"""
Python演示,上传数据
"""

# 申请的应用的信息
import unittest
import time
from src.gtt_sdk import TestReport, dict_encode_test_results

appid = '56dd4df26c9ae36434dda995'
appkey = 'jweDdTOrGcXbVvBqWnIEAf------'


class TestDemo(unittest.TestCase):
    """
    pyunit使用示例
    """

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_first_hello_world_true(self):
        """
        运行失败的用例
        :return:
        """
        self.assertTrue(True, msg='Hello Word是正确的')

    def test_first_hello_world_false(self):
        """
        运行正确的用例
        :return:
        """
        self.assertFalse(False, msg='Hello Word是失败的')


if __name__ == '__main__':
    # TODO 使用Pyunit框架可以构建一个如下的测试结果字典,然后上传到服务器即可
    # 此处为了简单,直接赋值出来

    start_time = time.time()

    # 装载测试用例
    test_cases = unittest.TestLoader().loadTestsFromTestCase(TestDemo)
    # 使用测试套件并打包测试用例
    test_suit = unittest.TestSuite()
    test_suit.addTests(test_cases)
    # 运行测试套件，并返回测试结果
    test_result = unittest.TextTestRunner().run(test_suit)

    end_time = time.time()
    total_time = end_time - start_time

    test_res_dict = dict_encode_test_results(
        test_result,
        run_time=total_time,
        pro_id='57fa12ec4------04a2c69',#按照线上报表系统设计来弄的
        pro_version='2.16.10.10.1'#当前被测试的系统的版本号
    )

    test_report = TestReport()
    test_report.get_api_auth(appid=appid, appkey=appkey)
    test_report.post_unit_test_data(test_res_dict)
