import pandas as pd
import urllib.request
import chardet
import numpy as np
from lxml import etree






# def start():
#     for i in range(1, 21):
#         page = urllib.request.urlopen(
#             'http://www.aastocks.com/tc/ipo/ListedIPO.aspx?iid=ALL&orderby=DA&value=DESC&index=%s' % i)
#         print(page)
#         htmlCode = page.read()
#         dom = etree.HTML(htmlCode)
#         # a_text = dom.xpath('//table/tbody/tr/td/table/tbody/tr/text()')
#         a_text = dom.xpath('//tr[@class="DR"]/td/text()|\
#               //tr[@class="ADR"]/td/a/text()|\
#               //td/span/text()|\
#               //tr[@class="DR"]/td/a/text()|\
#               //tr[@class="ADR"]/td/text()')
#         ret = []
#         for el in a_text:
#             if list(el.split()) != []:
#                 # print(el.split())
#                 ret.append(''.join(el.split()))
#         ret = ret[3:-2]

#         final.append(ret)


# final = []
# start()
# print(final)
# temp = []
# for el in final:
#     temp += el
# ret = np.array(temp)
# ret = ret.reshape(len(ret) // 11, 11)
# df = pd.DataFrame(ret)
# df.to_csv('股票.csv', index=False, encoding='UTF-8-sig')


# lis = [8418, 1895, 6110, 3601, 6820, 3938, 1960, 1876, 8668, 2696, 3928, 1732, 1920, 1073, 2558, 1915, 1949, 2772, 6805,
#        382, 1134, 1912, 6093, 8612, 1931, 1977, 1839, 2180, 924, 3798, 1901, 1930, 1943, 1286, 1701, 1842, 1909, 1849,
#        1951, 1861, 1769, 6117, 1935, 3877, 3692, 6811, 2189, 6055, 667, 1905, 2181, 1521, 3868, 2060, 1817, 2230, 2346,
#        1832, 1903, 1873, 1867, 1857, 1753, 8635, 1780, 6806, 1906, 1545, 3321, 2660, 2718, 6185, 1797, 8537, 6819, 1865,
#        1854, 1897, 3662, 2682, 3316, 8096, 1907, 1563, 1891, 1917, 1158, 150, 2108, 1902, 1872, 1025, 1793, 8607, 2616,
#        2019, 8036, 1827, 1703, 1850, 1896, 1890, 1851, 6162, 2013, 1785, 1767, 2885, 2360, 1841, 8631, 1743, 6058, 1845,
#        1796, 1759, 1713, 3978, 1877, 1820, 1762, 2892, 1675, 1995, 1983, 1992, 8622, 2359, 2798, 8621, 1837, 1860, 3992,
#        3668, 2168, 1119, 1790, 1782, 1761, 780, 6890, 2258, 1835, 3616, 8259, 1755, 1712, 1801, 1034, 8611, 1825, 1653,
#        8613, 1741, 8603, 8516, 8042, 1894, 3990, 6111, 1772, 1939, 1809, 1736, 1540, 1781, 8017, 1787, 1911, 1723, 6862,
#        1748, 3690, 8619, 2680, 2552, 8601, 1969, 1615, 8609, 8482, 1869, 8210, 1783, 1725, 8475, 6160, 788, 1765, 1672,
#        1758, 2048, 8512, 1576, 8525, 8547, 797, 3302, 8540, 8606, 1968, 1715, 1721, 2051, 1775, 1731, 6860, 3700, 8219,
#        8140, 1760, 1739, 1996, 1773, 1746, 1652, 8502, 6190, 8223, 1810, 1763, 2262, 8305, 1592, 6100, 1620, 8146, 1749,
#        1587, 1916, 2003, 6098, 8357, 1806, 8403, 1751, 1757, 6119, 1451, 8545, 8490, 1978, 3613, 1598, 8536, 8521, 8105,
#        2119, 8391, 1752, 1742, 1750, 8527, 8107, 1833, 1671, 8151, 8511, 1726, 8451, 8507, 8241, 8447, 8372, 1735, 8401,
#        8448, 1716, 2116, 3997, 2779, 807, 8168, 6036, 2377, 2363, 1737, 1705, 1815, 2182, 1621, 1933, 8483, 8526, 8367,
#        8532, 8379, 8040, 8510, 8522, 1183, 1729, 8523, 8535, 8473, 1690, 1990, 3319, 8519, 6829, 1659, 8450, 1719, 1711,
#        8456, 8395, 8136, 2683, 1686, 8513, 8043, 1665, 8287, 2139, 8479, 8371, 6182, 8313, 8285, 8493, 8487, 2448, 2292,
#        6158, 3699, 3309, 8509, 8350, 2025, 8506, 8501, 3738, 1730, 8422, 8485, 784, 2708, 3878, 8419, 1789, 2022, 6877,
#        8377, 839, 1722, 1727, 8385, 6090, 2227, 1475, 1417, 8429, 1697, 8406, 8495, 1997, 1710, 8402, 8118, 8373, 3358,
#        1975, 2858, 8376, 8400, 1706, 6083, 8375, 1337, 8426, 3919, 2122, 1720, 772, 2232, 8436, 1546, 8470, 2663, 6080,
#        8476, 8457, 8430, 2225, 8392, 8480, 8275, 2337, 8065, 8437]


