import requests
from bs4 import BeautifulSoup
import pandas as pd

name_list = []
price_list = []
reviews_list = []
desc_list = []

url = "https://www.airbnb.co.in/s/New-Delhi--India/homes?place_id=ChIJLbZ-NFv9DDkRzk0gTkm3wlI&refinement_paths%5B%5D=%2Fhomes"
r = requests.get(url)
# print(r)
soup = BeautifulSoup(r.text, "lxml")
try:
    while True:
        name = soup.find_all("div", {
            "class": "t1jojoys atm_g3_1kw7nm4 atm_ks_15vqwwr atm_sq_1l2sidv atm_9s_cj1kg8 atm_6w_1e54zos atm_fy_1vgr820 atm_7l_jt7fhx atm_cs_10d11i2 atm_w4_1eetg7c atm_ks_zryt35__1rgatj2 dir dir-ltr"})
        # print(name)
        for i in name:
            n = i.text
            name_list.append(n)
        # print(name_list)

        price = soup.find_all("span", {
            "class": "umg93v9 atm_7l_rb934l atm_cs_1peztlj atm_rd_14k51in atm_cs_kyjlp1__1v156lz dir dir-ltr"})
        for i in price:
            n = i.text
            price_list.append(n)
        # print(price_list)

        reviews = soup.find_all("span", {
            "class": "a8jt5op atm_3f_idpfg4 atm_7h_hxbz6r atm_7i_ysn8ba atm_e2_t94yts atm_ks_zryt35 atm_l8_idpfg4 atm_vv_1q9ccgz atm_vy_t94yts au0q88m atm_mk_stnw88 atm_tk_idpfg4 dir dir-ltr"})
        for i in reviews:
            n = i.text
            reviews_list.append(n)
        # print(reviews_list)

        np = soup.find("a", {"aria-label": "Next"}).get("href")
        cnp = "https://www.airbnb.co.in" + np
        # print(cnp)

        url = cnp
        r = requests.get(url)
        soup = BeautifulSoup(r.text, "lxml")
except:
    pass
min_len = min(len(name_list), len(price_list), len(reviews_list))

df = pd.DataFrame({
    "Name": name_list[:min_len],
    "Prices": price_list[:min_len],
    "Review": reviews_list[:min_len]
})
print(df)
df.to_csv("airbnb_del.csv")
