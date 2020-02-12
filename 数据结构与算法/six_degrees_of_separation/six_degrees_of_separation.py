# 六度分割理论的验证，计算百度百科任意两个词条之间的路径

import requests
from urllib.parse import urljoin
from bs4 import BeautifulSoup

class SolutionFound(RuntimeError):
    def __init__(self, message):
        self.message = message


class SixDegreesOfSeparation:
    def __init__(self):
        self.url = 'http://baike.baidu.com/'

    def get_links(self, current_url):
        print(urljoin(self.url, current_url))
        try:
            response = requests.get(urljoin(self.url, current_url))
            soup = BeautifulSoup(response.content)
            content = soup.find('div', {'class': 'main-content'})
        except Exception as e:
            print('{}页面请求出错'.format(current_url))
            return None
        current_set = set()
        words = content.select('a[href*=view]')
        if not words:
            return None
        for word in words:
            # print(word['href'], word.text)
            current_set.add(word['href'])
        # print('在{}页面找到{}个链接'.format(current_url, len(current_set)))
        return current_set

    def construct_dict(self, current_url):
        links = self.get_links(current_url)
        if links:
            return dict(zip(links, [{}]*len(links)))
        else:
            return None

    def search_depth(self, current_url, target_url, link_tree, depth):
        print('在第{}层{}页面中查找'.format(depth, current_url))
        if depth >= depth_max:
            return link_tree
        if not link_tree:
            link_tree = self.construct_dict(current_url)
            if not link_tree:
                print('{}页面中无链接'.format(current_url))
        if target_url in link_tree.keys():
            print('在第{}层{}页面找到{}'.format(depth, current_url, target_url))
            raise SolutionFound('trace ' + current_url)
        for branch_key, branch_value in link_tree.items():
            try:
                link_tree[branch_key] = self.search_depth(branch_key, target_url, branch_value, depth+1)
            except SolutionFound as e:
                print(e.message)
                raise SolutionFound('trace '+current_url)
        return link_tree

if __name__ == '__main__':
    start_url = '/subview/2489/5459693.html'    # 地球
    target_url = '/view/34119.htm'              # 第四纪
    # target_url = '/subview/1689/11849262.htm'   # 毛泽东
    depth_max = 4
    sdos = SixDegreesOfSeparation()
    try:
        sdos.search_depth(start_url, target_url, {}, 1)
        print("未找到{}".format(target_url))
    except SolutionFound as e:
        print(e.message)