# -*- encoding: utf-8 -*-
'''
@File    :   feiying_api.py
@Time    :   2020/01/10 10:40:04
@Author  :   bingjian.cui 
@Version :   1.0
@Contact :   bingjian.cui@percent.cn
@Desc    :   科大讯飞飞鹰校对系统API， http://202.85.216.21:8095/review
'''

# here put the import lib
import requests
from lxml import etree


class FeiYingAPI:
    def __init__(self):
        pass

    def fetch_page(self, text, text_category=0):
        """
        :description:
        :param text_category: 0:通用领域，1:教育领域
        :return:
        """
        url = 'http://202.85.216.21:8095/review'
        headers = {
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3',
            'Accept-Encoding': 'gzip, deflate',
            'Accept-Language': 'zh-CN,zh;q=0.9',
            'Cache-Control': 'no-cache',
            'Connection': 'keep-alive',
            'Cookie': 'csrftoken=Nl4l1iHg0gIjJMjGbfpPhjo1G3vmk3lrVLAbeK9ojdhIkbv2hTGGrzzyca4yiORM',
            'Host': '202.85.216.21:8095',
            'Origin': 'http://202.85.216.21:8095',
            'Referer': 'http://202.85.216.21:8095/review',
            'Upgrade-Insecure-Requests': '1',
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.94 Safari/537.36'
        }
        post_data = {
            'category': text_category,
            'mode': 1,
            'textContent': text
        }
        response = requests.post(url, data=post_data, headers=headers)
        return response.text


    def parse_page(self, page_content):
        check_result = dict()
        doc = etree.HTML(page_content)
        correct_all_category = doc.xpath('//div[@id="right_container_corrects"]/div')
        for correct_each_category in correct_all_category:
            correct_category = correct_each_category.xpath('./h2/text()')[0]
            # error_list = correct_each_category.xpath('./div/div[@class="error-list"]/div[@class="error-item"]/@data-json')
            # print(correct_category)
            # print(error_list)
            check_result[correct_category] = []
            error_detail_list = correct_each_category.xpath('./div/div[@class="error-list"]/div[@class="error-item"]/div[@class="error-item-right"]')
            for error_detail in error_detail_list:
                correct_sub_category = error_detail.xpath('./div[@class="error-item-right-top"]/span[2]/text()')
                error_content = error_detail.xpath('./div[@class="error-item-right-top"]/span[@style="color:red;"]//text()')
                correct_content = error_detail.xpath('./div[@class="error-item-right-top"]/span[@class="correct"]//text()')
                error_location = error_detail.xpath('./div[@class="error-item-right-bottom"]/div/span/text()')
                correct_detail_dict = {
                    'corrent_sub_category': ''.join(correct_sub_category).strip() if correct_sub_category else None,
                    'error_content': ''.join(error_content).strip() if error_content else None,
                    'correct_content': ''.join(correct_content).strip() if correct_content else None,
                    'error_location': ''.join(error_location).strip().strip('错误位置：') if error_location else None
                }
                check_result[correct_category].append(correct_detail_dict)
        return check_result


    def main(self, text):
        page_html = self.fetch_page(text)
        check_result = self.parse_page(page_html)
        return check_result


if __name__ == '__main__':
    fy_api = FeiYingAPI()
    text = """
    国务院办公厅关于开展城镇小区配套幼儿园治理工作的通知
 国办发〔2019〕3号
 各省自治区直辖市人民政府，国院各部委各直属机构，
 城镇小区配套建设幼儿园是城镇公共公共服务设施建设的重要内容，是扩大普惠性学前教育资源的重要途径，是保障和改善民生的重要举措。
 2018年11月，党中央国务院印发《关于学前教育深化改革规范发展的若干意见》
 提出规饭小区配套幼儿园建设使用，并对小区配幼儿园规划建设移交办园等情况进行治理作出部署。
 为落相关要求，经国务院同意，现就开展治理工作有关事项通知如下，：
 一、总体要求：
 以习近平新时代中国特色社会主义思想为指导，全面贯彻党的十九大和十九届二中三中全会精神，落实全国教大会部署，
 坚持以人民为中心的发展思想，认镇履行政府责任，依法落实城镇公共服务设施建设规定，
 着力构建以普惠性资源为主体的学前教育公共服务体系，聚焦小区配套幼儿园规划建设移交办园等环节存在的突出问题开展治理，
 进一步提高雪前教育公益普惠水平，切实办好学前教育，满足人民群众对幼有所育的期盼。
 二、工作任务：
 1.城镇小区严格依标配建幼儿园，严格遵循《中华人民共和国城乡规划法》和《城市居住区规划设计标准GB50180，
 老城区棚户区改造新城开发和居住区健设易地扶贫搬迁应将配套建设幼儿园纳入公共管理和公共服务设施建设规划，
 并相关标准和规范予以建设，城镇小区没有规划配套幼儿园或规画不足，或者有完整规划但并建设不到位的，要衣据国家和地方配建标准，
 通过补建改建或就近新建置换购置等方式予以解决，对存在配套幼儿园缓建缩建停建不建和建而不交等问题的，在整改到位之前,不得办理俊工验收.
 2.确保小区配套幼儿园如期移交
 已建成的小区配套幼儿园应按照规定机时移交当地教育行政部门，未移交当地教育行政部门的应先期完成移交，
 对已挪作他用的要采取有效措施予以收回，有关部门要按规定对移交的幼儿园办理土地园舍移交及资产登记手续
 3.规范小区配套幼儿园使用
 小区配套幼儿园移交当地教育行政部门后，从应当由教育行政部门办成公办园或委托办成普惠性民办园，不得办成营利性幼儿园。
 办成公办园的，当地政府及有关部门要做好机构编制教师配备等方面的工作；委托办成普惠性民办园的，
 要做好对相关机构资质管理能力卫生安全及保教质量等方面的审核，明确补助标准，加强对普惠实效及质量方面的动态监管
 三、工作措施
 1.摸低排查
 各地以县市区为单位，对城镇小区配套幼儿园情况进行的全面摸底排查，针对规划配建移交使用不到位等情况，,分别列出清单建立台账
 该项工作于2019年4月底前完成。
 2.全面整改
 针对摸底排查出的问题，从实际出发，认真制定有针对性的整改措施，按照一事一议一园一案的要求逐一进行整改。
 对于已经建成需要办理移交手续的，原则上于2019年，6月底前完成；对于需要回收智换购置的，原则上于2019年9月底前完成；
 对于需要补建改建新建的，原则上于2019年12月底前完成相关建设规划，2020年12月底前完成项目竣工验收
 3.监督评估
 对各地自查摸排整改等环节加强督导监督和评估，并针对关键环节适时进行抽查，对落实不力整改不到位的地区进行通报。
 四、组织实施
 1.建立治理工作协调机制
 成立城镇小区配套幼儿园幼儿园治理工作小组，组长由协助分管教育工作的国务院副秘书长担认，
 成员由教育部住房城乡建设部发展改革委民政部自然资源部等部门负责同志组成，治理工作联合办公室设在教育部住房城乡建设部
 各地要参照建立相应工作机制，加强治理工作协调。
    """
    page = fy_api.fetch_page(text)
    check_result = fy_api.parse_page(page)
    print(check_result)