lis = ['01707', '06885', '08445', '06060', '08199', '01651', '08491', '03830', '01696', '08383', '01552', '02863', '01693', '08142', '08152', '08471', 
'08073', '03848', '08465', '08427', '01216', '08291', '08472', '01676', '01649', '08481', '08462', '00994', '08257', '08463', '08297', '06088', '08405', '06113', '01962', '01702', '01695', '01932', '08157', '08469', '08362', '01571', '08460', '01551', '08420', '01630', '08446', '06038', '02269', '01679', '08183', '08431', '08365', '08452', '03329', '01655', '08252', '01257', '08410', '02001', '08409', '08413', '08309', '08455', '08347', '02611', '08412', '01667', '03768', '02281', '02017', '01647', '08439', '01569', '08442', '08421', '03869', '08425', '08423', '08013', '03395', '01985', '06169', '01627', '08417', '01989', '02266', '01660', '03789', '06068', '01518', '08069', '06122', '01575', '01656', '01536', '01637', '01596', '01580', '08062', '01357', '01617', '06066', '01581', '01635', '08160', '01632', '06189', '01629', '01608', '01611', '01272', '06163', '01458', '01633', '03689', '01572', '03686', '01610', '03306', '03320', '08407', '01609', '02113', '01547', '08023', '02166', '06099', '06858', '01526', '01577', '01658', '01591', '02633', '03893', '02031', '06178', '06816', '02278', '08293', '01589', '08333', '01579', '01612', '01573', '01523', '01560', '08360', '02869', '01586', '08328', '01606', '03958', '01549', '08280', '01420', '02588', '01585', '03626', '02738', '01243', 
'01982', '01496', '01469', '01419', '02239', '01578', '02016', '01557', '02138', '06833', '02768', '03963', '01565', '03301', '01459', '03773', '03326', '03678', '01799', '01548', '01558', '01568', '06196', '01543', '01197', '01662', '01786', '03600', '02289', '01979', '01447', '03996', '00331', '01341', '00416']


dic = {
    '招股日期': '',
    '定價日期': '',
    '公佈售股結果日期': '',
    '退票寄發日期': '',
    '上市日期': '',
    '上市市場': '',
    '行業': '',
    '背景': '',
    '業務主要地區': '',
    '網址': '',
    '每手股數': '',
    '招股價': '',
    '上市市值': '',
    '香港配售股份數目': '',
    '每股市盈率': '',
    '每股預測盈利': '',
    '每股預測市盈率': '',
    '保薦人': '',
    '包銷商': '',
    '收款銀行': '',
    'eIPO': ''
}


def detail():
    counter = 0
    for i in lis:
        counter += 1
        page = urllib.request.urlopen(
            
            
            'http://www.aastocks.com/tc/stocks/market/ipo/upcomingipo/company-summary?symbol=%s#info' % i
            )
        print(page)
        print('-------------------')
        print(str(counter)+' / ' + str(len(lis)))
        htmlCode = page.read()
        dom = etree.HTML(htmlCode)
        res = []
        # a_text = dom.xpath('\
        #       //td[@class="defaulttitle"]/text()|\
        #       //td[@class="defaulttitle2"]/text()|\
        #       //td[@class="defaulttitle"]/following-sibling::*/a/text()|\
        #       //td[@class="defaulttitle"]/following-sibling::*/text()|\
        #       //td[@class="defaulttitle2"]/following-sibling::*/text()'
        #                    )
        a_text = dom.xpath('//table[@class="ns2 mar15T"]/tbody/tr/td/text()')
        # a_text = dom.xpath('//table/tbody/tr/td/text()')

        ret = []
        for el in a_text:
            if list(el.split()) != [] and list(el.split()) != ['('] and list(el.split()) != [')'] and list(
                    el.split()) != ['相關往績']:
                # print(el.split())
                ret.append(el.split())

        for i in range(len(ret)):
            if ''.join(ret[i]) in dic:
                dic[''.join(ret[i])] = ret[i + 1]

        for el in dic.values():
            el = ''.join(el)
            res.append(el)
        temp.append(res)


temp = []
detail()
print(temp)
df = pd.DataFrame(temp)
df.to_csv('detail.csv', index=False, encoding='UTF-8-sig')
