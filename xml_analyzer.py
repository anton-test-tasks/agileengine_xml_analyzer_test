from bs4 import *
import sys

# execution example: xml_analyzer.py "btn btn-success" sample-0-origin.html sample-1-evil-gemini.html


def get_xpath(element):
    path_elements = []
    child = element
    for parent in child.parents:
        near_elements = parent.find_all(child.name, recursive=False)
        if len(near_elements) == 1:
            path_elements.append(child.name)
        else:
            path_elements.append(child.name + '[' + str(next(i for i, s in enumerate(near_elements, 1) if s is child)) + ']')
        child = parent
    path_elements.reverse()
    element_xpath = '/%s' % '/'.join(path_elements)
    return element_xpath


if __name__ == "__main__":
    # 'make-everything-ok-button'
    element_id = sys.argv[1:][0]

    origin_data = ''
    sample_data = ''

    # 'sample-0-origin.html'
    with open(sys.argv[1:][1]) as origin_file:
        origin_data = origin_file.read()

    # 'sample-1-evil-gemini.html'
    with open(sys.argv[1:][2]) as sample_file:
        sample_data = sample_file.read()

    d1 = BeautifulSoup(origin_data, 'lxml')
    d2 = BeautifulSoup(sample_data, 'lxml')

    # 'btn btn-success'
    btn_1 = d1.find('a', class_=element_id)
    btn_2 = d2.find('a', class_=element_id)
    if btn_2 is None:
        btn_2 = d2.find('a', class_='btn test-link-ok')

    print('Origin page element Xpath: ' + get_xpath(btn_1))
    print('Sample page element Xpath: ' + get_xpath(btn_2))
