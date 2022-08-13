# import pyfiglet
# baner = pyfiglet.figlet_format("matn baner",font=)
# #میزنیم و فونت ها میاد ار اونجا انتهاب میکنبم pyfiglet -l توی سی ام دی 
# print(baner)
# # اگه بخوایم از این بنر در جای دیگه استفاده کنیم
# # در اون کد مینویسیم
# #from اسم import اسم تابع
import pyfiglet
def banner(text,font_1):
    banner_1 = pyfiglet.figlet_format(text,font=font_1)
    print(banner_1)